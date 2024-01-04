# Movie Recommendation System (Content Filtering)

## Overview
This project is a content-based movie recommendation system developed using text classification, cosine similarity, and vectorization techniques. The system allows users to input a movie and receive five similar movie recommendations based on textual features.

## Features
- **Content Filtering:** Utilizes movie descriptions, genres, and metadata for recommendation generation.
- **Cosine Similarity:** Measures textual similarity between movies for accurate recommendations.
- **Streamlit Interface:** Interactive interface for users to input movie preferences and view recommendations.
- **Jupyter Notebook:** Utilized for model development, data preprocessing, and analysis.

## Tools & Technologies
- **Python:** Language used for data processing, model development, and system implementation.
- **Jupyter Notebook:** Platform for developing and running machine learning models.
- **Streamlit:** Framework for creating the user interface.
- **TMDB Database / Kaggle:** Sources for movie-related datasets.

## Usage
1. Clone the repository: `git clone <repository-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Streamlit app: `streamlit run app.py`

## Project Structure
- `Hello.py`: Main file containing the Streamlit app code.
- `Main.ipynb`: Contains code for text classification, vectorization, and cosine similarity.
- `data/`: Directory containing datasets used for training and testing.

## How to Contribute
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-new-feature`
3. Make changes and commit: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature-new-feature`
5. Submit a pull request.
