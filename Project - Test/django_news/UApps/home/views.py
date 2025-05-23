from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from newsapi import NewsApiClient
from newswebsite.config import NEWS_API_KEY
from typing import Optional, List, Dict, Any

def index(request):
    context: Dict[str, Optional[Any]] = {
        'articles': None,
        'error': None
    }
    
    try:
        # Initialize News API client
        newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        
        # Get news articles
        news_response = newsapi.get_top_headlines(
            language='en',
            page=1,
            page_size=6  # Get 6 articles
        )
        
        if news_response['status'] == 'ok':
            context['articles'] = news_response['articles']
        else:
            context['error'] = 'Failed to fetch news'
    except Exception as e:
        context['error'] = str(e)
        
    return render(request, 'home.html', context)