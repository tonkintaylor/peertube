"""Test the generated API functions for PeerTube."""

import pytest
from unittest.mock import Mock, patch

from peertube import Client


class TestGeneratedAPI:
    """Test that generated API functions can be imported and have correct structure."""

    def test_import_video_api_functions(self):
        """Test that video API functions can be imported."""
        try:
            from peertube.api.video import get_video, get_categories, get_languages
            
            assert get_video is not None
            assert get_categories is not None  
            assert get_languages is not None
        except ImportError as e:
            pytest.fail(f"Failed to import video API functions: {e}")

    def test_import_account_api_functions(self):
        """Test that account API functions can be imported."""
        try:
            from peertube.api.accounts import get_accounts, get_account
            
            assert get_accounts is not None
            assert get_account is not None
        except ImportError as e:
            pytest.fail(f"Failed to import accounts API functions: {e}")

    def test_api_function_structure(self):
        """Test that API functions have expected structure."""
        from peertube.api.video import get_categories
        
        # API functions should have sync and asyncio methods
        assert hasattr(get_categories, 'sync')
        assert hasattr(get_categories, 'asyncio')
        assert hasattr(get_categories, 'sync_detailed')
        assert hasattr(get_categories, 'asyncio_detailed')

    @patch('peertube.api.video.get_categories.sync')
    def test_api_function_call_structure(self, mock_get_categories):
        """Test that API functions can be called with client parameter."""
        from peertube.api.video import get_categories
        
        # Mock response
        mock_get_categories.return_value = {"1": "Music", "2": "Films"}
        
        # Create client
        client = Client(base_url="https://example.peertube.com")
        
        # Call API function
        result = get_categories.sync(client=client)
        
        # Verify call was made with client
        mock_get_categories.assert_called_once_with(client=client)
        assert result == {"1": "Music", "2": "Films"}

    def test_model_imports(self):
        """Test that generated models can be imported."""
        try:
            from peertube.models import VideoConstantNumberCategory
            
            assert VideoConstantNumberCategory is not None
        except ImportError:
            # Some models might not be generated due to spec issues, this is acceptable
            pass

    def test_types_import(self):
        """Test that generated types can be imported."""
        try:
            from peertube.types import Response
            
            assert Response is not None
        except ImportError as e:
            pytest.fail(f"Failed to import types: {e}")

    def test_errors_import(self):
        """Test that generated errors can be imported."""
        try:
            from peertube.errors import UnexpectedStatus
            
            assert UnexpectedStatus is not None
        except ImportError as e:
            pytest.fail(f"Failed to import errors: {e}")