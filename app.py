import os
import sys
import pickle
import streamlit as st
import numpy as np
from books_recommender.logger.log import logging
from books_recommender.config.configuration import AppConfiguration
from books_recommender.pipeline.training_pipeline import TrainingPipeline
from books_recommender.exception.exception_handler import AppException

# Apply custom CSS for enhanced styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(to right, #ece9e6, #ffffff);
            font-family: 'Recoleta', sans-serif;
        }
        .main-title {
            font-size: 48px;
            text-align: center;
            margin-bottom: 20px;
            color: #333;
        }
        .centered-button {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }
        @keyframes rainbow-border {
            0% { border-color: red; }
            14% { border-color: orange; }
            28% { border-color: yellow; }
            42% { border-color: green; }
            57% { border-color: blue; }
            71% { border-color: indigo; }
            85% { border-color: violet; }
            100% { border-color: red; }
        }
        .stButton button {
            background-color: #ffffff; /* White background */
            color: #000000; /* Black text color */
            padding: 8px 20px; /* Reduced padding for smaller button */
            font-size: 14px; /* Smaller font size */
            border-radius: 8px; /* Slightly smaller border radius */
            border: 2px solid; /* Border with default color */
            border-image: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet, red);
            border-image-slice: 1;
            animation: rainbow-border 5s infinite;
            box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1); /* Smaller shadow */
            transition: background-color 0.3s, box-shadow 0.3s;
        }
        .stButton button:hover {
            background-color: #f0f0f0; /* Light grey background on hover */
            color: #000000; /* Keep text color black on hover */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
        }
        .recommendation-box {
            background-color: #f9f9f9;
            padding: 15px; /* Reduced padding */
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 20px;
            overflow-x: auto; /* Enable horizontal scrolling */
            white-space: nowrap; /* Prevent wrapping */
        }
        .recommendation-box h3 {
            color: #555;
            font-size: 24px; /* Increased font size for better visibility */
            margin-bottom: 15px; /* Space below the heading */
        }
        .recommendation-container {
            display: flex;
            flex-direction: row; /* Horizontal layout */
            justify-content: flex-start; /* Align items to the start */
            align-items: flex-start;
            gap: 15px; /* Space between book items */
            overflow-x: auto; /* Ensure the container scrolls horizontally */
            white-space: nowrap; /* Prevent line wrapping */
        }
        .recommendation-container .book-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            min-width: 120px; /* Ensure items have a minimum width */
        }
        .recommendation-container .book-item img {
            max-width: 100px; /* Set a maximum width for images */
            max-height: 140px; /* Set a maximum height for images */
            border-radius: 10px; /* Rounded corners */
        }
        .recommendation-container .book-item p {
            font-size: 16px; /* Adjusted font size for book titles */
            margin-top: 5px; /* Space between image and text */
        }
    </style>
""", unsafe_allow_html=True)


class Recommendation:
    def __init__(self, app_config=AppConfiguration()):
        try:
            self.recommendation_config = app_config.get_recommendation_config()
        except Exception as e:
            raise AppException(e, sys) from e

    def fetch_poster(self, suggestion):
        try:
            book_name = []
            ids_index = []
            poster_url = []
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            final_rating = pickle.load(open(self.recommendation_config.final_rating_serialized_objects, 'rb'))

            for book_id in suggestion:
                book_name.append(book_pivot.index[book_id])

            for name in book_name[0]:
                ids = np.where(final_rating['title'] == name)[0][0]
                ids_index.append(ids)

            for idx in ids_index:
                url = final_rating.iloc[idx]['image_url']
                poster_url.append(url)

            return poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def recommend_book(self, book_name):
        try:
            books_list = []
            model = pickle.load(open(self.recommendation_config.trained_model_path, 'rb'))
            book_pivot = pickle.load(open(self.recommendation_config.book_pivot_serialized_objects, 'rb'))
            book_id = np.where(book_pivot.index == book_name)[0][0]
            distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

            poster_url = self.fetch_poster(suggestion)

            for i in range(len(suggestion)):
                books = book_pivot.index[suggestion[i]]
                for j in books:
                    books_list.append(j)
            return books_list, poster_url

        except Exception as e:
            raise AppException(e, sys) from e

    def train_engine(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training Completed!")
            logging.info(f"Recommended successfully!")
        except Exception as e:
            raise AppException(e, sys) from e

    def recommendations_engine(self, selected_books):
        try:
            recommended_books, poster_url = self.recommend_book(selected_books)
            st.markdown('<div class="recommendation-box"><h3>You will like these:</h3>', unsafe_allow_html=True)
            st.markdown('<div class="recommendation-container">', unsafe_allow_html=True)
            for i in range(1, len(recommended_books)):
                st.markdown(f'''
                    <div class="book-item">
                        <img src="{poster_url[i]}" alt="Book Poster">
                        <p>{recommended_books[i]}</p>
                    </div>
                ''', unsafe_allow_html=True)
            st.markdown('</div></div>', unsafe_allow_html=True)
        except Exception as e:
            raise AppException(e, sys) from e


if __name__ == "__main__":
    st.markdown(
    """
    <style>
    @keyframes rainbow {
        0% { color: red; }
        14% { color: orange; }
        28% { color: yellow; }
        42% { color: green; }
        57% { color: blue; }
        71% { color: indigo; }
        85% { color: violet; }
        100% { color: red; }
    }

    .rainbow-text {
        font-family: 'Garamond', serif;
        font-size: 4.5em; /* Increased size by 50% from 3em to 4.5em */
        animation: rainbow 5s infinite;
        text-align: center;
    }
    </style>
    <h1 class="rainbow-text">BookMaven</h1>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div style="text-align: center;">
        <p>A collaborative filtering based book recommendation system!</p>
    </div>
    """, 
    unsafe_allow_html=True
    )

    obj = Recommendation()

    # Training
    if st.button('Train Recommender System', key="train", use_container_width=True):
        obj.train_engine()

    book_names = pickle.load(open(os.path.join('templates', 'book_names.pkl'), 'rb'))
    selected_books = st.selectbox(
        "Type or select a book",
        book_names)

    # Recommendation
    if st.button('Show Recommendation', key="recommend", use_container_width=True):
        obj.recommendations_engine(selected_books)
