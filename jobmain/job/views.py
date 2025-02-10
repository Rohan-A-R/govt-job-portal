from django.shortcuts import render
from .scraper import scrape_data  # services.india.gov.in
from .scraper1 import scrape_evidyarthi_jobs  # evidyarthi.in
from django.core.paginator import Paginator

def job_listings(request):
    search_query = request.GET.get('search', '').strip()
    page_no = request.GET.get('page_no', '1')

    try:
        page_no = int(page_no)
        if page_no < 1:
            page_no = 1
    except ValueError:
        page_no = 1

    scraped_data = []
    if search_query:
        # Scraping from multiple websites
        scraped_data_1 = scrape_data(search_query, page_no)  # services.india.gov.in
        scraped_data_2 = scrape_data(search_query, page_no)  # allgovernmentjobs.in
        scraped_data_3 = scrape_evidyarthi_jobs(search_query, page_no)  # evidyarthi.in

        # Add source information and combine the data
        data_with_source = [
            {**job, 'source': 'Government Services'} for job in scraped_data_1
        ] + [
            {**job, 'source': 'Government Jobs'} for job in scraped_data_3
        ]

        data_with_source.sort(key=lambda x: x['title'].lower())

        # Set the sorted data into scraped_data
        scraped_data = data_with_source

    paginator = Paginator(scraped_data, 10) 
    page = paginator.get_page(page_no)

    context = {
        'scraped_data': page.object_list,
        'search_query': search_query,
        'page_no': page_no,
        'paginator': paginator,
        'page': page,
    }
    return render(request, 'home.html', context,)
