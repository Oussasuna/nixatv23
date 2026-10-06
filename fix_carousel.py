import re

paths = [
    '/ldfCF9RhR40mppkzmftxapaHeTo.jpg', # Migration
    '/hon92J1oqdrTwcGHXG64G2bXqrJ.jpg', # Hunger Games
    '/jcA2QFJ4wuFcG79P97wA7OBLQoL.jpg', # Aquaman
    '/5qHoazZiaLe7oFBok7XlUhg96f2.jpg', # Anyone But You
    '/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg', # Poor Things
    '/ehumsuIBbgAe1hg343oszCLrAfI.jpg', # Wish
    '/qhb1qOilapbapxWQn9jtRCMwXJF.jpg', # Wonka
    '/vcZWJGvB5xydWuUO1vaTLI82tGi.jpg', # Napoleon
    '/A7EByudX0eOzlkQ2FIbogzyazm2.jpg'  # Beekeeper
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the old URLs with the new ones
# The old ones might be broken like:
old_paths = [
    '/ldfUBqhfS73Xn7F7h2jG54o0rM2.jpg',
    '/mBaXZeBW2ZQiT5k2aK2xJpM4x3H.jpg',
    '/jcA2QFJ4wuFcG79P97wA7OBLQoL.jpg',
    '/5qHoazZiaLe7oFBok7XlUhg96f2.jpg',
    '/kCGlIMHnOm8JPXq3rXM6c5wMxcT.jpg',
    '/ehumsuIBbgAe1hg343oszCLrAfI.jpg',
    '/qhb1qRIqHapYftV2vaVhi1T2k0T.jpg',
    '/vcZWJGvB5xydWuUO1vaTLI82tGi.jpg',
    '/A7EByudXoE54yE0q4jG3H7g8Y47.jpg'
]

for i in range(9):
    content = content.replace(
        f'src="https://image.tmdb.org/t/p/original{old_paths[i]}"',
        f'src="https://image.tmdb.org/t/p/original{paths[i]}"'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
