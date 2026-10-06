import urllib.request
import re

movies = [
    'Migration',
    'The Ballad of Songbirds',
    'Aquaman and the Lost Kingdom',
    'Anyone But You',
    'Poor Things',
    'Wish',
    'Wonka',
    'Napoleon',
    'The Beekeeper'
]

for m in movies:
    url = 'https://www.themoviedb.org/search?query=' + urllib.parse.quote(m)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # match img class='poster'
        matches = re.findall(r'src="/t/p/w94_and_h141_bestv2([^"?]+)"', html)
        if matches:
            print(m, matches[0])
        else:
            print(m, 'Not found')
    except Exception as e:
        print(m, e)
