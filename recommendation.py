import requests

API_KEY = "Your YouTube API key"  # Your YouTube API key
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"

def get_youtube_recommendations(query):
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": 5,
        "key": API_KEY
    }
    
    response = requests.get(YOUTUBE_SEARCH_URL, params=params)
    
    if response.status_code != 200:
        return [{"error": "YouTube API request failed"}]

    data = response.json()
    recommendations = []
    
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        recommendations.append({"title": title, "id": video_id})
    
    return recommendations
