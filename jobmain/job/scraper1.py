import requests
from bs4 import BeautifulSoup

def scrape_evidyarthi_jobs(search_term, page_no=1):
    url = f"https://www.evidyarthi.in/sarkari-naukri/?s={search_term}&paged={page_no}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code != 200:
            print("Failed to retrieve the page from eVidyarthi")
            return []

        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = []

        # Extract job details
        for job in soup.find_all('h2', class_='entry-title'):
            title_tag = job.find('a', class_='entry-title-link')
            description_tag = job.find_next('div', class_='entry-content').find('p')

            if title_tag:
                title = title_tag.text.strip()
                apply_link = title_tag['href']
                description = description_tag.text.strip() if description_tag else 'No description available'

                job_listings.append({
                    'title': title,
                    'apply_link': apply_link,
                    'description': description,
                })

        return job_listings

    except requests.RequestException as e:
        print(f"Error fetching data from eVidyarthi: {e}")
        return []
