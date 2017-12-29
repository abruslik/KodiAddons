# -*- coding: utf-8 -*-

from source.filmixme.resources.lib.list import *
from bs4 import BeautifulSoup


class TestLibList:

    def test_parse_pagination_page_1(self):
        page = 1
        html = http.get(SITE_URL + '/films/page/' + str(page))
        soup = BeautifulSoup(html, 'html5lib')
        paging = parse_pagination(soup, page)
        assert sorted(paging.keys()) == ['pagenext', 'pagenum']
        assert paging['pagenum'] == 1
        assert paging['pagenext'] == 2

    def test_parse_pagination_page_1(self):
        page = 2
        html = http.get(SITE_URL + '/films/page/' + str(page))
        soup = BeautifulSoup(html, 'html5lib')
        paging = parse_pagination(soup, page)
        assert sorted(paging.keys()) == ['pagenext', 'pagenum', 'pageprev']
        assert paging['pageprev'] == 1
        assert paging['pagenum'] == 2
        assert paging['pagenext'] == 3

