import streamlit as st
import pickle
import requests

movies= pickle.load(open('models/movies_list.pkl','rb'))
similarity= pickle.load(open('models/similarity.pkl','rb'))

st.header("Movie Recommender System")
movies_list=movies['title'].values
selectValue= st.selectbox('Select a movie',movies_list)

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=4a2abb24649bbaad9b1aef2720bea69f&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    popularity=data['popularity']
    poster_path=data['poster_path']
    full_path="https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path,popularity

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance= sorted(list(enumerate(similarity[index])),reverse=True,key=lambda vector: vector[1])
    recommend_movie=[]
    recommend_poster=[]
    recommend_popularity=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append((movies.iloc[i[0]].title))
        poster,popularity=fetch_poster(movies_id)
        recommend_poster.append(poster)
        recommend_popularity.append(popularity)

    return recommend_movie,recommend_poster,recommend_popularity
if(st.button("Show Recommended movies")):
    movie_name, movie_poster, movie_poularity=recommend(selectValue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
        st.text("Popularity: \n"+str(movie_poularity[0]))
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
        st.text("Popularity: \n"+str(movie_poularity[1]))
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
        st.text("Popularity: \n"+str(movie_poularity[2]))
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
        st.text("Popularity: \n"+str(movie_poularity[3]))
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
        st.text("Popularity: \n"+str(movie_poularity[4]))
#4a2abb24649bbaad9b1aef2720bea69f
# https://api.themoviedb.org/3/movie/550?api_key=0a2e9d0b9b0b3b9b3b9b3b9b3b9b3b9b&language=en-US