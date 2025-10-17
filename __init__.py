"""YouTube Search Package

This package provides utilities for searching YouTube videos.
"""

from .search import search_youtube, VideoResult, YouTubeSearchError

__all__ = ['search_youtube', 'VideoResult', 'YouTubeSearchError']