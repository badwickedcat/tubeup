# tubeup
# TubeUp - YouTube Video Uploader

TubeUp is a Python script that automates the process of uploading videos to your YouTube playlist. It utilizes the YouTube Data API v3 for seamless integration.

## Setup

1. **Install Dependencies:**
    ```bash
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
    ```

2. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/tubeup.git
    cd tubeup
    ```

3. **Configure API Key:**
    - Follow the instructions in the [Google Cloud Console](https://console.cloud.google.com/) to obtain your API key.
    - Replace `YOUR_API_KEY` in the script with your actual API key.

4. **Run the Script:**
    ```bash
    python tubeup.py
    ```

## Important Note

Ensure you have created a playlist on YouTube before running the script. The uploaded videos will be added to this playlist.

## Contribution

Feel free to contribute to this project by creating issues or submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
