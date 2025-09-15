#!/usr/bin/env python3
"""
Example demonstrating PeerTube API wrapper integration with generated OpenAPI client.

This example shows how the PeerTube API wrappers now integrate with the 
auto-generated OpenAPI client while maintaining backward compatibility.
"""

from peertube import (
    PeerTubeClient,
    PeerTubeConfig,
    get_video,
    list_videos,
    search_videos,
    login,
)


def main():
    """Demonstrate PeerTube API wrapper usage with generated client integration."""
    print("🎬 PeerTube API Wrapper Examples")
    print("=" * 50)
    
    # Configuration
    instance_url = "https://example.peertube.com"  # Replace with actual instance
    
    # Example 1: Basic client with generated client integration
    print("\n1️⃣ Basic Client Configuration")
    config = PeerTubeConfig(base_url=instance_url)
    
    with PeerTubeClient(config) as client:
        print(f"✅ Client created for: {config.base_url}")
        print(f"Generated client available: {client.generated_client is not None}")
        
        if client.generated_client:
            print(f"Generated client type: {type(client.generated_client).__name__}")
            print("🔄 The generated client provides type-safe access to all PeerTube API endpoints")
    
    # Example 2: Convenience functions (using manual wrappers)
    print("\n2️⃣ Convenience Functions (Manual Wrappers)")
    try:
        # These use the existing manual wrapper implementations
        videos = list_videos(instance_url, count=5)
        print(f"✅ Listed videos: {videos.get('total', 'unknown')} total")
        
        if videos.get('data'):
            first_video = videos['data'][0]
            video_id = first_video.get('uuid', first_video.get('id'))
            if video_id:
                video_details = get_video(instance_url, video_id)
                print(f"✅ Retrieved video: {video_details.get('name', 'Unknown')}")
        
        # Search functionality
        search_results = search_videos(instance_url, "tutorial")
        print(f"✅ Search results: {search_results.get('total', 0)} videos found")
        
    except Exception as e:
        print(f"ℹ️  Note: {e} (Expected for demo - requires real PeerTube instance)")
    
    # Example 3: Authentication with generated client
    print("\n3️⃣ Authentication with Generated Client")
    try:
        # Login example (would need real credentials)
        auth_token = login(instance_url, "username", "password")
        print(f"✅ Authentication successful: {auth_token.get('access_token', 'token')[:10]}...")
        
        # Create authenticated client
        auth_config = PeerTubeConfig(
            base_url=instance_url,
            token=auth_token.get('access_token')
        )
        
        with PeerTubeClient(auth_config) as auth_client:
            print(f"✅ Authenticated client created")
            print(f"Generated client type: {type(auth_client.generated_client).__name__}")
            
            # The generated client now has access to authenticated endpoints
            if hasattr(auth_client.generated_client, 'token'):
                print("🔐 Generated client is authenticated and ready for protected endpoints")
                
    except Exception as e:
        print(f"ℹ️  Note: {e} (Expected for demo - requires real credentials)")
    
    # Example 4: Direct use of generated client
    print("\n4️⃣ Direct Generated Client Usage")
    config = PeerTubeConfig(base_url=instance_url)
    
    with PeerTubeClient(config) as client:
        if client.generated_client:
            print("✅ Generated client is available for direct use")
            print("📋 Available API modules:")
            
            # Show available API modules from generated client
            try:
                import os
                api_dir = os.path.join(os.path.dirname(client.generated_client.__class__.__module__.replace('.', '/')), '..', 'api')
                api_modules_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'peertube', 'generated_client', 'api')
                
                if os.path.exists(api_modules_path):
                    api_modules = [name for name in os.listdir(api_modules_path) 
                                  if os.path.isdir(os.path.join(api_modules_path, name)) and not name.startswith('_')]
                    
                    # Show some key modules
                    key_modules = ['video', 'session', 'search', 'accounts', 'users', 'config', 'abuses', 'register']
                    shown = []
                    
                    for module in key_modules:
                        if module in api_modules:
                            print(f"  • {module}")
                            shown.append(module)
                    
                    # Show a few more
                    remaining = [m for m in sorted(api_modules) if m not in shown][:5]
                    for module in remaining:
                        print(f"  • {module}")
                    
                    total_modules = len(api_modules)
                    print(f"  ... total: {total_modules} API module groups covering 200+ endpoints")
                else:
                    print("  • video, session, search, accounts, users, config, and more...")
                    
            except Exception:
                print("  • video, session, search, accounts, users, config, and more...")
    
    # Example 5: Integration benefits
    print("\n5️⃣ Integration Benefits")
    print("✅ Backward compatibility: All existing wrapper functions still work")
    print("✅ Type safety: Generated client provides full type annotations")
    print("✅ Complete coverage: Generated client covers all 200+ PeerTube API endpoints")
    print("✅ Automatic updates: Regenerate client when PeerTube API changes")
    print("✅ Best of both worlds: Use convenient wrappers or direct generated client")
    
    print("\n🎉 PeerTube API integration complete!")
    print("📖 Use wrapper functions for common operations, generated client for advanced use cases")


if __name__ == "__main__":
    main()