from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
html_content = conn.read()

soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid")
div = section.find("div","section-content")
ul = div.find("ul")

li_list = ul.find_all("li")
li = li_list[0]

top_song = []
for li in li_list:
    h3 = li.h3
    a = h3.a
    h4 = li.h4
    b = h4.a
    title = a.string.strip()
    author = b.string.strip()
    songs = OrderedDict({
        "Title" : title,
        "Author" : author
    })
    print(title+" "+author)
    options = {
        'default_search': 'ytsearch',
        'max_downloads': 10,
        'format': 'bestaudio/audio'
    }
    dl = YoutubeDL(options)
    dl.download([title + " " + author])

    top_song.append(songs)

pyexcel.save_as(records=top_song,dest_file_name="Top_song.xlsx")