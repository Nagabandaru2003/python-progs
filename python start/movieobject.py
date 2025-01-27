class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
        self.is_watched = False 

    def display_info(self):
        if self.is_watched:
            status = "Watched" 
        else:
            status = "Not Watched"
        print(f"Title: {self.title}, Director: {self.director}, Status: {status}")

    def mark_watched(self):
        self.is_watched = True
        print(f"{self.title} has been marked as watched.")

movie = Movie("Inception", "Christopher Nolan")

# Display the movie information
movie.display_info()

# Mark the movie as watched
movie.mark_watched()

# Display the movie information again
movie.display_info()