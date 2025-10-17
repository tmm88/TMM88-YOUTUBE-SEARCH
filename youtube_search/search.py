from dataclasses import dataclass
from typing import List, Optional
import requests
import urllib.parse
import json


@dataclass
class VideoResult:
    video_id: str
    title: str
    channel: Optional[str] = None
    duration: Optional[str] = None

    def url(self) -> str:
        """Return the full YouTube watch URL for this video."""
        return f"https://www.youtube.com/watch?v={self.video_id}"

    def short_url(self) -> str:
        """Return the youtu.be short URL for this video."""
        return f"https://youtu.be/{self.video_id}"


class YouTubeSearchError(Exception):
    pass


def _youtube_api_search(query: str, max_results: int, api_key: str, http_get=requests.get) -> List[VideoResult]:
    base = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": api_key,
    }
    resp = http_get(base, params=params, timeout=10)
    if resp.status_code != 200:
        raise YouTubeSearchError(f"YouTube API error: {resp.status_code} {resp.text}")
    data = resp.json()
    results: List[VideoResult] = []
    for item in data.get("items", []):
        vid = item["id"].get("videoId")
        snip = item.get("snippet", {})
        results.append(VideoResult(video_id=vid, title=snip.get("title", ""), channel=snip.get("channelTitle")))
    return results


def _html_fallback_search(query: str, max_results: int, http_get=requests.get) -> List[VideoResult]:
    q = urllib.parse.quote_plus(query)
    url = f"https://www.youtube.com/results?search_query={q}"
    resp = http_get(url, timeout=10)
    if resp.status_code != 200:
        raise YouTubeSearchError(f"Failed to fetch YouTube search page: {resp.status_code}")
    text = resp.text
    marker = "var ytInitialData ="
    idx = text.find(marker)
    if idx == -1:
        marker2 = "window[\"ytInitialData\"] ="
        idx = text.find(marker2)
        if idx == -1:
            raise YouTubeSearchError("Could not find initial data in YouTube page; fallback failed.")
        idx += len(marker2)
    else:
        idx += len(marker)
    end_idx = text.find(";</script>", idx)
    if end_idx == -1:
        end_idx = text.find(";", idx)
        if end_idx == -1:
            raise YouTubeSearchError("Could not parse initial data JSON")
    json_text = text[idx:end_idx].strip()
    if json_text.endswith(";"):
        json_text = json_text[:-1]
    try:
        data = json.loads(json_text)
    except Exception:
        raise YouTubeSearchError("Failed to decode embedded JSON from YouTube page")

    results: List[VideoResult] = []

    def walk_for_videos(obj):
        if isinstance(obj, dict):
            if 'videoRenderer' in obj:
                vr = obj['videoRenderer']
                vid = vr.get('videoId')
                title_obj = vr.get('title', {}).get('runs', [{}])[0]
                title = title_obj.get('text', '')
                channel = vr.get('ownerText', {}).get('runs', [{}])[0].get('text')
                if vid and title:
                    results.append(VideoResult(video_id=vid, title=title, channel=channel))
            else:
                for v in obj.values():
                    walk_for_videos(v)
        elif isinstance(obj, list):
            for item in obj:
                walk_for_videos(item)

    walk_for_videos(data)
    return results[:max_results]


def search_youtube(query: str, max_results: int = 5, api_key: Optional[str] = None, prefer_api: bool = True, http_get=requests.get) -> List[VideoResult]:
    if not query:
        raise ValueError("Search query cannot be empty")
    if max_results < 1:
        raise ValueError("max_results must be at least 1")
    if api_key and prefer_api:
        return _youtube_api_search(query, max_results, api_key, http_get=http_get)
    try:
        return _html_fallback_search(query, max_results, http_get=http_get)
    except YouTubeSearchError:
        if api_key:
            return _youtube_api_search(query, max_results, api_key, http_get=http_get)
        raise