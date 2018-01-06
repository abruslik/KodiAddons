# -*- coding: utf-8 -*-

from source.filmixme.resources.lib.defines import *
from source.filmixme.resources.lib.http import *
from bs4 import BeautifulSoup


class TestLibHttp:

    def setUp(self):
        self.url = SITE_URL

    def test_get_request(self):
        bs = BeautifulSoup(get(self.url), 'html5lib')
        logo_element = bs.select('div.logo a')
        assert len(logo_element) == 1
        assert logo_element[0].get('href') == SITE_URL
