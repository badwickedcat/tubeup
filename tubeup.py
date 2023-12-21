import os
import random
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload

# Replace these placeholders with your actual API keys and folder paths
API_KEY = "YOUR_YOUTUBE_API_KEY"
VIDEO_FOLDER = "PATH_TO_YOUR_VIDEO_FOLDER"
PLAYLIST_TITLE = "YOUR_PLAYLIST_TITLE"
TAGS_FILE = "tags.txt"

# Function to read tags from the file
def get_tags(file_path, num_tags):
    with open(file_path, 'r') as file:
        tags = [tag.strip() for tag in file.readlines()]

    # Categorize tags based on length
    short_tags = [tag for tag in tags if len(tag) <= 8]
    long_tags = [tag for tag in tags if len(tag) > 8]
    selected_tags = random.sample(short_tags, min(num_tags // 2, len(short_tags))) + \
                    random.sample(long_tags, min(num_tags // 2, len(long_tags)))

    return selected_tags

# Replace this function call with your actual API key
def authenticate_youtube(api_key):
    # Authenticate using API key
    youtube = build('youtube', 'v3', developerKey=api_key)
    return youtube

def create_playlist(youtube, playlist_title):
    # The rest of your code...

def add_video_to_playlist(youtube, playlist_id, video_id):
    # The rest of your code...

def upload_video(youtube, video_path, title, description, tags, playlist_id=None):
    # The rest of your code...

if __name__ == '__main__':
    # Replace this call with your actual API key
    youtube_api = authenticate_youtube(API_KEY)
if __name__ == '__main__':
    # Replace this call with your actual API key
    youtube_api = authenticate_youtube(API_KEY)

    # Replace these placeholders with your actual playlist title and video folder path
    playlist_id = create_playlist(youtube_api, PLAYLIST_TITLE)

    # Number of tags to use for each video
    num_tags_to_use = 10  # Adjust this number as needed

    # Replace this placeholder with your actual video folder path
    for video_file in os.listdir(VIDEO_FOLDER):
        if video_file.endswith('.mp4'):
            video_path = os.path.join(VIDEO_FOLDER, video_file)

            # Replace these variables with actual video details
            video_title = f'Video Title for {video_file}'
            video_description = f'Description for {video_file} goes here.'

            # Get selected tags
            selected_tags = get_tags(TAGS_FILE, num_tags_to_use)

            # Upload video with selected tags and add to the playlist
            upload_video(youtube_api, video_path, video_title, video_description, selected_tags, playlist_id)
