
# API Client for making REST API calls


import requests
import json
import random

class APIClient:
    def __init__(self, base_url): 
        # Initialize API client with base URL   
         
        self.base_url = base_url
        
    def get(self, endpoint, params=None):
        # Make a GET request to the API
        
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, params=params)
            return response
        except Exception as e:
            raise Exception(f"Error making GET request: {e}")
    
    def post(self, endpoint, data=None, headers=None):
        # Make a POST request to the API
        
        if headers is None:
            headers = {'Content-Type': 'application/json'}
        
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(
                url,
                data=json.dumps(data) if data else None,
                headers=headers
            )
            return response
        except Exception as e:
            raise Exception(f"Error making POST request: {e}")
    
    def get_random_user(self):
        
        # Get a random user from the API
       
        try:
            response = self.get("users")
            if response.status_code != 200:
                raise Exception(f"Failed to get users. Status code: {response.status_code}")
                
            users = response.json()
            if not users:
                raise Exception("No users returned from API")
                
            return random.choice(users)
        except Exception as e:
            raise Exception(f"Error getting random user: {e}")
    
    def get_user_posts(self, user_id):
        # Get posts for a specific user
        
        try:
            response = self.get(f"users/{user_id}/posts")
            if response.status_code != 200:
                raise Exception(f"Failed to get user posts. Status code: {response.status_code}")
                
            return response.json()
        except Exception as e:
            raise Exception(f"Error getting user posts: {e}")
    
    def create_post(self, user_id, title, body):
        # Create a new post
        
        data = {
            'userId': user_id,
            'title': title,
            'body': body
        }
        
        try:
            return self.post("posts", data)
        except Exception as e:
            raise Exception(f"Error creating post: {e}")