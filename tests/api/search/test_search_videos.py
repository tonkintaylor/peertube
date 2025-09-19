"""Test search_videos function with both string and enum sort parameters."""

from unittest.mock import patch

import pytest

from peertube import Client
from peertube.api.search import search_videos
from peertube.models.search_videos_sort import SearchVideosSort


class TestSearchVideosSort:
    """Test that search_videos accepts both string and enum for sort parameter."""

    def test_search_videos_with_enum_sort(self):
        """Test that search_videos works with SearchVideosSort enum."""
        client = Client(base_url="https://example.peertube.com")
        
        with patch("peertube.api.search.search_videos.sync_detailed") as mock_sync_detailed:
            # Mock successful response
            mock_sync_detailed.return_value.parsed = {"videos": []}
            
            # Call with enum sort parameter
            result = search_videos.sync(
                client=client,
                search="test",
                sort=SearchVideosSort.VALUE_3  # "-publishedAt"
            )
            
            # Verify the function was called
            mock_sync_detailed.assert_called_once()
            call_kwargs = mock_sync_detailed.call_args.kwargs
            assert call_kwargs["sort"] == SearchVideosSort.VALUE_3

    def test_search_videos_with_string_sort(self):
        """Test that search_videos works with string sort parameter."""
        client = Client(base_url="https://example.peertube.com")
        
        with patch("peertube.api.search.search_videos.sync_detailed") as mock_sync_detailed:
            # Mock successful response
            mock_sync_detailed.return_value.parsed = {"videos": []}
            
            # Call with string sort parameter
            result = search_videos.sync(
                client=client,
                search="test",
                sort="-publishedAt"
            )
            
            # Verify the function was called
            mock_sync_detailed.assert_called_once()
            call_kwargs = mock_sync_detailed.call_args.kwargs
            assert call_kwargs["sort"] == "-publishedAt"

    def test_get_kwargs_with_enum_sort(self):
        """Test that _get_kwargs correctly handles enum sort parameter."""
        from peertube.api.search.search_videos import _get_kwargs
        
        kwargs = _get_kwargs(
            search="test",
            sort=SearchVideosSort.VALUE_3
        )
        
        # The enum's value should be extracted
        assert kwargs["params"]["sort"] == "-publishedAt"

    def test_get_kwargs_with_string_sort(self):
        """Test that _get_kwargs correctly handles string sort parameter."""
        from peertube.api.search.search_videos import _get_kwargs
        
        kwargs = _get_kwargs(
            search="test",
            sort="-publishedAt"
        )
        
        # The string should be used directly
        assert kwargs["params"]["sort"] == "-publishedAt"