import re

def is_non_academic(affiliation: str) -> bool:
    company_keywords = ["inc", "pharma", "biotech", "ltd", "corp"]
    academic_keywords = ["univ", "college", "school", "institute", "lab"]
    affil = affiliation.lower()
    return any(word in affil for word in company_keywords) and not any(word in affil for word in academic_keywords)

def extract_email(text: str) -> str:
    match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    return match.group(0) if match else ""
 
