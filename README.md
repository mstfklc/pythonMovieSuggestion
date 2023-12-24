# Movie Recommendation System

This project aims to create a movie recommendation system using movie data on TMDb (The Movie Database). The project was developed using the Python programming language and scikit-learn library.

## Used technologies

- **Python**: The project is written in the Python programming language.
- **Pandas**: It was used for data manipulation and analysis.
- **scikit-learn**: Similarity measurements were made using algorithms such as TfidfVectorizer and linear_kernel.

## How does it work?

1. First, the movie data from TMDb (`tmdb_5000_credits.csv` and `tmdb_5000_movies.csv`) is read using the Pandas library.
2. Data sets are merged and unnecessary columns are purged.
3. Using TfidfVectorizer on the "overview" column, English stop words (the, a, an, etc.) and similar words are cleared.
4. Cosine similarity is calculated and the similarity matrix is ​​created.
5. By taking a movie name from the user, the movies most similar to this movie are listed and printed on the screen.

## Usage

1. If Python is not installed, [From Python's official website](https://www.python.org/downloads/) Download and install Python.
2. Enter these commands in the terminal or command prompt to install the required libraries:
    ```bash
    python3 -m pip install scikit-learn
    ```
4. Run the program by entering the following command in the terminal or command prompt in the project directory:
    ```bash
    python3 movieSuggestion.py
    ```
5. Enter a movie name according to the on-screen instructions and see movie recommendations.

This project offers movie buffs a guide to discover movies of similar genres.
