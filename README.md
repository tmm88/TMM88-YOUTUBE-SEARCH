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

Graphics & Motion:
- Computer Graphics (`examples/computer_graphics.py`)
- Abstract Motion Graphics (`examples/abstract_mograph.py`)
- Cinema 4D Advanced (`examples/cinema4d_advanced.py`)
- 3D Modeling Advanced (`examples/3d_modeling_advanced.py`)
- Rendering & Visualization (`examples/rendering_visualization.py`)

Game Engines:
- Unreal Engine (`examples/unreal_engine.py`)
- Unity3D (`examples/unity3d.py`)
- Godot (`examples/godot.py`)
- CryEngine (`examples/cryengine.py`)
- FMOD Integration (`examples/fmod_integration.py`)
- Game Maker Studio (`examples/gamemaker.py`)
- Mobile Engines (`examples/mobile_engines.py`)
- Web Game Engines (`examples/web_engines.py`)

Audio & Music:
- Computer Music (`examples/computer_music.py`)
- EDM Production (`examples/edm_production.py`)
- Audio Production Advanced (`examples/audio_production_advanced.py`)

Audio Programming & Interactive Systems:
- Game Audio & Middleware (`examples/audio_middleware.py`)
- Max/MSP Advanced (`examples/maxmsp_advanced.py`)
- Pure Data Advanced (`examples/puredata_advanced.py`)
- SuperCollider & Live Coding (`examples/supercollider_advanced.py`)

Development:
- Full-Stack Development (`examples/fullstack_development.py`)
- Modern Frontend (`examples/frontend_masters.py`)
- Backend Architecture (`examples/backend_advanced.py`)
- DevOps & Cloud (`examples/devops_cloud.py`)
- System Design (`examples/system_design.py`)

Each example demonstrates searching for curated lists of topics in their respective domains and includes an interactive browser feature.

### Running Examples

Basic usage:
```bash
python examples/computer_graphics.py
python examples/edm_production.py
python examples/cinema4d_advanced.py
# etc...
```

### Command Line Options

All example scripts support the following command-line options:

```bash
# Show help and available options
python examples/computer_graphics.py --help
```

Output:
```
Usage: computer_graphics.py [OPTIONS]

Options:
  --open    Open 3 random videos from search results in your default browser
  --help    Show this help message

Examples:
  python computer_graphics.py         # Run normal search
  python computer_graphics.py --open  # Search and open random videos
```

### Browser Integration

To automatically open 3 random videos in your default browser, use the `--open` flag:
```bash
python examples/computer_graphics.py --open
```

The browser-opening feature:
- Works cross-platform (Windows, macOS, Linux)
- Opens 3 random videos from your search results
- Uses the appropriate default browser for your OS
- Provides fallback URLs if browser launching fails

This works with all example scripts:
```bash
python examples/edm_production.py --open      # EDM production tutorials
python examples/cinema4d_advanced.py --open    # Cinema 4D tutorials
python examples/computer_music.py --open       # Music production tutorials
# etc...
```

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
