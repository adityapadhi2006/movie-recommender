import streamlit as st
import pickle
import pandas as pd
import requests

# Page configuration
st.set_page_config(page_title="Movie Recommender System", layout="wide")

TMDB_API_KEY = "582f5364190b97eff67367b659b5e9f8"

# Helper function to fetch movie poster from TMDB
@st.cache_data(show_spinner=False, ttl=3600)
def fetch_poster(movie_id):
    # Your TMDB API Read Access Token
    token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI1ODJmNTM2NDE5MGI5N2VmZjY3MzY3YjY1OWI1ZTlmOCIsIm5iZiI6MTc4ODk1NzUxOS4yNDk5OTk4LCJzdWIiOiI2YWExNTM0ZmNkMWI5ZDEzMDc0ZmNjZWEiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.EovoqB6ahah-ikUgQ6ZrRImSzWd5X3VtFrqnw2zi8VM"
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    fallback_poster = "https://placehold.co/500x750/png?text=Poster+Not+Found"

    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        poster_path = response.json().get("poster_path")
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    except Exception as error:
        print(f"Could not fetch poster for TMDB ID {movie_id}: {error}")

    return fallback_poster

# Load saved artifacts
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movies_dict)
    sim_matrix = pickle.load(open('similarity.pkl', 'rb'))
    return movies_df, sim_matrix

movies, similarity = load_data()

# Recommendation logic
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_titles = []
    recommended_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))
    return recommended_titles, recommended_posters

# UI Layout
st.title("🎬 Movie Recommender System")

selected_movie = st.selectbox(
    "Type or select a movie to get recommendations:",
    movies['title'].values
)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)
    cols = st.columns(5)
    
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster, width="stretch")
            