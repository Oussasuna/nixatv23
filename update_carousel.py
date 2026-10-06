import re

paths = [
    '/ldfUBqhfS73Xn7F7h2jG54o0rM2.jpg', # Migration
    '/mBaXZeBW2ZQiT5k2aK2xJpM4x3H.jpg', # Hunger Games
    '/jcA2QFJ4wuFcG79P97wA7OBLQoL.jpg', # Aquaman
    '/5qHoazZiaLe7oFBok7XlUhg96f2.jpg', # Anyone But You
    '/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg', # Poor Things
    '/ehumsuIBbgAe1hg343oszCLrAfI.jpg', # Wish
    '/qhb1qRIqHapYftV2vaVhi1T2k0T.jpg', # Wonka
    '/vcZWJGvB5xydWuUO1vaTLI82tGi.jpg', # Napoleon
    '/A7EByudXoE54yE0q4jG3H7g8Y47.jpg'  # Beekeeper
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The user wants 4k, let's use w780 or original. Let's use w780 for good quality
urls = [f'https://image.tmdb.org/t/p/original{p}' for p in paths]

for i in range(9):
    content = content.replace(f'src="posters/poster{i+1}.png"', f'src="{urls[i]}"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

