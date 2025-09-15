"""Example usage of PeerTube API wrappers."""

from peertube import (
    PeerTubeClient,
    PeerTubeConfig,
    get_user_info,
    get_video,
    list_videos,
    login,
    logout,
    register_user,
    search_videos,
)

# Note: This example requires the full dependencies to be installed
# For now, this serves as documentation of the intended API


def example_authentication() -> None:
    """Example of using authentication features."""
    # Login to get access token
    try:
        token = login("https://your-peertube-instance.com", "username", "password")
        print(f"Login successful! Token: {token.access_token}")

        # Get current user info
        user = get_user_info("https://your-peertube-instance.com", token.access_token)
        print(f"Logged in as: {user.username} (ID: {user.id})")

        # Logout
        logout("https://your-peertube-instance.com", token.access_token)
        print("Logged out successfully")

    except Exception as e:
        print(f"Authentication error: {e}")


def example_video_operations() -> None:
    """Example of using video operations."""
    base_url = "https://your-peertube-instance.com"

    try:
        # List recent videos
        videos = list_videos(base_url, count=5)
        print(f"Found {videos.get('total', 0)} videos")

        # Get specific video details
        if videos.get("data"):
            first_video = videos["data"][0]
            video_id = first_video["id"]

            video_details = get_video(base_url, video_id)
            print(f"Video: {video_details.get('name', 'Unknown')}")

        # Search for videos
        search_results = search_videos(base_url, "tutorial", count=3)
        print(f"Search found {search_results.get('total', 0)} tutorial videos")

    except Exception as e:
        print(f"Video operations error: {e}")


def example_client_usage() -> None:
    """Example of using the PeerTube client directly."""
    # Configure client
    config = PeerTubeConfig(
        base_url="https://your-peertube-instance.com/",
        token="your-access-token",
        timeout=30,
    )

    # Use client for API calls
    try:
        with PeerTubeClient(config) as client:
            # Get current user
            user_data = client.get("/users/me")
            print(f"User data: {user_data}")

            # Get server config (public endpoint)
            config_data = client.get("/config")
            print(f"Server config: {config_data}")

            # Check if generated client is available
            if client.generated_client:
                print("Generated OpenAPI client is available!")
            else:
                print("Using manual HTTP client")

    except Exception as e:
        print(f"Client error: {e}")


def example_registration() -> None:
    """Example of user registration."""
    try:
        result = register_user(
            base_url="https://your-peertube-instance.com/",
            username="newuser",
            password="securepassword",
            email="user@example.com",
            display_name="New User",
        )
        print(f"Registration successful: {result}")

    except Exception as e:
        print(f"Registration error: {e}")


if __name__ == "__main__":
    print("PeerTube API Wrappers Examples")
    print("=" * 40)

    print("\n1. Authentication Example:")
    example_authentication()

    print("\n2. Video Operations Example:")
    example_video_operations()

    print("\n3. Client Usage Example:")
    example_client_usage()

    print("\n4. Registration Example:")
    example_registration()

    print(
        "\nNote: These examples require proper PeerTube instance URLs and credentials.",
    )
