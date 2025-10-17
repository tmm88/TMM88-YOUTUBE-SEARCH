from youtube_search import search_youtube
import webbrowser
import random
import platform
import sys
import os
import json
import argparse

def list_available_categories():
    """List all available categories based on JSON files in tags directory."""
    tags_dir = os.path.join(os.path.dirname(__file__), 'tags')
    categories = [f.replace('.json', '') for f in os.listdir(tags_dir) if f.endswith('.json')]
    return categories

def load_tags(category_name):
    """Load tags from the corresponding JSON file."""
    try:
        json_path = os.path.join(os.path.dirname(__file__), 'tags', f'{category_name}.json')
        with open(json_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: Tags file for {category_name} not found.")
        available = list_available_categories()
        print(f"Available categories: {', '.join(available)}")
        sys.exit(1)

def open_in_browser(url):
    """Open URL in the default browser based on the operating system."""
    try:
        if platform.system() == 'Windows':
            os.startfile(url)
        elif platform.system() == 'Darwin':  # macOS
            webbrowser.get('safari').open(url)
        else:  # Linux and others
            webbrowser.get('firefox').open(url)
    except Exception as e:
        print(f"Failed to open browser: {e}")
        print(f"URL to open manually: {url}")

def search_topics(category_name, subcategory=None, open_random=False):
    """Search YouTube for topics in specified category and subcategory."""
    data = load_tags(category_name)
    print(f"Searching for {data['name']} Tutorials...")
    print("-" * 60)
    
    all_videos = []
    subcategories = [subcategory] if subcategory else data['tags'].keys()
    
    for subcat in subcategories:
        if subcat not in data['tags']:
            print(f"Error: Subcategory '{subcat}' not found.")
            print(f"Available subcategories: {', '.join(data['tags'].keys())}")
            sys.exit(1)
            
        print(f"\nSubcategory: {subcat}")
        for topic in data['tags'][subcat]:
            print(f"\nTopic: {topic}")
            try:
                results = search_youtube(topic, max_results=2)
                for video in results:
                    print(f"\nTitle: {video.title}")
                    print(f"Channel: {video.channel}")
                    print(f"Watch: {video.url()}")
                    print(f"Short URL: {video.short_url()}")
                    print("-" * 30)
                    all_videos.append(video)
            except Exception as e:
                print(f"Error searching for {topic}: {e}")
            print()

    if open_random and all_videos:
        print("\nOpening 3 random videos in your browser...")
        selected_videos = random.sample(all_videos, min(3, len(all_videos)))
        for video in selected_videos:
            print(f"Opening: {video.title}")
            open_in_browser(video.url())

def main():
    parser = argparse.ArgumentParser(description='Search for tutorials on YouTube by category')
    parser.add_argument('category', help='Category name (e.g., development, computer_graphics, audio_production)')
    parser.add_argument('-s', '--subcategory', help='Specific subcategory to search')
    parser.add_argument('--open', action='store_true', help='Open 3 random videos in browser')
    parser.add_argument('--list', action='store_true', help='List available categories and subcategories')
    
    args = parser.parse_args()
    
    if args.list:
        print("Available categories:")
        for category in list_available_categories():
            data = load_tags(category)
            print(f"\n{data['name']} ({category}):")
            print(f"Subcategories: {', '.join(data['tags'].keys())}")
        sys.exit(0)
    
    search_topics(args.category, args.subcategory, args.open)

if __name__ == "__main__":
    main()