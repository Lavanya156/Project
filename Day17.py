class Movie:
    def __init__(self, title):
        self.title = title
        self.ratings = []
    def add_rating(self, rating):
        self.ratings.append(rating)
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class MovieRatingSystem:
    def __init__(self):
        self.movies = {}
    def add_movie(self, title):
        if title not in self.movies:
            self.movies[title] = Movie(title)
            print(f"Movie '{title}' added successfully.")
        else:
            print(f"Movie '{title}' already exists.")
    def rate_movie(self, title, rating):
        if title in self.movies:
            self.movies[title].add_rating(rating)
            print(f"Rating {rating} added to movie '{title}'.")
        else:
            print(f"Movie '{title}' not found.")
    def display_average_ratings(self):
        if not self.movies:
            print("No movies found.")
            return
        print("\nAverage Ratings:")
        for title, movie in self.movies.items():
            avg_rating = movie.average_rating()
            print(f"{title}: {avg_rating:.2f}")

# Example Usage:
movie_system = MovieRatingSystem()

while True:
    print("\nMovie Rating System Menu:")
    print("1. Add Movie")
    print("2. Rate Movie")
    print("3. Display Average Ratings")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        title = input("Enter movie title: ")
        movie_system.add_movie(title)

    elif choice == '2':
        title = input("Enter movie title: ")
        rating = float(input("Enter rating (0-10): "))
        movie_system.rate_movie(title, rating)

    elif choice == '3':
        movie_system.display_average_ratings()

    elif choice == '4':
        print("Exiting Movie Rating System. Thank You!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")