import requests
import os
import hashlib
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get URLs from user input
    urls_input = input("Please enter the image URLs (comma-separated): ")
    url_list = [u.strip() for u in urls_input.split(",") if u.strip()]

    # Call the download function
    download_images(url_list)


def download_images(urls, dest_folder="Fetched_Images"):
    os.makedirs(dest_folder, exist_ok=True)

    # Track downloaded images to avoid duplicates
    seen_hashes = set()

    # Safe request headers
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        ),
        "Accept": "image/*"
    }

    for url in urls:
        print(f"\nFetching: {url}")

        try:
            # Fetch the image
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Check Content-Type
            content_type = response.headers.get("Content-Type", "")
            if not content_type.startswith("image/"):
                print(f"✗ Skipped: Content-Type not image (got '{content_type}')")
                continue

            # Generate hash of the content
            file_hash = hashlib.md5(response.content).hexdigest()
            if file_hash in seen_hashes:
                print("✗ Skipped: Duplicate image detected")
                continue
            seen_hashes.add(file_hash)

            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path) or f"image_{file_hash[:8]}.jpg"
            filepath = os.path.join(dest_folder, filename)

            print(f"Saving to: {filepath}")

            # Save the image
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("Connection strengthened. Community enriched.")

        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")

        except Exception as e:
            print(f"✗ An error occurred: {e}")


if __name__ == "__main__":
    main()
