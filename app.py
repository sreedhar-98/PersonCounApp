import streamlit as st
from streamlit_webrtc import webrtc_streamer,VideoHTMLAttributes
from test2 import callback1


st.title("Person Counter App")
webrtc_streamer(key="sample", video_frame_callback=callback1,media_stream_constraints={"video":True,"audio":False},
                rtc_configuration={ "iceServers": [{"urls": ["turn:global.relay.metered.ca:80"],"username":'51634103147da7f5e3a354b5',"credential":"P+HO7Cc0P3wIIMim"}]})


