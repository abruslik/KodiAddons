# -*- coding: utf-8 -*-

from defines import *
from bs4 import BeautifulSoup
import http
from xbmcswift2 import Plugin
plugin = Plugin()


def load_page(page=1, category=''):
    url = SITE_URL + '/' + category + '/page/' + str(page)
    html = http.get(url)
    soup = BeautifulSoup(html, 'html5lib')
    paging = parse_pagination(soup, page)
    items = get_list(soup)
    items = add_list_paging(items, category, paging)
    return items


def get_list(soup):
    array = []
    articles = soup.select('article.shortstory')
    for div in articles:
        element_href = div.find('div', class_='short')
        element_quality = div.select('div.full div.quality')
        element_year = div.select('div.year a')
        element_genre = div.select('div.full span.item-content')
        element_director = div.select('span[itemprop="director"]')

        movie_poster = element_href.find('img', class_='poster').get('src')
        movie_url = div.select('a.watch')[0].get('href')

        movie_name = div.select('div.full h2.name a')[0].get_text().strip()
        movie_origin_name = div.select('div.origin-name')[0].get_text().strip()
        movie_year = element_year[0].get_text() if len(element_year) > 0 else ''
        movie_genre = element_genre[0].get_text() if len(element_genre) > 0 else ''
        movie_format = '[{0}]'.format(element_quality[0].get_text().strip()) if len(element_quality) > 0 else ''
        movie_director = element_director[0].get_text().strip() if len(element_director) > 0 else ''

        add_info = []
        if movie_year != '':
            add_info.append(movie_year)
        if movie_genre != '':
            add_info.append(movie_genre)

        label = movie_name + ' [COLOR white][' + ', '.join(add_info) + '][/COLOR] ' + movie_format

        info = {
            'type': 'Video',
            'originaltitle': movie_origin_name,
            'year': movie_year,
            'genre': movie_genre,
            'director': movie_director
        }

        array.append({
            'label': label,
            'icon': movie_poster,
            'path': plugin.url_for('show_translations', url=movie_url, info=info),
            'info': info
        })
    return array


def add_list_paging(items, category, paging_info):
    if 'pageprev' in paging_info:
        items.insert(0, {
            'label': plugin.get_string(30101),
            'path': plugin.url_for(category,
                                   page=str(paging_info['pageprev']),
                                   category=category,
                                   update=True)
        })
    if 'pagenext' in paging_info:
        items.append({
            'label': plugin.get_string(30102),
            'path': plugin.url_for(category,
                                   page=str(paging_info['pagenext']),
                                   category=category,
                                   update=True)
        })
    return items


def parse_pagination(soup, page):
    paging_info = {'pagenum': int(page)}
    if len(soup.select('div.navigation a.next')) > 0:
        paging_info['pagenext'] = int(page) + 1
    if len(soup.select('div.navigation a.prev')) > 0:
        paging_info['pageprev'] = int(page) - 1
    return paging_info
