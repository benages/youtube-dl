# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from .brightcove import BrightcoveLegacyIE
from ..compat import (
    compat_parse_qs,
    compat_urlparse,
)
from ..utils import smuggle_url


class DiscoveryNetworksDeIE(InfoExtractor):
    _VALID_URL = r'https?://(?:www\.)?(?:discovery|tlc|animalplanet|dmax)\.de/(?:.*#(?P<id>\d+)|(?:[^/]+/)*videos/(?P<title>[^/?#]+))'

    _TESTS = [{
        'url': 'http://www.tlc.de/sendungen/breaking-amish/videos/#3235167922001',
        'info_dict': {
            'id': '3235167922001',
            'ext': 'mp4',
            'title': 'Breaking Amish: Die Welt da draußen',
            'description': (
                'Vier Amische und eine Mennonitin wagen in New York'
                '  den Sprung in ein komplett anderes Leben. Begleitet sie auf'
                ' ihrem spannenden Weg.'),
            'timestamp': 1396598084,
            'upload_date': '20140404',
            'uploader_id': '1659832546',
        },
    }, {
        'url': 'http://www.dmax.de/programme/storage-hunters-uk/videos/storage-hunters-uk-episode-6/',
        'only_matching': True,
    }, {
        'url': 'http://www.discovery.de/#5332316765001',
        'only_matching': True,
    }]
    BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1659832546/default_default/index.html?videoId=%s'

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        brightcove_id = mobj.group('id')
        if not brightcove_id:
            title = mobj.group('title')
            webpage = self._download_webpage(url, title)
            brightcove_legacy_url = BrightcoveLegacyIE._extract_brightcove_url(webpage)
            brightcove_id = compat_parse_qs(compat_urlparse.urlparse(
                brightcove_legacy_url).query)['@videoPlayer'][0]
        return self.url_result(smuggle_url(
            self.BRIGHTCOVE_URL_TEMPLATE % brightcove_id, {'geo_countries': ['DE']}),
            'BrightcoveNew', brightcove_id)


class DiscoveryNetworksEsIE(InfoExtractor):
    _VALID_URL = 'https?://(?:www\.)?(?:discoverychannel\.es|dmax\.marca\.com)/(?:.*#(?P<id>\d+)?|(?:[^/]+/)*(?P<title>[^/?#]+)/epis)'

    _TESTS = [{
        'url': 'http://www.dmax.marca.com/series/motor/joyas-sobre-ruedas/episodios-completos/#4591736984001',
        'info_dict': {
            'id': '4591736984001',
            'ext': 'mp4',
            'title': 'Joyas sobre ruedas: Noble M12 GTO 2.5',
            'description': (
                'Las leyendas de la automoción Mike Brewer y Edd China van'
                ' a correr el mayor riesgo de sus carreras: abrir un taller en la co...'),
            'timestamp': 1446502357,
            'upload_date': '20151102',
            'uploader_id': '1378939881',
        },
    }, {
        'url': 'http://www.dmax.marca.com/series/motor/joyas-sobre-ruedas/episodios-completos/',
        'only_matching': True,
    }, {
        'url': 'http://www.dmax.marca.com/player/#5298706050001',
        'only_matching': True,
    }]
    BRIGHTCOVE_URL_TEMPLATE = 'http://players.brightcove.net/1378939881/default_default/index.html?videoId=%s'

    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        brightcove_id = mobj.group('id')
        if not brightcove_id:
            title = mobj.group('title')
            webpage = self._download_webpage(url, title)
            brightcove_legacy_url = BrightcoveLegacyIE._extract_brightcove_url(webpage)
            brightcove_id = compat_parse_qs(compat_urlparse.urlparse(
                brightcove_legacy_url).query)['@videoPlayer'][0]
        return self.url_result(smuggle_url(
            self.BRIGHTCOVE_URL_TEMPLATE % brightcove_id, {'geo_countries': ['ES']}),
            'BrightcoveNew', brightcove_id)
