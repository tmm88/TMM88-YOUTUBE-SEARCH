from youtube_search import search_youtube

# List of computer graphics related topics and technologies
CG_TAGS = [
    "Unreal Engine 5",
    "Unity 3D",
    "Blender 3D",
    "Maya 3D",
    "3DS Max",
    "Computer Graphics Programming",
    "OpenGL Tutorial",
    "DirectX Development",
    "Vulkan Graphics",
    "Game Engine Development",
    "3D Modeling",
    "Texture Creation",
    "Shader Programming",
    "Ray Tracing",
    "Computer Animation",
    "VFX Creation",
    "Procedural Generation",
    "Character Modeling",
    "Digital Sculpting",
    "Motion Graphics"
]

def search_cg_topics(max_results_per_tag=3):
    """Search for videos for each computer graphics topic."""
    print("Searching for Computer Graphics Topics...")
    print("-" * 50)
    
    for tag in CG_TAGS:
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
            print(f"Error searching for {tag}: {str(e)}")
        
if __name__ == "__main__":
    search_cg_topics()
    