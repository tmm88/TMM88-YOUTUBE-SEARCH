from youtube_search import search_youtube

# Topics/tags for computer music and music production
MUSIC_TAGS = [
    "Music production tutorial",
    "Ableton Live beginner tutorial",
    "FL Studio beat making",
    "Logic Pro X tutorial",
    "Sound design tutorial",
    "Synthesis basics",
    "Modular synthesis",
    "Audio engineering",
    "Mixing and mastering",
    "Music theory for producers",
    "Electronic music production",
    "MIDI production",
    "Sampling techniques",
    "DAW workflow tips",
    "Home studio setup",
    "Game audio",
    "Film scoring tutorials",
    "Sound design for games",
    "Ambient music production",
    "Algorithmic composition"
]


def search_music_topics(max_results_per_tag=3):
    print("Searching for Computer Music Topics...")
    print("-" * 50)
    for tag in MUSIC_TAGS:
        print(f"\nResults for: {tag}")
        print("-" * 30)
        try:
            results = search_youtube(tag, max_results=max_results_per_tag, api_key=None)
            for r in results:
                print(f"Title: {r.title}")
                print(f"Video ID: {r.video_id}")
                print(f"Channel: {r.channel if r.channel else 'N/A'}")
                print(f"URL: {r.url()}")
                print(f"Short URL: {r.short_url()}")
                print("-" * 20)
        except Exception as e:
            print(f"Error searching for {tag}: {e}")


if __name__ == '__main__':
    search_music_topics()