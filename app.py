import streamlit as st
from streamlit_webrtc import webrtc_streamer,VideoHTMLAttributes
from test2 import callback1
from twilio.rest import Client

# account_sid=st.secrets["sid"]
# auth_token=st.secrets["token"]
# client=Client(account_sid,auth_token)

# token=client.tokens.create()

st.title("Person Counter App")
webrtc_streamer(key="sample", video_frame_callback=callback1,media_stream_constraints={"video":True,"audio":False})


 