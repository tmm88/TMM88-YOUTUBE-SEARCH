# YouTube Search

A lightweight Python package for searching YouTube videos using either the official YouTube Data API or an HTML fallback method. Perfect for developers who need quick programmatic access to YouTube search results.

## Features

- 🔑 YouTube Data API support with API key
- 🌐 HTML fallback mode when no API key is available
- 🎯 Simple and intuitive interface
- 🔗 Full and short URL generation for videos
- 📦 Easy integration with existing projects

## Installation

```bash
git clone https://github.com/tmm88/TMM88-YOUTUBE-SEARCH.git
cd TMM88-YOUTUBE-SEARCH
pip install -e .
```

## Quick Start

Basic usage example:

```python
from youtube_search import search_youtube

# Search with API key (recommended)
results = search_youtube('python tutorial', max_results=3, api_key='YOUR_API_KEY')

# Or use HTML fallback (no API key required)
results = search_youtube('python tutorial', max_results=3, api_key=None)

# Print results with full URLs
for video in results:
    print(f"Title: {video.title}")
    print(f"Channel: {video.channel}")
    print(f"Full URL: {video.url()}")
    print(f"Short URL: {video.short_url()}")
    print("---")
```

## Domain-Specific Examples

The package includes example scripts for searching videos in specific domains:

- Computer Graphics (`examples/computer_graphics.py`)
- Computer Music (`examples/computer_music.py`)
- Full-Stack Development (`examples/fullstack_development.py`)

Each example demonstrates searching for curated lists of topics in their respective domains.

## API Reference

### VideoResult Class

```python
@dataclass
class VideoResult:
    video_id: str      # YouTube video ID
    title: str         # Video title
    channel: str       # Channel name (optional)
    duration: str      # Video duration (optional)
    
    def url() -> str       # Returns full YouTube URL
    def short_url() -> str # Returns shortened youtu.be URL
```

### Main Function

```python
def search_youtube(
    query: str,
    max_results: int = 10,
    api_key: Optional[str] = None
) -> List[VideoResult]
```

Parameters:
- `query`: Search terms
- `max_results`: Maximum number of results to return (default: 10)
- `api_key`: YouTube Data API key (optional, falls back to HTML scraping if None)

## Dependencies

- requests >= 2.0.0
- pytest >= 7.0 (for testing)
- setuptools >= 50.0.0 (for installation)

## Important Notes

1. The HTML fallback method is provided as a convenience and:
   - May be less reliable than the API method
   - Could break with YouTube UI changes
   - Should not be used for high-volume scraping
   - May violate YouTube's Terms of Service if used at scale

2. For production use, it's strongly recommended to:
   - Use the YouTube Data API with a valid API key
   - Respect YouTube's API quotas and terms of service
   - Handle rate limiting appropriately

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
