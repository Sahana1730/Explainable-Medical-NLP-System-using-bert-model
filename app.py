import streamlit as st
import torch
import torch.nn.functional as F
from transformers import BertTokenizer, BertForSequenceClassification
from medical_kb import medical_kb

# Load model
from transformers import BertTokenizer, BertForSequenceClassification

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Sort terms for multi-word matching
sorted_terms = sorted(medical_kb.keys(), key=lambda x: len(x), reverse=True)

# Domain detection
def detect_domain(text):
    text = text.lower()
    if any(word in text for word in ["patient", "blood", "disease"]):
        return "Medical 🏥"
    elif any(word in text for word in ["law", "contract"]):
        return "Legal ⚖️"
    return "General"

# Predict complexity (used only for confidence)
def predict_complex(sentence):
    inputs = tokenizer(sentence, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = F.softmax(outputs.logits, dim=1)

    confidence = torch.max(probs).item()
    label = torch.argmax(probs).item()

    return label, confidence

# Simplification (FIXED 🔥)
def simplify_sentence(sentence):
    changes = []
    sentence_lower = sentence.lower()

    for term in sorted_terms:
        if term in sentence_lower:
            simple = medical_kb[term]["simple"]
            explanation = medical_kb[term]["explanation"]

            # Find exact match in original sentence
            start = sentence_lower.find(term)
            end = start + len(term)

            original_text = sentence[start:end]

            # Replace safely
            sentence = sentence.replace(original_text, f"**{simple}**")

            # Update lowercase after replacement
            sentence_lower = sentence.lower()

            changes.append((term, simple, explanation))

    return sentence, changes

# Main pipeline (UPDATED LOGIC 🔥)
def process_text(text):
    sentences = text.split(".")
    output = []
    all_changes = []
    confidences = []

    for s in sentences:
        s = s.strip()
        if not s:
            continue

        # Get confidence from model
        label, conf = predict_complex(s)
        confidences.append(conf)

        # ALWAYS attempt simplification
        simplified, changes = simplify_sentence(s)

        if changes:
            output.append(simplified)
            all_changes.extend(changes)
        else:
            output.append(s)

    avg_conf = sum(confidences) / len(confidences) if confidences else 0
    return ". ".join(output), all_changes, avg_conf

# ---------------- UI ---------------- #

st.set_page_config(page_title="Medical NLP System", layout="centered")

st.title("🧠 Explainable Medical NLP System")
st.write("Simplifies medical text with explanations and highlights")

text = st.text_area("✍️ Enter text")

if st.button("Simplify 🚀"):

    if text.strip() == "":
        st.warning("Please enter text")
    else:
        domain = detect_domain(text)
        output, changes, confidence = process_text(text)

        st.subheader("📌 Domain")
        st.info(domain)

        st.subheader("📄 Original Text")
        st.write(text)

        st.subheader("✨ Simplified Text")
        st.markdown(output)

        st.subheader("📊 Confidence Score")
        st.write(round(confidence, 2))

        if changes:
            st.subheader("🔍 Changes & Explanations")
            for term, simple, explanation in changes:
                st.write(f"**{term} → {simple}**")
                st.caption(explanation)