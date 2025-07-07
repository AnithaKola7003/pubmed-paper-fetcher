import requests
from typing import List

def search_pubmed(query: str) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": "10"
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_details(ids: List[str]) -> str:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    return response.text
 
