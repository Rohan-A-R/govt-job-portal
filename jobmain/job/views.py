from django.shortcuts import render
from .scraper import scrape_data

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
