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

### Using the Client

```python
from peertube import PeerTubeClient, PeerTubeConfig

# Configure client
config = PeerTubeConfig(
    base_url="https://your-peertube-instance.com",
    token="your-access-token"
)

# Use client for API calls
with PeerTubeClient(config) as client:
    response = client.get("/users/me")
    print(response)
```

## API Coverage

The package is organized into the following modules:

- **Auth** (`peertube.auth`): Login, logout, registration, token management
- **Videos** (`peertube.videos`): Video operations (planned)
- **Search** (`peertube.search`): Search functionality (planned)
- **Accounts** (`peertube.accounts`): User and account management (planned)
- **Moderation** (`peertube.moderation`): Content moderation (planned)
- **Instance** (`peertube.instance`): Instance administration (planned)

## Development Status

🚧 **This package is currently under development.** 

Currently implemented:
- ✅ Basic authentication (login, logout, user info)
- ✅ User registration functionality
- ✅ Core client architecture
- ✅ Exception handling
- ✅ Type-safe models using Pydantic

Planned:
- 🔄 Video management operations
- 🔄 Search functionality
- 🔄 Complete account management
- 🔄 Moderation tools
- 🔄 Instance administration

## Requirements

- Python 3.10+
- httpx >= 0.27.0
- pydantic >= 2.0.0
- typing-extensions >= 4.0.0

## Contributing

This project follows modern Python development practices:

- Type hints for all functions
- Pydantic models for data validation
- Comprehensive error handling
- 100-character line length limit
- pytest for testing

## License

MIT License
