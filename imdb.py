import urllib.request
import re

movies = [
    ('Migration', 'tt14170364'),
    ('Hunger Games', 'tt10545296'),
    ('Wonka', 'tt11649992'),   # I know Wonka is tt11649992
    ('Beekeeper', 'tt15314262') # Beekeeper is tt15314262
]

for name, tt in movies:
    req = urllib.request.Request(f'https://www.imdb.com/title/{tt}/', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # match imdb poster
        match = re.search(r'https://m\.media-amazon\.com/images/M/[^\.]+\.jpg', html)
        if match:
            url = match.group(0)
            # Remove the sizing suffix so it's high res! e.g., ..._V1_QL75_UX190_CR0,2,190,281_.jpg -> ..._V1_.jpg
            high_res = re.sub(r'_(V1).*?\.jpg$', r'_\1_.jpg', url)
            print(name, high_res)
        else:
            print(name, 'Not found')
    except Exception as e:
        print(name, str(e))
