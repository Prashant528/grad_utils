'''
INPUT:
IEEE detects bots trying to scrape. So, we save the website on our desktop and then scrape the saved file.
Give the link (file links) of the saved (html) 'results' page of your search in base_urls list.
Doesn't move to next page dynamically yet.

OUTPUT:
Prints the list of papers and their links in ACM library.
Exports the results to a spreadsheet.
'''

import requests
import pandas as pd
from bs4 import BeautifulSoup

def scrape_journal_search_results(urls):
    papers = []

    for url in urls:
        print("Scraping new page...")
        # Make a GET request to the search results page
        response = open(url, 'r+')
        soup = BeautifulSoup(response, 'html.parser')

        # Find and extract information about papers
        for result in soup.find_all('div', class_='List-results-items'):  # Update class name based on HTML structure
            title = result.find('a', class_='fw-bold').text.strip()  # Update class name based on HTML structure
            # link = extract_link(result)
            link = result.find('a')['href']
            papers.append({'title': title, 'link': link})
    return papers

def export_to_excel(data, output_file='ieee_search_results.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")

# Example usage
base_urls = ["/Users/prashant/Desktop/IEEE.html"
             , "/Users/prashant/Desktop/IEEE2.html"
             , "/Users/prashant/Desktop/IEEE3.html"
             ]
results = scrape_journal_search_results(base_urls)

if results:
    count = 0
    for paper in results:
        print(f"Title: {paper['title']}")
        print(f"Link: {paper['link']}")
        print("---")
        count = count+ 1
    print("Exporting to excel...")
    export_to_excel(results)
    print("No of papers = count")