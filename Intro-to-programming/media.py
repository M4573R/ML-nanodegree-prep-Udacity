
import webbrowser
class Movie():
    """This module does some random shit related to movies. Yo!"""
    valid_ratings = ["G","PG","PG-13","R"]
    def __init__(self,movie_title,movie_storyline,movie_image,movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url  = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
