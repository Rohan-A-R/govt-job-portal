from django.shortcuts import render
from .scraper import scrape_data
from .scraper1 import scrape_allgovernmentjobs_selenium, format_state_name
from django.core.paginator import Paginator

def job_listings(request):
    search_query = request.GET.get('search', '').strip()
    page_no = request.GET.get('page_no', '1')
    filter_type = request.GET.get('filter', 'all')
    category = request.GET.get('category', '').strip()

    try:
        page_no = int(page_no)
        if page_no < 1:
            page_no = 1
    except ValueError:
        page_no = 1

    scraped_data = []
    scraped_data_1, scraped_data_2 = [], []

    if category:
        # If category is selected, fetch jobs from that category
        scraped_data_2 = scrape_allgovernmentjobs_selenium(category, page_no)
    elif search_query:
        # Format search query as a state-based URL
        formatted_state = format_state_name(search_query)
        search_url = f"https://allgovernmentjobs.in/govt-jobs-in-{formatted_state}/page/{page_no}"

        if filter_type in ('all', 'services'):
            scraped_data_1 = scrape_data(search_query)  
        if filter_type in ('all', 'jobs'):
            scraped_data_2 = scrape_allgovernmentjobs_selenium(search_url, page_no)

    # Combine results with source labels
    scraped_data = (
        [{**job, 'source': 'Government Services'} for job in scraped_data_1] +
        [{**job, 'source': 'All Government Jobs'} for job in scraped_data_2]
    )

    paginator = Paginator(scraped_data, 10)
    page = paginator.get_page(page_no)

    context = {
        'scraped_data': page.object_list,
        'search_query': search_query,
        'filter_type': filter_type,
        'category': category,
        'page_no': page_no,
        'paginator': paginator,
        'page': page,
    }

    return render(request, 'home.html', context)
