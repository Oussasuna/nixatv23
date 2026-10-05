from PIL import Image
import os

img_path = r"C:\Users\aites\.gemini\antigravity\brain\9b1825b9-be6f-4d49-80ba-5770e0652b2e\.user_uploaded\media_1791243641129.png"
img = Image.open(img_path)

os.makedirs("posters", exist_ok=True)

width, height = img.size
num_posters = 9
poster_width = width / num_posters

for i in range(num_posters):
    left = i * poster_width
    right = (i + 1) * poster_width
    poster = img.crop((left, 0, right, height))
    poster.save(f"posters/poster{i+1}.png")
