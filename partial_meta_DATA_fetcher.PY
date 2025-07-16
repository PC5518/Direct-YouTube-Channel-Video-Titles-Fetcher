import yt_dlp
import sys

def get_channel_video_titles(channel_url):
    """
    Connects to a YouTube channel URL and extracts the titles of all its videos.

    Args:
        channel_url (str): The URL of the YouTube channel's main page or videos tab.

    Returns:
        list: A list of video titles, or None if an error occurs.
    """
    # These are the options we'll pass to yt-dlp.
    ydl_opts = {
        'quiet': True,              # Suppress console output from yt-dlp
        'extract_flat': 'in_playlist', # Don't process individual video pages, just list them
        'force_generic_extractor': True, # Important for treating channel URLs as playlists
        'ignoreerrors': True,       # Continue on download errors
    }

    titles = []
    print(f"Attempting to fetch videos from: {channel_url}")

    try:
        # The 'with' statement ensures resources are properly closed.
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract information from the URL
            info_dict = ydl.extract_info(channel_url, download=False)

            # Check if the 'entries' key exists. This key holds the list of videos.
            if 'entries' in info_dict:
                videos = info_dict['entries']
                print(f"Found {len(videos)} videos. Extracting titles...")
                
                # Loop through each video entry and grab its title
                for video in videos:
                    # Some entries might be malformed, so we check if 'title' exists.
                    if video and 'title' in video:
                        titles.append(video['title'])
            else:
                print("Could not find a list of videos for this URL. Is it a valid channel URL?")
                return None

    except yt_dlp.utils.DownloadError as e:
        # Handle errors, like an invalid URL
        print(f"\nError: Could not process the URL. Please check if it's correct.")
        print(f"yt-dlp error message: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

    return titles

# This block runs when the script is executed directly
if __name__ == "__main__":
    print("--- YouTube Video Title Downloader ---")
    print("Please provide the URL of the YouTube channel's main page or its 'Videos' tab.")
    print("Examples:")
    print("  - https://www.youtube.com/@MrBeast")
    print("  - https://www.youtube.com/c/mkbhd")
    print("  - https://www.youtube.com/channel/UCBJycsmduvYEL83R_U4JriQ\n")
    
    # Get the channel URL from the user
    # Note: We use channel URL instead of just the name because it's more reliable.
    # yt-dlp is smart enough to handle different URL formats (@handle, /c/, /channel/).
    input_url = input("Enter your YouTube URL:  ")

    if not input_url:
        print("No URL entered. Exiting.")
        sys.exit()

    # Call our function to get the titles
    video_titles = get_channel_video_titles(input_url)

    # If we got titles back, print them out neatly.
    if video_titles:
        print("\n--- All Video Titles ---")
        for i, title in enumerate(video_titles, 1):
            print(f"{i}. {title}")
        
        print(f"\nSuccessfully downloaded {len(video_titles)} titles.")
    else:
        print("\nCould not retrieve any video titles.")