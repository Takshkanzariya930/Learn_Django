from django.shortcuts import render
from newsapi import NewsApiClient
from newswebsite.config import NEWS_API_KEY
from typing import Optional, List, Dict, Any

def searchnews(request):
    context: Dict[str, Optional[Any]] = {
        'articles': None,
        'search_query': None,
        'error': None
    }
    
    if request.method == 'POST':
        search_query = request.POST.get('vsearch')
        if search_query:
            try:
                # Initialize News API client
                newsapi = NewsApiClient(api_key=NEWS_API_KEY)
                
                # Get news articles
                news_response = newsapi.get_everything(
                    q=search_query,
                    language='en',
                    sort_by='relevancy',
                    page=1,
                    page_size=6  # Get 6 articles
                )
                
                if news_response['status'] == 'ok':
                    context['articles'] = news_response['articles']
                    context['search_query'] = search_query
                else:
                    context['error'] = 'Failed to fetch news'
            except Exception as e:
                context['error'] = str(e)
        
    return render(request, 'news.html', context)