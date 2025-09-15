# PeerTube Python API Wrappers

Python API wrappers for PeerTube using modern HTTP client and type-safe implementations.

## Overview

This package provides Python wrappers for the PeerTube API, organized thematically based on the OpenAPI specification. It uses `httpx` for HTTP operations and `pydantic` for data validation and type safety.

## Installation

```bash
pip install peertube
```

## Quick Start

### Authentication

```python
from peertube import login, get_user_info

# Login to get access token
token = login("https://your-peertube-instance.com", "username", "password")

# Get current user information
user = get_user_info("https://your-peertube-instance.com", token.access_token)
print(f"Logged in as: {user.username}")
```

### Video Operations

```python
from peertube import get_video, list_videos, search_videos

# Get specific video details
video = get_video("https://your-peertube-instance.com", "video-uuid")
print(f"Video: {video['name']}")

# List recent videos
videos = list_videos("https://your-peertube-instance.com", count=10)
print(f"Found {videos['total']} videos")

# Search for videos  
results = search_videos("https://your-peertube-instance.com", "tutorial")
for video in results['data']:
    print(f"- {video['name']}")
```

### OpenAPI Client Integration

The package integrates with auto-generated OpenAPI clients for type-safe operations:

```python
from peertube import PeerTubeClient, PeerTubeConfig

config = PeerTubeConfig(
    base_url="https://your-peertube-instance.com",
    token="your-access-token"
)

with PeerTubeClient(config) as client:
    # Manual HTTP client (always available)
    response = client.get("/users/me")
    
    # Generated OpenAPI client (when available)
    if client.generated_client:
        # Type-safe operations with auto-completion
        pass
```

## API Coverage

The package is organized into the following modules:

- **Auth** (`peertube.auth`): Login, logout, registration, token management
- **Videos** (`peertube.videos`): Core video operations (get, list)
- **Search** (`peertube.search`): Video search functionality
- **Accounts** (`peertube.accounts`): User and account management (planned)
- **Moderation** (`peertube.moderation`): Content moderation (planned)
- **Instance** (`peertube.instance`): Instance administration (planned)

## Development Status

🚧 **This package is currently under development.** 

Currently implemented:
- ✅ Basic authentication (login, logout, user info)
- ✅ User registration functionality
- ✅ Core client architecture with OpenAPI integration
- ✅ Basic video operations (get video, list videos)
- ✅ Video search functionality
- ✅ Exception handling and type-safe models using Pydantic

Planned:
- 🔄 Video upload and management
- 🔄 Video playlist operations
- 🔄 Complete account management
- 🔄 Moderation tools
- 🔄 Instance administration

## Requirements

- Python 3.10+
- httpx >= 0.27.0
- pydantic >= 2.0.0
- typing-extensions >= 4.0.0

### Development Dependencies

- openapi-python-client >= 0.21.0 (for generating type-safe clients)

## OpenAPI Client Generation

This package supports integration with auto-generated OpenAPI clients for enhanced type safety:

```bash
# Install development dependencies
pip install openapi-python-client

# Generate client from OpenAPI specification
python scripts/generate_openapi_client.py
```

The generated client provides:
- Type-safe method signatures
- Auto-completion in IDEs
- Automatic request/response validation
- Comprehensive coverage of all API endpoints

## Contributing

This project follows modern Python development practices:

- Type hints for all functions
- Pydantic models for data validation
- Comprehensive error handling
- 100-character line length limit
- pytest for testing

## License

MIT License
