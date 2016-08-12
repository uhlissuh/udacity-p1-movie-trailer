import webbrowser


class Movie():
    """ class Movie creates a constructor for movies, allowing
        a movie name, storyline, poster image, trailer, and
        release date to be defined for an instance by variables
        passed to it.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.date = release_date
