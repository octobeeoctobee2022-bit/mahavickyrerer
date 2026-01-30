import webbrowser
import os

keywords = [
    "wireless mouse",
    "bluetooth headphones",
    "gaming keyboard"
]

index_file = "kw_index.txt"

if os.path.exists(index_file):
    with open(index_file, "r") as f:
        index = int(f.read())
else:
    index = 0

keyword = keywords[index]
next_index = (index + 1) % len(keywords)

with open(index_file, "w") as f:
    f.write(str(next_index))

google_url = f"https://www.google.com/search?q={keyword.replace(' ', '+')}"
amazon_url = f"https://www.amazon.in/dp/B0FNKL3QVH?keywords={keyword.replace(' ', '+')}"

webbrowser.open_new(google_url)
webbrowser.open_new(amazon_url)
