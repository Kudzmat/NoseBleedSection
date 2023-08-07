from django.shortcuts import render
from .functions import get_ringer_links


def the_ringer_news(request):

    # get news from theringer.com
    news = get_ringer_links()

    context = {'news': news}

    return render(request, 'nba_news/news.html', context=context)