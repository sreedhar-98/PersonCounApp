import streamlit as st
from streamlit_webrtc import webrtc_streamer,VideoHTMLAttributes
import streamlit.components.v1 as com
from test2 import callback1


st.title("Person Counter App")
webrtc_streamer(key="sample", video_frame_callback=callback1,media_stream_constraints={"video":True,"audio":False})


