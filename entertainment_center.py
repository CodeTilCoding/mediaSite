import fresh_tomatoes
import media

princess_bride = media.Movie("The Princess Bride",
                        "Fencing. Fighting. Torture. Poison. True Love. Hate. Revenge. Giants. Hunters. Bad men. Good men. Beautifulest Ladies. Snakes. Spiders... Pain. Death. Brave men. Cowardly men. Strongest men. Chases. Escapes. Lies. Truths. Passion. Miracles.",
                        "98 minutes",
                        "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
                        "https://www.youtube.com/watch?v=YU_-MUJRgyQ")
#print(toy_story.storyline)

movies = [princess_bride]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)



