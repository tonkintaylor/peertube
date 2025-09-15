# PeerTube API Client Usage Guide

This guide shows how to use the PeerTube API client with the integrated OpenAPI-generated client.

## Quick Start

### Basic Setup

```python
from peertube import PeerTubeConfig, PeerTubeClient

# Create configuration
config = PeerTubeConfig(base_url="https://your-peertube-instance.com")

# Create client
with PeerTubeClient(config) as client:
    # Client is ready to use
    print(f"Generated client available: {client.generated_client is not None}")
```

### Authenticated Setup

```python
from peertube import PeerTubeConfig, PeerTubeClient, login

# Login to get token
token_response = login("https://your-instance.com", "username", "password")
access_token = token_response["access_token"]

# Create authenticated configuration
config = PeerTubeConfig(
    base_url="https://your-instance.com",
    token=access_token
)

# Create authenticated client
with PeerTubeClient(config) as client:
    # Client has access to protected endpoints
    print(f"Authenticated: {hasattr(client.generated_client, 'token')}")
```

## Usage Patterns

### 1. Convenience Functions (Recommended for Common Operations)

```python
from peertube import get_video, list_videos, search_videos

# Get a specific video
video = get_video("https://instance.com", "video-uuid")

# List recent videos
videos = list_videos("https://instance.com", count=10)

# Search for videos
results = search_videos("https://instance.com", "tutorial")
```

### 2. Direct Generated Client Usage (For Advanced Operations)

```python
from peertube import PeerTubeClient, PeerTubeConfig

config = PeerTubeConfig(base_url="https://instance.com", token="your-token")

with PeerTubeClient(config) as client:
    # Access the generated client directly
    generated = client.generated_client
    
    # Use type-safe API calls
    # Note: Actual usage depends on specific endpoints you need
    # Refer to the generated client documentation
```

### 3. Available API Modules

The generated client provides access to 49 API module groups covering 200+ endpoints:

- `video` - Video operations (CRUD, upload, transcoding)
- `session` - Authentication and session management  
- `search` - Search functionality
- `accounts` - Account management
- `users` - User operations
- `config` - Instance configuration
- `abuses` - Abuse reporting and moderation
- `register` - User registration
- `live_videos` - Live streaming
- `video_playlists` - Playlist management
- `video_comments` - Comment operations
- And many more...

## Error Handling

```python
from peertube import PeerTubeError, AuthenticationError, NotFoundError

try:
    video = get_video("https://instance.com", "invalid-uuid")
except NotFoundError:
    print("Video not found")
except AuthenticationError:
    print("Authentication required")
except PeerTubeError as e:
    print(f"PeerTube API error: {e}")
```

## Configuration Options

```python
from peertube import PeerTubeConfig

config = PeerTubeConfig(
    base_url="https://your-instance.com",
    token="optional-auth-token",
    verify_ssl=True,  # Set to False for testing only
    timeout=30        # Request timeout in seconds
)
```

## Regenerating the Client

When the PeerTube API changes, regenerate the client:

```bash
python scripts/regenerate_openapi_client.py
```

This script:
1. Fixes known OpenAPI specification issues
2. Generates a new client from the latest specification
3. Integrates it with the existing wrapper architecture
4. Maintains backward compatibility

## Migration from Manual Wrappers

All existing code continues to work unchanged. The generated client provides additional functionality:

**Before (still works):**
```python
from peertube import get_video
video = get_video("https://instance.com", "uuid")
```

**Now (additional options):**
```python
# Option 1: Continue using convenience functions
from peertube import get_video
video = get_video("https://instance.com", "uuid")

# Option 2: Use generated client for type safety
from peertube import PeerTubeClient, PeerTubeConfig
config = PeerTubeConfig(base_url="https://instance.com")
with PeerTubeClient(config) as client:
    # Use client.generated_client for type-safe API access
    pass
```

## Benefits of the Integration

- **Backward Compatibility**: All existing code continues to work
- **Type Safety**: Generated client provides full type annotations  
- **Complete Coverage**: Access to all 200+ PeerTube API endpoints
- **Maintainability**: Easy regeneration when API changes
- **Flexibility**: Choose between convenience functions or direct API access