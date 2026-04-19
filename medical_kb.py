medical_kb = {
    "hypertension": {
        "simple": "high blood pressure",
        "type": "disease",
        "explanation": "A condition where blood pressure is too high"
    },
    "myocardial infarction": {
        "simple": "heart attack",
        "type": "disease",
        "explanation": "Occurs when blood flow to heart is blocked"
    },
    "intravenous": {
        "simple": "through a vein",
        "type": "procedure",
        "explanation": "Giving medicine directly into a vein"
    },
    "edema": {
        "simple": "swelling",
        "type": "symptom",
        "explanation": "Swelling caused by fluid buildup"
    },
    "neurological": {
        "simple": "brain-related",
        "type": "domain",
        "explanation": "Related to brain and nervous system"
    },
    "gastrointestinal": {
        "simple": "digestive system",
        "type": "domain",
        "explanation": "Related to stomach and intestines"
    },
    "renal": {
        "simple": "kidney-related",
        "type": "domain",
        "explanation": "Related to kidneys"
    },
    "hepatic": {
        "simple": "liver-related",
        "type": "domain",
        "explanation": "Related to liver"
    },
    "cardiovascular": {
        "simple": "heart-related",
        "type": "domain",
        "explanation": "Related to heart and blood vessels"
    },
    "pharmacological": {
        "simple": "medicine-related",
        "type": "treatment",
        "explanation": "Treatment using drugs"
    }
}
medical_kb.update({

    # Diseases
    "diabetes mellitus": {"simple": "high blood sugar", "type": "disease", "explanation": "Body cannot regulate sugar levels"},
    "pneumonia": {"simple": "lung infection", "type": "disease", "explanation": "Infection causing inflammation in lungs"},
    "tuberculosis": {"simple": "serious lung infection", "type": "disease", "explanation": "Bacterial infection affecting lungs"},
    "arthritis": {"simple": "joint pain", "type": "disease", "explanation": "Inflammation of joints"},
    "osteoporosis": {"simple": "weak bones", "type": "disease", "explanation": "Bones become fragile and brittle"},
    "anemia": {"simple": "low red blood cells", "type": "disease", "explanation": "Reduced oxygen-carrying capacity"},
    "stroke": {"simple": "brain attack", "type": "disease", "explanation": "Blood supply to brain is interrupted"},
    "epilepsy": {"simple": "seizure disorder", "type": "disease", "explanation": "Condition causing repeated seizures"},
    "bronchitis": {"simple": "airway inflammation", "type": "disease", "explanation": "Inflammation of bronchial tubes"},
    "hepatitis": {"simple": "liver infection", "type": "disease", "explanation": "Inflammation of the liver"},

    # Symptoms
    "dyspnea": {"simple": "difficulty breathing", "type": "symptom", "explanation": "Shortness of breath"},
    "tachycardia": {"simple": "fast heart rate", "type": "symptom", "explanation": "Heart beats faster than normal"},
    "bradycardia": {"simple": "slow heart rate", "type": "symptom", "explanation": "Heart beats slower than normal"},
    "cyanosis": {"simple": "bluish skin color", "type": "symptom", "explanation": "Low oxygen in blood"},
    "hypotension": {"simple": "low blood pressure", "type": "symptom", "explanation": "Blood pressure is too low"},
    "hyperglycemia": {"simple": "high blood sugar", "type": "symptom", "explanation": "Too much glucose in blood"},
    "hypoglycemia": {"simple": "low blood sugar", "type": "symptom", "explanation": "Too little glucose in blood"},
    "palpitations": {"simple": "irregular heartbeat", "type": "symptom", "explanation": "Feeling heart beating fast or uneven"},
    "vertigo": {"simple": "spinning sensation", "type": "symptom", "explanation": "Feeling dizzy or off balance"},
    "syncope": {"simple": "fainting", "type": "symptom", "explanation": "Temporary loss of consciousness"},

    # Procedures
    "angioplasty": {"simple": "opening blocked artery", "type": "procedure", "explanation": "Procedure to widen blood vessels"},
    "catheterization": {"simple": "tube insertion", "type": "procedure", "explanation": "Inserting a tube into body"},
    "dialysis": {"simple": "blood cleaning", "type": "procedure", "explanation": "Removes waste from blood when kidneys fail"},
    "endoscopy": {"simple": "internal camera exam", "type": "procedure", "explanation": "Viewing inside body using camera"},
    "laparoscopy": {"simple": "keyhole surgery", "type": "procedure", "explanation": "Minimally invasive surgery"},
    "transfusion": {"simple": "blood transfer", "type": "procedure", "explanation": "Giving blood from donor"},
    "ventilation": {"simple": "breathing support", "type": "procedure", "explanation": "Machine helps breathing"},
    "resuscitation": {"simple": "reviving patient", "type": "procedure", "explanation": "Restoring breathing or heartbeat"},
    "vaccination": {"simple": "disease prevention shot", "type": "procedure", "explanation": "Protects from infections"},
    "biopsy": {"simple": "tissue test", "type": "procedure", "explanation": "Sample taken for analysis"},

    # Treatments
    "antibiotics": {"simple": "bacteria-killing drugs", "type": "treatment", "explanation": "Medicines that kill bacteria"},
    "analgesics": {"simple": "painkillers", "type": "treatment", "explanation": "Relieve pain"},
    "sedation": {"simple": "calming medicine", "type": "treatment", "explanation": "Helps relax or sleep"},
    "immunotherapy": {"simple": "immune treatment", "type": "treatment", "explanation": "Boosts immune system"},
    "rehabilitation": {"simple": "recovery therapy", "type": "treatment", "explanation": "Helps regain ability"},
    "anticoagulants": {"simple": "blood thinners", "type": "treatment", "explanation": "Prevent blood clots"},
    "antipyretics": {"simple": "fever reducers", "type": "treatment", "explanation": "Reduce fever"},
    "antihistamines": {"simple": "allergy medicines", "type": "treatment", "explanation": "Treat allergic reactions"},
    "chemotherapy": {"simple": "cancer drug treatment", "type": "treatment", "explanation": "Uses drugs to kill cancer"},
    "radiotherapy": {"simple": "radiation treatment", "type": "treatment", "explanation": "Uses radiation for cancer"},

    # Body systems / domains
    "respiratory": {"simple": "breathing system", "type": "domain", "explanation": "Related to lungs"},
    "endocrine": {"simple": "hormone system", "type": "domain", "explanation": "Controls hormones"},
    "musculoskeletal": {"simple": "muscle and bone system", "type": "domain", "explanation": "Supports movement"},
    "dermatological": {"simple": "skin-related", "type": "domain", "explanation": "Related to skin"},
    "ophthalmic": {"simple": "eye-related", "type": "domain", "explanation": "Related to eyes"},
    "cardiology": {"simple": "heart study", "type": "domain", "explanation": "Study of heart"},
    "neurology": {"simple": "brain study", "type": "domain", "explanation": "Study of nervous system"},
    "oncology": {"simple": "cancer study", "type": "domain", "explanation": "Study of cancer"},
    "nephrology": {"simple": "kidney study", "type": "domain", "explanation": "Study of kidneys"},
    "gastroenterology": {"simple": "digestive system study", "type": "domain", "explanation": "Study of digestion"}

})