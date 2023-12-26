'''
INPUT:
IEEE detects bots trying to scrape. So, we save the website on our desktop and then scrape the saved file.
File format for saving 'mhtml'. Saved 'html' doesn't work for some reason.
Give the link(filepath) to the saved 'results' page of your search in base_urls list.
Doesn't move to next page dynamically yet.

OUTPUT:
Prints the list of papers and their links in ACM library.
Exports the results to a spreadsheet.
'''

import email
import pandas as pd
from bs4 import BeautifulSoup

def extract_html_from_mhtml(mhtml_file_path):
    with open(mhtml_file_path, 'rb') as file:
        # Parse the MHTML file using the email module
        message = email.message_from_binary_file(file)

        # Extract HTML content from the MHTML parts
        html_parts = [part.get_payload(decode=True) for part in message.walk() if part.get_content_type() == 'text/html']

        # Join HTML parts into a single string
        html_content = b''.join(html_parts).decode('utf-8')

    return html_content

def scrape_titles_and_links_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    papers = []
    for result in soup.find_all('li', class_='ResultItem col-xs-24 push-m'):  # Update class name based on HTML structure
        title = result.find('span', class_='anchor-text').text.strip()  # Update class name based on HTML structure
        # link = extract_link(result)
        link = result.find('a', class_='anchor result-list-title-link u-font-serif text-s anchor-default')['href']
        papers.append({'title': title, 'link': link})

    return papers

def export_to_excel(data, output_file='elsevier_search_results.xlsx'):
    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)
    print(f"Data exported to {output_file}")

# Example usage
mhtml_file_paths = ['/Users/prashant/Desktop/ELS_test4.mht',
                    '/Users/prashant/Desktop/ELS_test5.mhtml',
                    '/Users/prashant/Desktop/ELS_test6.mhtml',
                    '/Users/prashant/Desktop/ELS_test7.mhtml',
                    '/Users/prashant/Desktop/ELS_test8.mhtml',
                    '/Users/prashant/Desktop/ELS_test9.mhtml',
                    '/Users/prashant/Desktop/ELS_test10.mhtml',
                    '/Users/prashant/Desktop/ELS_test11.mhtml',
                    ]  # Replace with the actual file path

results = []
for mhtml_file_path in mhtml_file_paths:
    html_content = extract_html_from_mhtml(mhtml_file_path)
    results = results+scrape_titles_and_links_from_html(html_content)

count = 0
for paper in results:
    print(f"Title: {paper['title']}")
    print(f"Link: {paper['link']}")
    print("---")
    count = count+ 1
print("Exporting to excel...")
export_to_excel(results)
print(f"No of papers = {count}")
        
