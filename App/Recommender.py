import pandas as pd
import numpy as np

import streamlit as st

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# import sys
# sys.path.insert(1, '../Src/Lib')
# from config import *

import pickle
import yaml

def recommender(track):
	
	st.write("Selected {} by {} from {}".format(track["name"], track["artists"][0]["name"], track["album"]["name"]))
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=st.secrets["Client_ID"], client_secret=st.secrets["Client_Secret"]))

	track_columns = ["Song", "Artist", "ID", "Link",
                    "danceability", "energy", "key", "loudness",
                    "mode", "speechiness", "instrumentalness", "liveness",
                    "valence", "tempo", "duration_ms", "time_signature"]
	
	track_features = {}
	track_features["Song"] = track["name"]
	track_features["Artist"] = track["artists"][0]["name"]
	track_features["ID"] = track["id"]
	track_features["Link"] = track["external_urls"]["spotify"]
        
	audio_features = sp.audio_features(track["id"])[0]
	for feature in track_columns[4:]:
		track_features[feature] = audio_features[feature]
            
	song_data = pd.DataFrame.from_dict(track_features, orient = "index").T
	song_data.columns = song_data.columns = ['Song', 'Artist', 'ID', 'Link',
                                            'Danceability', 'Energy', 'Key','Loudness',
                                            'Mode', 'Speechiness', 'Instrumentalness', 'Liveness',
                                            'Valence', 'Tempo', 'Duration', 'Time Signature']
        
	song_data = song_data.drop(columns = ["Song", "Artist", "ID", "Link", "Energy", "Mode", "Time Signature", "Duration", "Key", "Liveness"])
            
	with open("../params.yaml", "r") as file:
		config = yaml.safe_load(file)
            
	with open(config["Transformers"]["Power"], "rb") as file:
		transformer = pickle.load(file)
	song_data_pt = transformer.transform(song_data)
        
	with open(config["Scalers"]["Standard"], "rb") as file:
		scaler = pickle.load(file)
	song_data_pt_ss = scaler.transform(song_data_pt)
        
	with open(config["Models"]["K-Means"], "rb") as file:
		km = pickle.load(file)
	cluster = km.predict(song_data_pt_ss)
            
	with open(config["Data"]["Songs_DB_Clusters"], "r", encoding = "utf-8") as file:
		songs = pd.read_csv(file)
        
	st.write("Your recommended songs are:")
        
	if track_features["ID"] in list(songs["ID"][songs["Label"] == "H"]):
		
		st.write("Your song is in the Top 100!")
		
		examples = songs[(songs["Label"] == "H") & (songs["Cluster"] == cluster[0])].sample(3)
            
		c = st.expander("Recommended songs")

		url = examples.iloc[0]["Link"]
		c.write("{} by {}".format(examples.iloc[0]["Song"], examples.iloc[0]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)
		
		url = examples.iloc[1]["Link"]
		c.write("{} by {}".format(examples.iloc[1]["Song"], examples.iloc[1]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)
		
		url = examples.iloc[2]["Link"]
		c.write("{} by {}".format(examples.iloc[2]["Song"], examples.iloc[2]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)  
		
	else:
		examples = songs[(songs["Label"] == "N") & (songs["Cluster"] == cluster[0])].sample(3)
            
		c = st.expander("Recommended songs")

		url = examples.iloc[0]["Link"]
		c.write("{} by {}".format(examples.iloc[0]["Song"], examples.iloc[0]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)
		
		url = examples.iloc[1]["Link"]
		c.write("{} by {}".format(examples.iloc[1]["Song"], examples.iloc[1]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)
		
		url = examples.iloc[2]["Link"]
		c.write("{} by {}".format(examples.iloc[2]["Song"], examples.iloc[2]["Artist"]))
		url2 = url.split("m/t")
		embed = url2[0]+"m/embed/t"+url2[1]
		spotify = '<iframe style="border-radius:12px" src={} width="100%" height="80" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>'.format(embed)
		c.markdown(spotify, unsafe_allow_html=True)