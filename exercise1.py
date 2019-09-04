romantic_movie1 = (
    'The Princess Bride', 1987, 98,
    'The story of a man and a woman who lived happily ever after.',
    ['Buttercup', 'Westley', 'Fezzik', 'Inigo Montoya', 'Vizzini']
)

romantic_movie2 = (
    'Groundhog Day', 1993, 101,
    "He's having the day of his life… over and over again.",
    ['Phil Connors']
)

romantic_movie3 = (
    'Amélie', 2001, 122,
    'One person can change your life forever.',
    ['Amélie Poulain', 'Nino Quincampoix', 'The Garden Gnome']
)

romantic_movie_list = [romantic_movie1, romantic_movie2, romantic_movie3]

print('Here are my favorite romance movies:\n')
for movie in romantic_movie_list:
    print(movie[0], ' (', movie[1], '): ', movie[3], '\n', sep='')
