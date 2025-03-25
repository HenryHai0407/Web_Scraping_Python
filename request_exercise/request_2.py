import requests
from datetime import datetime

api_base_url = "http://example.com/api"
api_key = "your_api_key"
HEADERS = {"Authorization": f"Bearer {api_key}","Content-Type": "application/json"}

def get_all_posts():
    response = requests.get(f"{api_base_url}/posts",headers = HEADERS)
    response.raise_for_status()
    return response.json()

def delete_posts(post_id):
    response = requests.delete(f"{api_base_url}/posts/{post_id}", headers=HEADERS)
    response.raise_for_status
    print(f"Delete post with ID:{post_id}")

def delete_five_oldest_posts(excluded_updated_posts=True):
    posts = get_all_posts()

    if excluded_updated_posts:
        recent_threshold = datetime.now().timestamp() - 300
        posts = [post for post in posts if "update_at" not in post or post['updated_at'] < recent_threshold]
    # Above loop running for excluding the update posts
    sorted_p = sorted(posts, lambda x: x['created_at'])

    oldest_five = sorted_p[:5]

    # Delete each of the 5 oldest posts:
    for post in oldest_five:
        delete_posts(post['id'])

if __name__ == "__main__":
    try:
        delete_five_oldest_posts()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
