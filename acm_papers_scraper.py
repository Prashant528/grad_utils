'''
INPUT:
Give the link to the 'results' page of your search in base_urls list.
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
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find and extract information about papers
            for result in soup.find_all('li', class_='search__item issue-item-container'):  # Update class name based on HTML structure
                title = result.find('span', class_='hlFld-Title').text.strip()  # Update class name based on HTML structure
                # link = extract_link(result)
                link = result.find('a')['href']
                papers.append({'title': title, 'link': 'https://dl.acm.org'+link})
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
    return papers

def export_to_excel(data, output_file='search_results.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")

# Example usage
base_urls = ["https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29+OR+Keyword%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29&startPage=0&pageSize=50",
              "https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29+OR+Keyword%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29&startPage=1&pageSize=50",
              "https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29+OR+Keyword%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29&startPage=2&pageSize=50",
              "https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29+OR+Keyword%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29&startPage=3&pageSize=50",
              "https://dl.acm.org/action/doSearch?fillQuickSearch=false&target=advanced&expand=dl&AllField=Title%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29+OR+Keyword%3A%28%28%28%22benefits%22+OR+%22advantages%22+OR+%22strengths%22+OR+%22impact%22+OR+%22role%22+OR+%22roles%22+OR+%22effect%22+OR+%22using%22+OR+%22use%22%29+AND+%28%22storytelling%22+OR+%22narratives%22+OR+%22narrations%22+OR+%22stories%22+OR+%22story%22%29%29%29&startPage=4&pageSize=50"
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