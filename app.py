import streamlit as st
from streamlit_webrtc import webrtc_streamer,VideoHTMLAttributes
from test2 import callback1


st.title("Person Counter App")
webrtc_streamer(key="sample", video_frame_callback=callback1,media_stream_constraints={"video":True,"audio":False},
                rtc_configuration={ "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})


