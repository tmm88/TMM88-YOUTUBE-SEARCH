from youtube_search import search_youtube

# Topics/tags for full-stack development
FS_TAGS = [
    "Full stack development tutorial",
    "React tutorial for beginners",
    "Node.js REST API tutorial",
    "Django full stack tutorial",
    "Flask REST API tutorial",
    "Frontend development with React",
    "Backend architecture best practices",
    "Database design tutorial",
    "PostgreSQL tutorial",
    "Docker for developers",
    "Kubernetes basics",
    "TypeScript tutorial",
    "GraphQL tutorial",
    "Authentication and OAuth",
    "CI/CD pipeline tutorial",
    "Microservices architecture",
    "Web performance optimization",
    "Serverless functions tutorial",
    "Next.js fullstack tutorial",
    "Testing and TDD in web development"
]


def search_fs_topics(max_results_per_tag=3):
    print("Searching for Full-Stack Development Topics...")
    print("-" * 50)
    for tag in FS_TAGS:
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
    search_fs_topics()