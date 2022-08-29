![Spot-me-songs](https://github.com/Alfon22A/GNOD-Project/blob/master/Images/Spot-me-songs200.png)

# Spot-me-songs

## Introduction

This is a Song Recommender built with Python SpotiPy using the Spotify API.

It contains a database with over 3500 songs collected with two different methods.

The finished product is an interface where you input your song, pick between five options at most, and then get three song recommendations.

It has a Spotify embedded player.

## Data Collection

Web Scrapping: [Billboard](https://www.billboard.com/charts/hot-100/)

Spotify API: [Spotify](https://open.spotify.com/playlist/1G8IpkZKobrIlXcVPoSIuf)

## Clustering

### Variables

[Spotify](https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features)

#### Danceability

Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

#### Instrumentalness

Predicts whether a track contains no vocals. “Ooh” and “aah” sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly “vocal”. The closer the instrumentalness value is to 1.0, the greater the likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.

#### Loudness

The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.

#### Speechiness

Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g., talk show, audiobook, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.

#### Tempo

The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.

#### Valence

A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g., happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g., sad, depressed, angry).

### Tested methods

K-Means
- K: 2-30
	
DBSCAN
- Epsilon: 2.556919002986411
- Neighbors: 5
	
Gaussian Mixtures
- Covariance types: full, tied, diag, spherical
- N: 3-30
	
Agglomerative Clustering: 
- N: 2-30
	
### Chosen method

K-Means with 28 clusters.

## Front end

Built with Streamlit.

To use, run the Python script Spot-me-songs.py with the following command in your console:

```powershell
streamlit run Spot-me-songs.py
```
## Config

You will need a ```config.py``` file in ```Src/Lib/``` with your credentials:

Client_ID = ""

Client_Secret = ""