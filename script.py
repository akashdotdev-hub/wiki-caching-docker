import os
import redis
import requests
import time

# Connect to the Redis container
# Make sure this host name matches your service name in docker-compose.yml
redis_password = os.environ.get('REDIS_PASSWORD', None)

cache = redis.Redis(
    host='redis', 
    port=6379, 
    password=redis_password,  # <-- THIS IS THE MAGIC LINE
    decode_responses=True
)
def get_wikipedia_summary(page_title):
    # 1. Try to get data from the cache first
    try:
        cached_data = cache.get(page_title)
        if cached_data:
            print(f"🚀 CACHE HIT! Fetching '{page_title}' from Redis...")
            return cached_data
    except Exception as e:
        print(f"⚠️ Redis connection error: {e}")

    # 2. If not in cache, fetch from Wikipedia
    print(f"🐢 CACHE MISS. Fetching '{page_title}' from Wikipedia API...")
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title}"
    
    # Adding a header helps Wikipedia know you aren't a 'bot'
    headers = {'User-Agent': 'MyCachingPracticeApp/1.0 (contact: your@email.com)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        summary = response.json().get('extract', 'Topic not found.')
        # 3. Save to cache with a TTL of 60 seconds
        cache.setex(page_title, 60, summary)
        return summary
    else:
        return f"❌ Error: Wikipedia returned status {response.status_code}"

# Testing it out
topic = "Cloud_computing"
print("\n--- Round 1 ---")
print(get_wikipedia_summary(topic)[:150] + "...")

time.sleep(2) # Just a tiny pause

print("\n--- Round 2 (Immediate) ---")
print(get_wikipedia_summary(topic)[:150] + "...")
