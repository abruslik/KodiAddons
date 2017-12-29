# -*- coding: utf-8 -*-

import resources.lib.list as List
from resources.lib.list import plugin


@plugin.route('/')
def index():
    return [
        {'label': plugin.get_string(30001), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30002), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30003), 'path': plugin.url_for('void')},

        {'label': plugin.get_string(30004), 'is_playable': False, 'path': plugin.url_for('void')},

        {'label': plugin.get_string(30005), 'path': plugin.url_for('films', page=1, category='films')},
        {'label': plugin.get_string(30006), 'path': plugin.url_for('serialy', page=1, category='serialy')},
        {'label': plugin.get_string(30007), 'path': plugin.url_for('multfilmy', page=1, category='multfilmy')},
        {'label': plugin.get_string(30008), 'path': plugin.url_for('multserialy', page=1, category='multserialy')},
    ]


@plugin.route('/void')
def void():
    return plugin.finish(succeeded=False)


@plugin.route('/list/<category>/<page>')
@plugin.route('/list/<category>/<page>', name='films')
@plugin.route('/list/<category>/<page>', name='serialy')
@plugin.route('/list/<category>/<page>', name='multfilmy')
@plugin.route('/list/<category>/<page>', name='multserialy')
def show_video_list(page=1, category=''):
    items = List.load_page(page, category)

    kwargs = {
        'update_listing': 'update' in plugin.request.args
    }
    return plugin.finish(items, **kwargs)


@plugin.route('/translations/')
def show_translations():
    items = []
    return items

if __name__ == '__main__':
    plugin.run()
