import streamlit as st
import pickle
import pandas as pd
#To hit api we need requests module
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7adc9dd206737259b5e17dd07f49b062&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(user_movie):
    movie_index = movies[movies['title'] == user_movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        #this movie _id is used to fetch poster of movies using api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster
        
movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)      

similarity = pickle.load(open('similarity.pkl','rb'))  

st.title('Movie Recommender System')

#user_movie = st.text_input('Movie title 👇')
user_movie = st.selectbox('Movie title 👇', movies['title'])

#making button
if st.button('RECOMMEND'):
    names, posters= recommend(user_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])    
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])