import streamlit as st
import pickle
import pandas as pd
import numpy as np


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    # we need to store the index and movie, so we will use enumerate function
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
       movie_id = i[0]
       # fetch poster from this movie id using API

       recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


similarity = pickle.load(open('similarity.pkl', 'rb'))
movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))

movies = pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Choose a Movie', movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)




