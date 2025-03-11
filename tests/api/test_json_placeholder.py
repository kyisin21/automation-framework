
# Test cases for JSONPlaceholder API


import pytest
import random
from src.utils.api_client import APIClient
from src.config.config import Config

class TestJSONPlaceholder:
    @pytest.fixture
    def api_client(self):
        
        # Set up API client
        
        return APIClient(Config.JSON_PLACEHOLDER_API)
    
    def test_get_random_user_email(self, api_client):
        """
        Test Scenario:
        1. Get a random user
        2. Print their email address
        
        Returns:
            user_id: The random user ID for use in other tests
        """
        print("\n----- Testing: Get Random User Email -----")
        
        # Get a random user
        random_user = api_client.get_random_user()
        
        # Extract user information
        user_id = random_user['id']
        user_name = random_user['name']
        user_email = random_user['email']
        
        # Print email to console as required
        print(f"Random User ID: {user_id}")
        print(f"User Name: {user_name}")
        print(f"User Email: {user_email}")
        
        # Simple validation
        assert '@' in user_email, "Email address should contain @ symbol"
        assert '.' in user_email, "Email address should contain domain"
        
        # Return user_id for use in subsequent tests
        return user_id
    
    def test_verify_user_posts(self, api_client):
        """
        Test Scenario:
        1. Get a random user ID
        2. Get this user's posts
        3. Verify post IDs are valid (integers between 1 and 100)
        """
        print("\n----- Testing: Verify User Posts -----")
        
        # Step 1: Get a random user ID
        user_id = self.test_get_random_user_email(api_client)
        
        # Step 2: Get user's posts
        print(f"Getting posts for User ID: {user_id}")
        posts = api_client.get_user_posts(user_id)
        
        # Verify we got some posts
        assert posts, f"No posts found for User ID: {user_id}"
        print(f"Found {len(posts)} posts for User ID: {user_id}")
        
        # Step 3: Verify each post ID
        valid_posts = True
        for i, post in enumerate(posts, 1):
            post_id = post['id']
            
            # Verify post ID is an integer between 1 and 100
            is_valid = isinstance(post_id, int) and 1 <= post_id <= 100
            if not is_valid:
                valid_posts = False
                print(f"Invalid Post ID: {post_id} (not an integer between 1-100)")
            
        assert valid_posts, "One or more posts had invalid IDs"
        print("All post IDs are valid integers between 1-100")
        
        return user_id
    
    def test_create_post(self, api_client):
        """
        Test Scenario:
        1. Get a random user ID
        2. Create a post with this user ID
        3. Verify correct response is returned
        """
        print("\n----- Testing: Create Post -----")
        
        # Step 1: Get a random user ID
        user_id = self.test_verify_user_posts(api_client)
        
        # Step 2: Create a post
        title = "Test Post Title"
        body = "This is a test post body created during API testing"
        
        print(f"Creating post for User ID: {user_id}")
        print(f"Title: {title}")
        print(f"Body: {body}")
        
        response = api_client.create_post(user_id, title, body)
        
        # Step 3: Verify response (JSONPlaceholder returns 201 for create operations)
        assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
        print(f"Response status code: {response.status_code} (PASSED)")
        
        created_post = response.json()
        
        # Verify response contains expected data
        assert created_post['userId'] == user_id, "Created post has incorrect user ID"
        assert created_post['title'] == title, "Created post has incorrect title"
        assert created_post['body'] == body, "Created post has incorrect body"
        assert 'id' in created_post, "Created post should have an ID assigned"
        
        print(f"Created post with ID: {created_post['id']}")
        print("Post creation successful with all data validated")