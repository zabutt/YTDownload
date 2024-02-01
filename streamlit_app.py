import streamlit as st
from pytube import YouTube
import tempfile
import shutil

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

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = f"{tmpdir}/{yt.title}.{stream.subtype}"
            stream.download(output_path)

            return output_path
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Main Streamlit app
def main():
    st.title("YouTube Downloader")
    st.image("your_logo.png", use_container_width=True)  # Add your logo image path

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

if __name__ == "__main__":
    main()

