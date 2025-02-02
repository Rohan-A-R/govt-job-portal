from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException

def scrape_data(search_term, page_no=1):
    # Build URL with the page number (default is 1)
    url = f"https://services.india.gov.in/service/search?kw={search_term}&page_no={page_no}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=20)
        if response.status_code != 200:
            print("Failed to retrieve the page")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        job_listings = []

        # Adjust selector based on the page structure:
        for job in soup.find_all('div', class_='edu-lern-con'):  # Update with the correct container class
            job_link = job.find('a', class_='ext-link')
            job_description = job.find('p')
            
            if job_link:
                title = job_link.text.strip()
                apply_link = job_link['href']
                description = job_description.text.strip() if job_description else 'No description available'
                
                job_listings.append({
                    'title': title,
                    'apply_link': apply_link,
                    'description': description,
                })
        
        return job_listings

    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []




def job_listings(request):
    # Capture search term and page number from the URL
    search_query = request.GET.get('search', '').strip()
    page_no = request.GET.get('page_no', '1')

    # Ensure page_no is an integer (default to 1 if conversion fails)
    try:
        page_no = int(page_no)
        if page_no < 1:
            page_no = 1
    except ValueError:
        page_no = 1

    if search_query:
        scraped_data = scrape_data(search_query, page_no)
    else:
        scraped_data = []

    context = {
        'scraped_data': scraped_data,
        'search_query': search_query,
        'page_no': page_no,
    }
    return render(request, 'home.html', context)
