import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story", "A story of a boy and his toys that come to life","http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

batman_dark_knight=media.Movie("Batman Dark Knight","The Joker, a psychopath, terrorises Gotham so he can prove that even the most incorruptible people can become evil. However, Batman, Gordon and Dent stand against him.","http://www.gstatic.com/tv/thumb/movieposters/173378/p173378_p_v8_au.jpg","https://www.youtube.com/watch?v=EXeTwQWrcwY")

inception=media.Movie("Inception","Cobb steals information from his targets by entering their dreams. He is wanted for his alleged role in his wife's murder and his only chance at redemption is to perform the impossible, an inception.","http://t2.gstatic.com/images?q=tbn:ANd9GcRo9vfJCM6dzPkZHIHBVCtlJnAnew9Ai26kEdrli0-tfmatmciD","https://www.youtube.com/watch?v=8hP9D6kZseM")

lucy=media.Movie("Lucy","A woman's strength and thinking power grow exponentially after the effects of a performance-enhancing drug set in.","http://t2.gstatic.com/images?q=tbn:ANd9GcR9NUZo3YHaOwWcJ6uAqBvy2Eet5-JiFIFrke8x69h3jekrHAsY","https://www.youtube.com/watch?v=MVt32qoyhi0")

star_wars = media.Movie("Star Wars","http://ia.media-imdb.com/images/M/MV5BMTU4NTczODkwM15BMl5Ban","https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Star_Wars_Logo.svg/1200px-Star_Wars_Logo.svg.png","https://www.youtube.com/watch?v=9gvqpFbRKtQ")

avengers=media.Movie("Avengers","S.H.I.E.L.D. leader Nick Fury is compelled to launch the 'Avengers Initiative' when Loki poses a threat to planet Earth. Will Nick Fury's squad of superheroes prove themselves equal to the task?","http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s","https://www.youtube.com/watch?v=eOrNdBpGMv8")

movies=[toy_story,batman_dark_knight,inception,lucy,star_wars,avengers]
fresh_tomatoes.open_movies_page(movies)
fresh_tomatoes.create_movie_tiles_content(movies)