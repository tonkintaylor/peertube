#!/usr/bin/env python3
"""
Script to regenerate the OpenAPI client.

This script fixes known issues in the PeerTube OpenAPI specification and
generates a compatible Python client using openapi-python-client.
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path


def fix_openapi_spec(input_path: Path, output_path: Path) -> None:
    """Fix validation issues in the OpenAPI spec."""
    print("Loading and fixing OpenAPI specification...")
    
    with open(input_path) as f:
        spec = json.load(f)
    
    # Fix callback references that cause validation errors
    paths_to_fix = [
        "/api/v1/search/videos",
        "/api/v1/search/video-channels", 
        "/api/v1/search/video-playlists"
    ]
    
    for path_key in paths_to_fix:
        if path_key in spec.get("paths", {}):
            path_item = spec["paths"][path_key]
            if "get" in path_item and "callbacks" in path_item["get"]:
                print(f"  Removing callbacks from {path_key}")
                del path_item["get"]["callbacks"]
    
    # Write the fixed spec
    with open(output_path, "w") as f:
        json.dump(spec, f, indent=2)
    
    print(f"Fixed OpenAPI spec written to {output_path}")


def generate_client(
    spec_path: Path, 
    output_dir: Path, 
    config_path: Path | None = None
) -> bool:
    """Generate the OpenAPI client."""
    print(f"Generating OpenAPI client from {spec_path}...")
    
    # Build command
    cmd = [
        "openapi-python-client", 
        "generate",
        "--path", str(spec_path),
        "--output-path", str(output_dir),
        "--meta", "none",
        "--no-fail-on-warning",
        "--overwrite"
    ]
    
    if config_path and config_path.exists():
        cmd.extend(["--config", str(config_path)])
    
    # Run generation
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("✅ Client generation completed successfully")
            if result.stdout:
                print("Output:", result.stdout)
            if result.stderr:
                print("Warnings/Info:", result.stderr)
            return True
        else:
            print("❌ Client generation failed")
            print("Error:", result.stderr)
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running openapi-python-client: {e}")
        return False


def main() -> int:
    """Main function to regenerate the OpenAPI client."""
    print("🔄 Regenerating PeerTube OpenAPI Client")
    print("=" * 50)
    
    # Define paths
    repo_root = Path(__file__).parent.parent
    openapi_spec = repo_root / "assets" / "openapi.json"
    config_file = repo_root / "openapi-client-config.yaml"
    output_dir = repo_root / "src" / "peertube" / "generated_client"
    temp_spec = Path("/tmp/openapi_fixed.json")
    temp_gen_dir = Path("/tmp/peertube_gen")
    
    # Check if OpenAPI spec exists
    if not openapi_spec.exists():
        print(f"❌ OpenAPI specification not found: {openapi_spec}")
        return 1
    
    try:
        # Step 1: Fix the OpenAPI spec
        fix_openapi_spec(openapi_spec, temp_spec)
        
        # Step 2: Clean existing generated client
        if output_dir.exists():
            print(f"Cleaning existing generated client: {output_dir}")
            shutil.rmtree(output_dir)
        
        # Step 3: Generate client to temp directory
        if not generate_client(temp_spec, temp_gen_dir, config_file):
            return 1
        
        # Step 4: Copy generated client to final location
        print(f"Moving generated client to {output_dir}")
        shutil.copytree(temp_gen_dir, output_dir)
        
        # Step 5: Clean up temp files
        if temp_spec.exists():
            temp_spec.unlink()
        if temp_gen_dir.exists():
            shutil.rmtree(temp_gen_dir)
        
        print("\n✅ OpenAPI client regeneration completed successfully!")
        print(f"📁 Generated client location: {output_dir}")
        
        # Step 6: Test import
        print("\n🧪 Testing generated client import...")
        try:
            from peertube.generated_client import Client, AuthenticatedClient
            print("✅ Generated client imports successfully")
        except ImportError as e:
            print(f"⚠️  Warning: Generated client import failed: {e}")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error during generation: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())