import webbrowser

class Video():
    """For different typeds of video"""
    def __init__(self, title, plot, duration):
        self.title = title
        self.plot = plot
        self.duration = duration
    

class Movie(Video):
    """A class for storing movies info"""
    VALID_RATINGS = ["G", "PG", "PG13", "R"]
    
    def __init__(self, title, plot, duration, poster_image, trailer_youtube):
        Video.__init__(self, title, plot, duration)
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TVSeries(Video):
    """A class for storing tv info"""
    
    def __init__(self, title, plot, duration, poster_image, netflix_link):
        Video.__init__(self, title, plot, duration)
        self.poster_image_url = poster_image
        self.netflix_link = netflix_link

 #   def open_netflix(self):
#        webbrowser.open(self.netflix_link)
