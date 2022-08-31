import streamlit as st

import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import pickle
import yaml

from Recommender import recommender

def main ():
	
	options = ["Main", "Stop"]
	choice = st.sidebar.selectbox("Menu", options, key = "1")
	if (choice == "Main"):
		col1, col2 = st.columns(2)
		col1.title("Spot-me-songs")
		col1.write("By Alfonso Muñoz and Ignace Gravereaux, 2022")
		col2.image("Images/Spot-me-songs.png")
		st.header("Get song recommendations from a database with more than 3500 songs!")
		song = st.text_input("Title of your song:")
		if song:
			def search_song(song):
	
				sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=st.secrets["Client_ID"], client_secret=st.secrets["Client_Secret"]))
					
				results = sp.search(q=song, limit = 5)
				
				if len(results["tracks"]["items"]) > 0:
					
					st.write("Pick the one you meant:")
					
					try:
						for track in results["tracks"]["items"]:
							selection = st.button("{} by {} from {}".format(track["name"], track["artists"][0]["name"], track["album"]["name"]))
							url = track["external_urls"]["spotify"]
							url2 = url.split("m/t")
							embed = url2[0]+"m/embed/t"+url2[1]
							spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
							st.markdown(spotify, unsafe_allow_html=True)
						
							if selection:
								recommender(track)
							
					except:
						pass
					
					st.write("If it is not there, try again!")
				
				else:
					st.write("We couldn't find your song, please try again!")
					
			search_song(song)
			
	else:
		st.stop()
    
main()