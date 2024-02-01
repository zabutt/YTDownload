import streamlit as st
from pytube import YouTube
import io
import base64

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

        video_bytes = stream.stream_to_buffer()
        return video_bytes
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
            video_bytes = download_video(youtube_url, download_type)

            if video_bytes:
                # Provide download link
                download_link = f"data:video/{download_type.lower()};base64,{base64.b64encode(video_bytes.getvalue()).decode()}"
                st.success(f"Download successful! [Download Link]({download_link})")

if __name__ == "__main__":
    main()
