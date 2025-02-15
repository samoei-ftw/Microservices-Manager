# Set up a customer locally to perform end-to-end transactions through cybs
import requests
def get_data(url):
    """Perform a GET request and return JSON response."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed GET request to {url} with status code {response.status_code}")
        return None


def post_data(url, data):
    """Perform a POST request with given data."""
    response = requests.post(url, json=data)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        print(f"Failed POST request to {url} with status code {response.status_code}")
        return None


def main():
    # Step 1: Check if merchant exists
    url1 = "https://jsonplaceholder.typicode.com/posts/1"
    data1 = get_data(url1)

    if data1:
        user_id = data1.get("userId")
        print(f"User ID from first request: {user_id}")

        # Step 2: Conditional GET request based on first response
        url2 = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        user_data = get_data(url2)

        if user_data:
            print(f"User Name: {user_data.get('name')}, Email: {user_data.get('email')}")

            # Step 3: POST request using obtained data
            post_url = "https://jsonplaceholder.typicode.com/posts"
            new_post_data = {
                "title": "Automated Post",
                "body": f"Created for user {user_data.get('name')}",
                "userId": user_id
            }
            post_response = post_data(post_url, new_post_data)

            if post_response:
                print(f"Successfully created post: {post_response}")


if __name__ == "__main__":
    main()
