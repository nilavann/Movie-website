import webbrowser


class Movie():
    ''' this template is used as a blue print for the movies with specific
    details for each movie by creating an instance
    for each with movie name,story line,poster,youtube trailer'''

    # intialize variables of the movie class from the movie_trailer file

    def __init__(self, movie_name, story_line, poster_link, trailer_link, wiki_link):  # nopep8
        self.title = movie_name
        self.storyline = story_line
        self.poster_image_url = poster_link
        self.trailer_youtube_url = trailer_link
        self.wikipedia_link = wiki_link

# the function to play the youtube_trailer of the movie

    def play_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
