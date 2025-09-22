"""Tests for peertube.client module"""

import httpx
import pytest

from peertube.client import AuthenticatedClient, Client


@pytest.mark.parametrize(
    "headers",
    [
        {"User-Agent": "test-agent"},
        {"Authorization": "Bearer token"},
        {"X-Custom": "value"},
    ],
    ids=["user_agent", "bearer_auth", "custom_header"],
)
def test_client_with_headers_returns_new_instance(client, headers):
    """Test that Client.with_headers() returns a new Client instance"""
    result = client.with_headers(headers)
    assert isinstance(result, Client)


@pytest.mark.parametrize(
    "cookies",
    [
        {"session": "abc123"},
        {"prefs": "dark_mode"},
        {"session": "xyz", "theme": "light"},
    ],
    ids=["session_cookie", "prefs_cookie", "multiple_cookies"],
)
def test_client_with_cookies_returns_new_instance(client, cookies):
    """Test that Client.with_cookies() returns a new Client instance"""
    result = client.with_cookies(cookies)
    assert isinstance(result, Client)


@pytest.mark.parametrize(
    "timeout",
    [
        httpx.Timeout(5.0),
        httpx.Timeout(30.0),
        httpx.Timeout(10.0, read=20.0),
    ],
    ids=["short_timeout", "long_timeout", "custom_read_timeout"],
)
def test_client_with_timeout_returns_new_instance(client, timeout):
    """Test that Client.with_timeout() returns a new Client instance"""
    result = client.with_timeout(timeout)
    assert isinstance(result, Client)


def test_client_set_httpx_client_returns_new_instance(client, mock_httpx_client):
    """Test that Client.set_httpx_client() returns a new Client instance"""
    result = client.set_httpx_client(mock_httpx_client)
    assert isinstance(result, Client)


def test_client_get_httpx_client_returns_client(client):
    """Test that Client.get_httpx_client() returns an httpx.Client instance"""
    result = client.get_httpx_client()
    assert isinstance(result, httpx.Client)


def test_client_set_async_httpx_client_returns_new_instance(
    client, mock_async_httpx_client
):
    """Test that Client.set_async_httpx_client() returns a new Client instance"""
    result = client.set_async_httpx_client(mock_async_httpx_client)
    assert isinstance(result, Client)


def test_client_get_async_httpx_client_returns_client(client):
    """Test Client.get_async_httpx_client() returns httpx.AsyncClient instance"""
    result = client.get_async_httpx_client()
    assert isinstance(result, httpx.AsyncClient)


@pytest.mark.parametrize(
    "headers",
    [
        {"User-Agent": "test-agent"},
        {"Authorization": "Bearer token"},
        {"X-Custom": "value"},
    ],
    ids=["user_agent", "bearer_auth", "custom_header"],
)
def test_authenticated_client_with_headers_returns_new_instance(auth_client, headers):
    """Test AuthenticatedClient.with_headers() returns new instance"""
    result = auth_client.with_headers(headers)
    assert isinstance(result, AuthenticatedClient)


@pytest.mark.parametrize(
    "cookies",
    [
        {"session": "abc123"},
        {"prefs": "dark_mode"},
        {"session": "xyz", "theme": "light"},
    ],
    ids=["session_cookie", "prefs_cookie", "multiple_cookies"],
)
def test_authenticated_client_with_cookies_returns_new_instance(auth_client, cookies):
    """Test AuthenticatedClient.with_cookies() returns new instance"""
    result = auth_client.with_cookies(cookies)
    assert isinstance(result, AuthenticatedClient)


@pytest.mark.parametrize(
    "timeout",
    [
        httpx.Timeout(5.0),
        httpx.Timeout(30.0),
        httpx.Timeout(10.0, read=20.0),
    ],
    ids=["short_timeout", "long_timeout", "custom_read_timeout"],
)
def test_authenticated_client_with_timeout_returns_new_instance(auth_client, timeout):
    """Test AuthenticatedClient.with_timeout() returns new instance"""
    result = auth_client.with_timeout(timeout)
    assert isinstance(result, AuthenticatedClient)


def test_authenticated_client_set_httpx_client_returns_new_instance(
    auth_client, mock_httpx_client
):
    """Test AuthenticatedClient.set_httpx_client() returns new instance"""
    result = auth_client.set_httpx_client(mock_httpx_client)
    assert isinstance(result, AuthenticatedClient)


def test_authenticated_client_get_httpx_client_returns_client(auth_client):
    """Test AuthenticatedClient.get_httpx_client() returns httpx.Client instance"""
    result = auth_client.get_httpx_client()
    assert isinstance(result, httpx.Client)


def test_authenticated_client_set_async_httpx_client_returns_new_instance(
    auth_client, mock_async_httpx_client
):
    """Test AuthenticatedClient.set_async_httpx_client() returns new instance"""
    result = auth_client.set_async_httpx_client(mock_async_httpx_client)
    assert isinstance(result, AuthenticatedClient)


def test_authenticated_client_get_async_httpx_client_returns_client(auth_client):
    """Test AuthenticatedClient.get_async_httpx_client() returns AsyncClient"""
    result = auth_client.get_async_httpx_client()
    assert isinstance(result, httpx.AsyncClient)
