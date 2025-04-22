import asyncio
from YouTubeMusic.YtSearch import Search

async def search_youtube(query):
    print(f"Searching YouTube for: {query}")
    results = await Search(query, limit=3)  # Fetch top 3 results

    if not results:
        print("No results found.")
        return None, None, None

    item = results[0]
    song_title = item["title"]
    song_url = item["url"]
    song_thumbnail = item["thumbnail"]
    return song_title, song_url, song_thumbnail
  
