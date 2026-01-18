import streamlit as st
import pickle


def recommend(movie):

    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


movies_df = pickle.load(open('./movies.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))

movie_titles = movies_df['title'].values

st.title("Movie Recommender System")

selected_movie_name = st.selectbox('Please select a movie', movie_titles)

if st.button('Recommend'):
    names = recommend(selected_movie_name)
    # for i in names:
    #     st.write(i)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.write(names[0])
        st.image(f"https://placehold.co/600x400?text={names[0]}")
    with col2:
        st.write(names[1])
        st.image(f"https://placehold.co/600x400?text={names[1]}")

    with col3:
        st.write(names[2])
        st.image(f"https://placehold.co/600x400?text={names[2]}")

    with col4:
        st.write(names[3])
        st.image(f"https://placehold.co/600x400?text={names[3]}")

    with col5:
        st.write(names[4])
        st.image(f"https://placehold.co/600x400?text={names[4]}")
