![Spot-me-songs](https://github.com/Alfon22A/GNOD-Project/blob/master/Images/Spot-me-songs200.png)

# Spot-me-songs

This is a Song Recommender built with Python SpotiPy using the Spotify API.

## Data Collection

Web Scrapping: [Billboard](https://www.billboard.com/charts/hot-100/)

Spotify API: [Spotify](https://open.spotify.com/playlist/1G8IpkZKobrIlXcVPoSIuf)

## Clustering

### Tested

K-Means
- K: 2-30
	
DBSCAN
- ε: 2.556919002986411
- Neighbors: 5
	
Gaussian Mixtures
- Covariance types: full, tied, diag, spherical
- N: 3-30
	
Agglomerative Clustering: 
- N: 2-30
	
### Chosen

K-Means with 28 clusters

## Front end

Built with Streamlit

You will need a ```config.py``` file in ```Src/Lib/``` with your credentials:

Client_ID = ""
Client_Secret = ""
