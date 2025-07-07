# PubMed Paper Fetcher

## Author
Anitha Kola

## Objective
A Python CLI tool to fetch PubMed research papers and identify those with at least one non-academic author affiliated with a pharmaceutical or biotech company.

## Features
- Uses PubMed eSearch and eFetch API
- Parses XML with BeautifulSoup
- Filters authors based on non-academic/company affiliation
- Saves results to CSV file
- Built using Poetry and Typer

## Technologies Used
- Python
- Typer (CLI)
- Requests
- BeautifulSoup4
- Pandas
- Poetry

## Output Format
The output CSV includes the following columns:
- PubmedID
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Author Email

## How to Run the Project

### 1. Install dependencies:
```bash
poetry install
 
