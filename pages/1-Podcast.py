import streamlit as st
st.title("Podcast")
video_file = open("static/imgs_site/scrolling_video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)
st.caption("solo come esempio")