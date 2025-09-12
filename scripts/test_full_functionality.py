#!/usr/bin/env python3
"""
Test script for PeerTube API wrappers.

This script will test the full functionality once dependencies are installed.
Run with: python scripts/test_full_functionality.py
"""

import sys
from pathlib import Path

# Add src to Python path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


def test_imports():
    """Test that all imports work correctly."""
    print("🔍 Testing imports...")
    
    try:
        from peertube.base.exceptions import PeerTubeError, AuthenticationError
        print("  ✅ Base exceptions imported")
        
        from peertube.base.types import AuthToken, User, Video
        print("  ✅ Base types imported")
        
        from peertube.base.client import PeerTubeClient, PeerTubeConfig
        print("  ✅ Client classes imported")
        
        from peertube.auth.session import SessionClient, login
        print("  ✅ Auth session imported")
        
        from peertube.auth.register import RegisterClient, register_user
        print("  ✅ Auth registration imported")
        
        # Test main package imports
        from peertube import (
            PeerTubeClient, PeerTubeConfig, 
            login, logout, get_user_info, register_user,
            hello_world
        )
        print("  ✅ Main package imports successful")
        
    except ImportError as e:
        print(f"  ❌ Import error: {e}")
        return False
    
    return True


def test_basic_functionality():
    """Test basic functionality without network calls."""
    print("\n🧪 Testing basic functionality...")
    
    try:
        from peertube.base.types import AuthToken, User, Video
        from peertube.base.exceptions import AuthenticationError
        from peertube.base.client import PeerTubeConfig
        
        # Test model creation
        token = AuthToken(access_token="test123", token_type="Bearer")
        print(f"  ✅ AuthToken created: {token.access_token}")
        
        user = User(id=1, username="testuser", role="user", created_at="2023-01-01")
        print(f"  ✅ User created: {user.username}")
        
        video = Video(
            id=1, name="Test Video", duration=120, views=100,
            likes=10, dislikes=1, published_at="2023-01-01", created_at="2023-01-01"
        )
        print(f"  ✅ Video created: {video.name}")
        
        # Test configuration
        config = PeerTubeConfig(base_url="https://example.com", token="test")
        print(f"  ✅ Config created: {config.base_url}")
        
        # Test exception handling
        try:
            raise AuthenticationError("Test error")
        except AuthenticationError as e:
            print(f"  ✅ Exception handling works: {e.message}")
        
    except Exception as e:
        print(f"  ❌ Functionality error: {e}")
        return False
    
    return True


def test_legacy_compatibility():
    """Test that legacy functionality still works."""
    print("\n🔄 Testing legacy compatibility...")
    
    try:
        from peertube.functions.hello_world import hello_world
        result = hello_world("PeerTube")
        expected = "Hello, PeerTube!"
        
        if result == expected:
            print(f"  ✅ Legacy function works: {result}")
            return True
        else:
            print(f"  ❌ Legacy function failed: expected '{expected}', got '{result}'")
            return False
            
    except Exception as e:
        print(f"  ❌ Legacy compatibility error: {e}")
        return False


def test_package_structure():
    """Test that the package structure is correct."""
    print("\n📁 Testing package structure...")
    
    base_path = Path(__file__).parent.parent / "src" / "peertube"
    
    expected_dirs = [
        "base", "auth", "functions", "videos", "search"
    ]
    
    expected_files = [
        "__init__.py",
        "base/__init__.py", "base/client.py", "base/exceptions.py", "base/types.py",
        "auth/__init__.py", "auth/session.py", "auth/register.py",
        "functions/__init__.py", "functions/hello_world.py",
        "videos/__init__.py", "search/__init__.py"
    ]
    
    all_good = True
    
    for directory in expected_dirs:
        dir_path = base_path / directory
        if dir_path.exists():
            print(f"  ✅ Directory exists: {directory}/")
        else:
            print(f"  ❌ Directory missing: {directory}/")
            all_good = False
    
    for file_path in expected_files:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"  ✅ File exists: {file_path}")
        else:
            print(f"  ❌ File missing: {file_path}")
            all_good = False
    
    return all_good


def main():
    """Run all tests."""
    print("🚀 PeerTube API Wrappers - Full Functionality Test")
    print("=" * 50)
    
    tests = [
        ("Package Structure", test_package_structure),
        ("Legacy Compatibility", test_legacy_compatibility),
        ("Imports", test_imports),
        ("Basic Functionality", test_basic_functionality),
    ]
    
    results = []
    for test_name, test_func in tests:
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary:")
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {test_name}")
        if not passed:
            all_passed = False
    
    if all_passed:
        print("\n🎉 All tests passed! PeerTube API wrappers are ready.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the output above for details.")
        return 1


if __name__ == "__main__":
    sys.exit(main())