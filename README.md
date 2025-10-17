# youtube_search

Small illustrative Python package to search YouTube using the Data API or a fragile HTML fallback.

Usage example:

```py
from youtube_search import search_youtube

results = search_youtube('python tutorial', max_results=3, api_key=None)
for r in results:
    print(r.video_id, r.title)
```

Notes:
- The HTML fallback is brittle and may violate YouTube TOS for scraping at scale.
- Use an API key when possible.
