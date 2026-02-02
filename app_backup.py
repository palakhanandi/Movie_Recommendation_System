import streamlit as st
import pickle
import pandas as pd
import requests
st.title('Movie Recommender system')
def load_css():
    with open("stle.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()


OMDB_API_KEY = "23ea0969"




def fetch_poster(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
    data = requests.get(url).json()
    
    # OMDb returns Poster URL directly
    poster_url = data.get("Poster")

    # Fallback if poster missing
    if poster_url is None or poster_url == "N/A":
        return "https://via.placeholder.com/500x750?text=No+Poster"

    return poster_url

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movie_names = []
    recommended_movie_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        
        recommended_movie_names.append(title)
        recommended_movie_posters.append(fetch_poster(title))

    return recommended_movie_names, recommended_movie_posters


    
movies = pickle.load(open('movies.pkl','rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))
selected_movie_name = st.selectbox(
    'How would you like to be contacted?',
    movies_list) 


if st.button('Recommend'):
   
    
   recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
  
   
   
 

   cols = st.columns(5)
   for i in range(5):
    with cols[i]:
        st.image(recommended_movie_posters[i], use_container_width=True)
        st.markdown(f"<p style='text-align: center; font-weight: bold;'>{recommended_movie_names[i]}</p>", unsafe_allow_html=True)





