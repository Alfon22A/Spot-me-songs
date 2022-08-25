import pandas as pd
import numpy as np

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from config import *

import pickle
import yaml

def search_song():
	
	sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= Client_ID, client_secret= Client_Secret))
	
	print("Please write a song name:")
	song = str(input())
	print()
	try:
		results = sp.search(q=song, limit = 5)
    
		for track in results["tracks"]["items"]:
			print(results["tracks"]["items"].index(track)+1)
			print("Song:",track["name"])
			print("Artist:",track["artists"][0]["name"])
			print("Album:",track["album"]["name"])
			print("Link:",track["external_urls"]["spotify"])
			print()
        
		print("Which song did you mean?",range(len(results["tracks"]["items"]))[0]+1,"-",range(len(results["tracks"]["items"]))[-1]+1)
		print("If your song is not here, input 0")
		select = int(input())
		print()
    
		while select > len(results["tracks"]["items"]):
			print("Please input a valid number")
			select = int(input())
			print()
        
		else:
			if select == 0:
				search_song()
        
			else:
				print("Selected", results["tracks"]["items"][select-1]["name"],"by",results["tracks"]["items"][select-1]["artists"][0]["name"])
				print()
        
				track_columns = ["Song", "Artist", "ID", "Link",
                         "danceability", "energy", "key", "loudness",
                         "mode", "speechiness", "instrumentalness", "liveness",
                         "valence", "tempo", "duration_ms", "time_signature"]
        
				track = results["tracks"]["items"][select-1]
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
        
				if track_features["ID"] in list(songs["ID"][songs["Label"] == "H"]):
					print("Your song is in the Top 100!")
					print()
					examples = songs[(songs["Label"] == "H") & (songs["Cluster"] == cluster[0])].sample(3)
            
					print("Song:",examples.iloc[0]["Song"])
					print("Artist:",examples.iloc[0]["Artist"])
					print("Link:",examples.iloc[0]["Link"])
					print()
					print("Song:",examples.iloc[1]["Song"])
					print("Artist:",examples.iloc[1]["Artist"])
					print("Link:",examples.iloc[1]["Link"])
					print()
					print("Song:",examples.iloc[2]["Song"])
					print("Artist:",examples.iloc[2]["Artist"])
					print("Link:",examples.iloc[2]["Link"])        
				else:
					examples = songs[(songs["Label"] == "N") & (songs["Cluster"] == cluster[0])].sample(3)
            
					print("Song:",examples.iloc[0]["Song"])
					print("Artist:",examples.iloc[0]["Artist"])
					print("Link:",examples.iloc[0]["Link"])
					print()
					print("Song:",examples.iloc[1]["Song"])
					print("Artist:",examples.iloc[1]["Artist"])
					print("Link:",examples.iloc[1]["Link"])
					print()
					print("Song:",examples.iloc[2]["Song"])
					print("Artist:",examples.iloc[2]["Artist"])
					print("Link:",examples.iloc[2]["Link"])
		print()
		print("Would you like more recomendations? Y/N")
		answer = str(input())
		if answer in ["Y", "y", "Yes", "yes"]:
			search_song()
		else:
			print("Bye!")
				
	except:
		print("Your song was not found, please try again.")
		print()
		search_song()

if __name__ == "__main__":
	search_song()