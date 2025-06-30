import re
import spacy
import docx2txt
import pdfplumber

# Load English tokenizer, POS tagger, etc.
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    text = ''
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path)

def extract_email(text):
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return email[0] if email else None

def extract_phone(text):
    phone = re.findall(r'\+?\d[\d\s]{9,}', text)
    return phone[0] if phone else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            return ent.text
    return None

def extract_skills(text, skills_db):
    skills_found = []
    text_lower = text.lower()
    for skill in skills_db:
        if skill.lower() in text_lower:
            skills_found.append(skill)
    return list(set(skills_found))

# Predefined skill set (you can expand it)
skills_list = ['Python', 'Java', 'SQL', 'Excel', 'Machine Learning', 'Data Analysis', 'Communication']

# File input
file_path = "vaibhav resume final.pdf"  # or "resume.docx"

# Choose parser based on file type
if file_path.endswith('.pdf'):
    resume_text = extract_text_from_pdf(file_path)
elif file_path.endswith('.docx'):
    resume_text = extract_text_from_docx(file_path)
else:
    raise ValueError("Unsupported file format")

# Extract data
name = extract_name(resume_text)
email = extract_email(resume_text)
phone = extract_phone(resume_text)
skills = extract_skills(resume_text, skills_list)

# Display
print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills)
