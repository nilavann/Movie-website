# import user defined templates

import template
import fresh_tomatoes

# creating instance for class Movie with movie details movie_name,story line
# poster_img url,trailer link,wikipedia link

imsai_arasan = template.Movie("Imsai Arasan 23rd Pulikecei",
                "The King of Torture, Pulikecei the 23rd,A foolish king and his brave brother",  # nopep8
                "https://upload.wikimedia.org/wikipedia/en/f/f0/Imsai_Arasan_23am_Pulikesi_poster.jpg",  # nopep8
                "https://www.youtube.com/watch?v=IiimrNEaZAo",
                "https://en.wikipedia.org/wiki/Imsai_Arasan_23rd_Pulikecei"
                )
thirudan_police = template.Movie("Thirudan Police",
                    "Son investigating father murder",
                    "http://tamilmp3free.com/up_images/Thirudan%20Police.jpg",  # nopep8
                    "https://www.youtube.com/watch?v=kL6GnnCSkhg",
                    "https://en.wikipedia.org/wiki/Thirudan_Police"
                    )
mundasupatti = template.Movie("Mundasupatti",
                    "Photographer and superstitious village",
                    "https://madaboutmoviez.files.wordpress.com/2014/04/mundasupatti.jpg?w=240&h=300",  # nopep8
                    "https://www.youtube.com/watch?v=J0dgeT4jBZg",
                    "https://en.wikipedia.org/wiki/Mundasupatti"
                    )
naan_mahaan_alla = template.Movie("Naan Mahaan Alla",
                    "An younster realise whats a real life",
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQh_PCl94AEcKu0Tqx5-yzk91JjwxePQipfBjrnTGObAFu5dbIs",  # nopep8
                    "https://www.youtube.com/watch?v=TmQNqPefB-k",
                    "https://en.wikipedia.org/wiki/Naan_Mahaan_Alla_(2010_film)")  # nopep8
raja_rani = template.Movie("Raja Rani",
                    "A Romantic love film",
                    "http://a10.gaanacdn.com/images/albums/34/266034/crop_175x175_266034.jpg",  # nopep8
                    "https://www.youtube.com/watch?v=q6hMWYND4jQ",
                    "https://en.wikipedia.org/wiki/Raja_Rani_(2013_film)"
                    )
thani_oruvan = template.Movie("Thani Oruvan",
                    "A young police office investigation",  # nopep8
                    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGgd_pC2MMq0TLg7pGUtceNSPhszYyACk9n06iuLrz8WG46OAmEg",  # nopep8
                    "https://www.youtube.com/watch?v=r5Lih8rKd6k",
                    "https://en.wikipedia.org/wiki/Thani_Oruvan"
                    )

# create a list with all movie names

movie_list = [
    thani_oruvan, raja_rani, imsai_arasan,
    thirudan_police, mundasupatti, naan_mahaan_alla
]

# passung movies name list to a method in fresh_tomatoes

fresh_tomatoes.open_movies_page(movie_list)
