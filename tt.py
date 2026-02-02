import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommender system')
OMDB_API_KEY = "23ea0969"


# def fetch_poster(title):
#     url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
#     data = requests.get(url).json()
    
#     # OMDb returns Poster URL directly
#     poster_url = data.get("Poster")

#     # Fallback if poster missing
#     if poster_url is None or poster_url == "N/A":
#         return "https://via.placeholder.com/500x750?text=No+Poster"

#     return poster_url

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        
        recommended_movie_names.append(title)
        # recommended_movie_posters.append(fetch_poster(title))

    return recommended_movie_names, recommended_movie_posters


    
movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list) 
if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(movies_list)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
