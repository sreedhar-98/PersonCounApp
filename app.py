import streamlit as st
from streamlit_webrtc import webrtc_streamer,VideoHTMLAttributes
from test2 import callback1


st.title("Person Counter App")
webrtc_streamer(key="sample", video_frame_callback=callback1,media_stream_constraints={"video":True,"audio":False},
                rtc_configuration={ "iceServers": [{"urls": ["turn:openrelay.metered.ca:80"],"username":'openrelayproject',"credentials":"openrelayproject"}]})


