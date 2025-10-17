import json
import pytest
from youtube_search.search import search_youtube, _youtube_api_search, _html_fallback_search, VideoResult, YouTubeSearchError


class DummyResp:
    def __init__(self, status_code=200, text='', json_data=None):
        self.status_code = status_code
        self.text = text
        self._json = json_data

    def json(self):
        if self._json is None:
            raise ValueError('no json')
        return self._json


def test_youtube_api_search_success():
    sample = {
        'items': [
            {'id': {'videoId': 'abc123'}, 'snippet': {'title': 'Test Video', 'channelTitle': 'Tester'}}
        ]
    }

    def fake_get(url, params=None, timeout=None):
        return DummyResp(status_code=200, json_data=sample)

    res = _youtube_api_search('query', 1, api_key='key', http_get=fake_get)
    assert isinstance(res, list)
    assert len(res) == 1
    assert res[0].video_id == 'abc123'
    assert res[0].title == 'Test Video'
    assert res[0].channel == 'Tester'


def test_youtube_api_search_http_error():
    def fake_get(url, params=None, timeout=None):
        return DummyResp(status_code=403, text='Forbidden')

    with pytest.raises(YouTubeSearchError):
        _youtube_api_search('q', 1, api_key='key', http_get=fake_get)


def test_html_fallback_parsing():
    # Create a minimal page with embedded ytInitialData JSON containing a videoRenderer
    initial = {
        'contents': {
            'twoColumnSearchResultsRenderer': {
                'primaryContents': {
                    'sectionListRenderer': {
                        'contents': [
                            {'itemSectionRenderer': {'contents': [
                                {'videoRenderer': {
                                    'videoId': 'vid1',
                                    'title': {'runs': [{'text': 'T1'}]},
                                    'ownerText': {'runs': [{'text': 'Ch'}]}
                                }}
                            ]}}
                        ]
                    }
                }
            }
        }
    }
    page = '... var ytInitialData = ' + json.dumps(initial) + ';</script>...'

    def fake_get(url, timeout=None):
        return DummyResp(status_code=200, text=page)

    res = _html_fallback_search('q', 3, http_get=fake_get)
    assert len(res) == 1
    assert res[0].video_id == 'vid1'
    assert res[0].title == 'T1'
    assert res[0].channel == 'Ch'


def test_html_fallback_no_json():
    def fake_get(url, timeout=None):
        return DummyResp(status_code=200, text='no data here')

    with pytest.raises(YouTubeSearchError):
        _html_fallback_search('q', 1, http_get=fake_get)


def test_search_youtube_validation():
    with pytest.raises(ValueError):
        search_youtube('')  # Empty query

    with pytest.raises(ValueError):
        search_youtube('test', max_results=0)  # Invalid max_results


def test_search_youtube_fallback_to_api():
    calls = []
    
    def fake_get(url, params=None, timeout=None):
        calls.append(url)
        if 'youtube.com' in url:
            raise YouTubeSearchError("HTML parsing failed")
        return DummyResp(status_code=200, json_data={'items': []})

    # Should try HTML first, then fall back to API
    search_youtube('test', api_key='key', prefer_api=False, http_get=fake_get)
    assert len(calls) == 2
    assert 'youtube.com' in calls[0]  # First try HTML
    assert 'googleapis.com' in calls[1]  # Then fallback to API