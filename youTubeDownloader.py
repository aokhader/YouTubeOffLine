from pytubefix import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

ytd = yt.streams.get_highest_resolution()
print("Downloading video...")
ytd.download("./")
print("Done!")
