from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

CATEGORY_URLS = {
    "Medical": "medical-jobs",
    "Engineering": "engineering-jobs",
    "Law": "llb-jobs",
    "Finance": "mba-jobs",
    "Nurse": "staff-nurse-jobs",
    "Pharmacy": "pharmacy-jobs",
    "Dental": "bds-jobs",
    "Aviation": "aeronautical-engineering-jobs",
    "Naval": "indian-navy-recruitment",
    "Hotel Management": "hotel-management-jobs",
    "Sports Quota": "sports-quota-jobs",
    "Architecture": "architectural-engineering-jobs",
    "ITI/Diploma": "iti-jobs",
    "Arts": "m-a-jobs",
    "Agriculture": "agricultural-engineering-job",
    "Teacher Training": "b-ed-jobs",
    "Any Degree": "any-degree-jobs"
}

def format_state_name(state_name):
    """Converts state name to the required URL format."""
    return state_name.lower().replace(" ", "-")

def scrape_allgovernmentjobs_selenium(category_or_url, max_pages=5):
    """Scrapes job listings based on category or state search."""

    if category_or_url in CATEGORY_URLS:
        base_url = f"https://allgovernmentjobs.in/{CATEGORY_URLS[category_or_url]}"
    else:
        base_url = category_or_url  # If it's a URL (state search)

    options = Options()
    options.add_argument("--headless")  
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(base_url)
    time.sleep(3)

    all_jobs = []
    page_count = 0

    while page_count < max_pages:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        job_cards = soup.find_all('div', class_='card-body p-3')

        for job_card in job_cards:
            title_tag = job_card.find('div', class_='card-title h6 mb-0')
            title = title_tag.text.strip() if title_tag else 'No title available'

            date_tag = job_card.find('div', class_='mb-1 text-secondary _ln')
            job_date = date_tag.text.strip() if date_tag else 'No date available'

            description_tag = job_card.find('div', class_='content')
            description = description_tag.text.strip() if description_tag else 'No description available'

            apply_tag = job_card.find('div', class_='mt-3').find('a', href=True) if job_card.find('div', class_='mt-3') else None
            apply_link = apply_tag['href'] if apply_tag else 'No link available'

            all_jobs.append({
                'title': title,
                'date': job_date,
                'description': description,
                'apply_link': apply_link
            })

        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            next_button.click()
            time.sleep(3)
            page_count += 1
        except:
            break

    driver.quit()
    return all_jobs
