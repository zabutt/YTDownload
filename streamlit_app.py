import streamlit as st
from pytube import YouTube
import os
import shutil
from datetime import datetime, timedelta

# Set page title and favicon
st.set_page_config(page_title="YouTube Downloader", page_icon=":arrow_down:")

# Function to download YouTube video
def download_video(youtube_url, download_type):
    try:
        yt = YouTube(youtube_url)
        if download_type == "Video":
            stream = yt.streams.filter(file_extension="mp4").first()
        else:
            stream = yt.streams.filter(only_audio=True).first()

        output_path = f"./downloads/{yt.title}.{stream.subtype}"
        stream.download(output_path)

        return output_path
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Function to clean up old files
def clean_up_old_files():
    downloads_folder = "./downloads"
    current_time = datetime.now()

    for filename in os.listdir(downloads_folder):
        file_path = os.path.join(downloads_folder, filename)
        file_time = datetime.fromtimestamp(os.path.getctime(file_path))

        if current_time - file_time > timedelta(minutes=10):
            os.remove(file_path)

# Create downloads folder
os.makedirs("./downloads", exist_ok=True)

# Main Streamlit app
def main():
    st.title("YouTube Downloader")
    st.image("ytlogo.png", use_container_width=True)  # Add your logo image path

    # User input for YouTube URL
    youtube_url = st.text_input("Enter YouTube Video URL:")

    if youtube_url:
        # User input for download type
        download_type = st.selectbox("Select Download Type:", ["Video", "Audio"])

        if st.button("Download"):
            # Download video or audio
            file_path = download_video(youtube_url, download_type)

            if file_path:
                # Provide download link
                st.success(f"Download successful! [Download Link]({file_path})")

    # Run clean-up of old files
    clean_up_old_files()

if __name__ == "__main__":
    main()
