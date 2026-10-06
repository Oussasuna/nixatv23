import urllib.request
import re

movies = [
    ('Migration', 'https://en.wikipedia.org/wiki/Migration_(2023_film)'),
    ('Hunger Games', 'https://en.wikipedia.org/wiki/The_Hunger_Games:_The_Ballad_of_Songbirds_%26_Snakes'),
    ('Wonka', 'https://en.wikipedia.org/wiki/Wonka_(film)'),
    ('Beekeeper', 'https://en.wikipedia.org/wiki/The_Beekeeper_(2024_film)')
]

for name, url in movies:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        match = re.search(r'<table class="infobox[^>]*>.*?<img[^>]*src="(//upload\.wikimedia\.org/wikipedia/en/[^"]+)"', html, re.DOTALL)
        if match:
            # Get the higher res version if it's a thumbnail
            img_url = 'https:' + match.group(1).replace('/thumb/', '/')
            img_url = re.sub(r'/[^/]+$', '', img_url) if '/thumb/' in match.group(1) else img_url
            print(name, img_url)
        else:
            print(name, 'Not found')
    except Exception as e:
        print(name, str(e))
