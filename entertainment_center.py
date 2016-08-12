import media
import sys
import fresh_tomatoes

# creating instances of the movie class for each movie to be displayed
toy_story = media.Movie(
    "Toy Story", "Movie about a boy and his toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc", "2008"
)


little_miss_sunshine = media.Movie(
    "Little Miss Sunshine",
    "A family goes on a roadtrip to a kids beauty pageant",
    "https://upload.wikimedia.org/wikipedia/en/1/16/Little_miss_sunshine_poster.jpg",       # NOQA
    "https://www.youtube.com/watch?v=wvwVkllXT80", "2006"
)

harold_and_maude = media.Movie(
    "Harold and Maude", "An old, wise woman connects with young miserable guy",
    "https://upload.wikimedia.org/wikipedia/en/5/5f/Harold_and_Maude_%281971_film%29_poster.jpg",       # NOQA
    "www.youtube.com/watch?v=u-cOukYeGVM", "1971"
)

clueless = media.Movie(
    "Clueless", "movie and about some rich highschoolers",
    "https://upload.wikimedia.org/wikipedia/en/2/21/Clueless.jpg",
    "https://www.youtube.com/watch?v=yHDcD_xhwAo", "1995"
)

magic_mike = media.Movie(
    "Magic Mike", "movie about some strippers",
    "https://upload.wikimedia.org/wikipedia/en/6/65/Magic_Mike.jpg",
    "www.youtube.com/watch?v=Rnkv_nyKkX8", "2012"
)

league_of_their_own = media.Movie(
    "A League of their Own",
    "a movie about the 1940s woman's baseball league",
    "https://upload.wikimedia.org/wikipedia/en/5/5f/League_of_their_own_ver2.jpg",      # NOQA
    "https://www.youtube.com/watch?v=WcN392H2jx0", "1992"
)

movies = [
    toy_story, little_miss_sunshine, harold_and_maude, clueless, magic_mike,
    league_of_their_own
]


# call to open the movies page function, defined in the fresh tomatoes file
fresh_tomatoes.open_movies_page(movies)
