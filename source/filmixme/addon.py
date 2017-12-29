# -*- coding: utf-8 -*-

from xbmcswift2 import Plugin
plugin = Plugin()


@plugin.route('/')
def index():
    return [
        {'label': plugin.get_string(30001), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30002), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30003), 'path': plugin.url_for('void')},

        {'label': plugin.get_string(30004), 'is_playable': False, 'path': plugin.url_for('void')},

        {'label': plugin.get_string(30005), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30006), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30007), 'path': plugin.url_for('void')},
        {'label': plugin.get_string(30008), 'path': plugin.url_for('void')},
    ]


@plugin.route('/void')
def void():
    return plugin.finish(succeeded=False)

if __name__ == '__main__':
    plugin.run()
