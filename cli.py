import typer
import pandas as pd
from papers.fetcher import search_pubmed, fetch_details
from papers.utils import is_non_academic, extract_email
from bs4 import BeautifulSoup

app = typer.Typer()

@app.command()
def get_papers_list(query: str, file: str = None):
    ids = search_pubmed(query)
    xml_data = fetch_details(ids)

    soup = BeautifulSoup(xml_data, "lxml")
    records = []

    for article in soup.find_all("pubmedarticle"):
        try:
            pmid = article.pmid.text
            title = article.find("articletitle").text
            pub_date = article.find("pubdate").text if article.find("pubdate") else ""
            authors = article.find_all("author")
            non_acad_authors = []
            companies = set()
            email = ""

            for author in authors:
                affil_tag = author.find("affiliation")
                if affil_tag:
                    affil_text = affil_tag.text
                    if is_non_academic(affil_text):
                        name = " ".join([tag.text for tag in author.find_all(["firstname", "lastname"])])
                        non_acad_authors.append(name)
                        companies.add(affil_text)
                        if not email:
                            email = extract_email(affil_text)

            if non_acad_authors:
                records.append({
                    "PubmedID": pmid,
                    "Title": title,
                    "Publication Date": pub_date,
                    "Non-academic Author(s)": "; ".join(non_acad_authors),
                    "Company Affiliation(s)": "; ".join(companies),
                    "Corresponding Author Email": email
                })

        except Exception as e:
            print("Error:", e)

    df = pd.DataFrame(records)

    if file:
        df.to_csv(file, index=False)
        print(f"Saved to {file}")
    else:
        print(df)

if __name__ == "__main__":
    app()
 
