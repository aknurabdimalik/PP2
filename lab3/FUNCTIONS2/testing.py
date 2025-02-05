

from task2 import filter_good_movies
from task3 import get_movies_by_category
from task4 import average_imdb_score
from task5 import average_imdb_score_by_category

movies = [
    {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"},
    {"name": "Hitman", "imdb": 6.3, "category": "Action"},
    {"name": "Dark Knight", "imdb": 9.0, "category": "Adventure"},
    {"name": "The Help", "imdb": 8.0, "category": "Drama"},
    {"name": "The Choice", "imdb": 6.2, "category": "Romance"},
    {"name": "Colonia", "imdb": 7.4, "category": "Romance"},
    {"name": "Love", "imdb": 6.0, "category": "Romance"},
    {"name": "Bride Wars", "imdb": 5.4, "category": "Romance"},
    {"name": "AlphaJet", "imdb": 3.2, "category": "War"},
    {"name": "Ringing Crime", "imdb": 4.0, "category": "Crime"},
    {"name": "Joking muck", "imdb": 7.2, "category": "Comedy"},
    {"name": "What is the name", "imdb": 9.2, "category": "Suspense"},
    {"name": "Detective", "imdb": 7.0, "category": "Suspense"},
    {"name": "Exam", "imdb": 4.2, "category": "Thriller"},
    {"name": "We Two", "imdb": 7.2, "category": "Romance"}
]

# Examples
# filter_good_movies
good_movies = filter_good_movies(movies)
print("Good Movies:")
for movie in good_movies:
    print(movie["name"])

# get_movies_by_category
romance_movies = get_movies_by_category(movies, "Romance")
print("\nRomance Movies:")
for movie in romance_movies:
    print(movie["name"])

# average_imdb_score
avg_score = average_imdb_score(movies)
print(f"\nAverage IMDB score: {avg_score:.2f}")

# average_imdb_score_by_category
avg_romance_score = average_imdb_score_by_category(movies, "Romance")
print(f"Average IMDB score of Romance movies: {avg_romance_score:.2f}")
