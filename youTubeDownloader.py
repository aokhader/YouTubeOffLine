from pytubefix import YouTube
from sys import argv

for i in range(1, len(argv)):
    link = argv[i]
    yt = YouTube(link)

    print("Title: ", yt.title)
    print("Views: ", yt.views)

    ytd = yt.streams.get_highest_resolution()
    message = "Downloading video number " + str(i) + "..."
    print(message)
    ytd.download("./") #Change to desired path
    print("Done!")


