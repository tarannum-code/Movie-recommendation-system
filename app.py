import streamlit as st
import pickle
import pandas as pd
import requests
from config import api_key

# -------------------- LOAD DATA --------------------

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Ensure movies is a DataFrame
if not isinstance(movies, pd.DataFrame):
    movies = pd.DataFrame(movies)

# -------------------- TMDB POSTER FUNCTION --------------------

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')

    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"

# -------------------- RECOMMENDER FUNCTION --------------------

def recommend(movie):
    if movie not in movies['title'].values:
        return [], []

    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters

# -------------------- STREAMLIT UI --------------------

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎥 Movie Recommender System")

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    if names:
        cols = st.columns(5)
        for i in range(5):
            with cols[i]:
                st.image(posters[i])
                st.caption(names[i])
    else:
        st.error("Movie not found!")
