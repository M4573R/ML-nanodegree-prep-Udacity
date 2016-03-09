import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and a toy that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")



avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")



star_wars_4 = media.Movie ("Star Wars: Episode IV - A New Hope",
                            "Luke Skywalker to the rescue, or?",
                            "http://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
                            "https://www.youtube.com/watch?v=hb8kJ7F-_1s")

star_wars_6 = media.Movie("Star Wars: Episode VI - Return of the Jedi",
                           "Destruction of the Death Star",
                           "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                           "www.youtube.com/watch?v=5UfA_aKBGMc")

star_wars_5 = media.Movie("Star Wars: Episode V - Empire Strikes Back",
                          "The bumpy road to Jedi mastery",
                          "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                          "www.youtube.com/watch?v=PkEKIw0FU6Y")

gattaca = media.Movie("Gattaca",
                      "A genetically inferior man assumes the identity of a superior one in order to pursue his lifelong dream of space travel",
                      "http://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",
                      "www.youtube.com/watch?v=ZppWok6SX88")

movies = [toy_story, avatar, star_wars_4, star_wars_5, star_wars_6, gattaca]
#fresh_tomatoes.open_movies_page(movies)
print media.Movie.__doc__
print media.Movie.__name__
print media.Movie.__module__
