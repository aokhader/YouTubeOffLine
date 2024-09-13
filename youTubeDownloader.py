from pytubefix import YouTube
from sys import argv
import os.path
import sys

def download_video(link, pathToSave, number):
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    ytd = yt.streams.get_highest_resolution()
    
    message = "Downloading video number " + str(number) + "..."
    print(message)
    ytd.download(pathToSave) 
    print("Done! \n")

#Checking what type of input we are getting
vid_location = input("Are the video(s) in a file or will you insert them here, into the terminal? Answer file or terminal. \n")
path_to_save = input("Leave blank if you want to download the file in this directory or enter the desired path: \n") or "./"

if vid_location == "terminal":
    for i in range(1, len(argv)):
        link = argv[i]
        download_video(link, path_to_save, i)
        
elif vid_location == "file":
    file_path = input("Please input the path to the text file that contains the YT links: \n")
    if not os.path.isfile(file_path): 
        sys.exit("The given path is not a file. Please enter a valid path.")
    
    file = open(file_path)
    video_number = 1
    
    for line in file:
        download_video(line, path_to_save, video_number)
        video_number += 1
        
else:
    print("\nNot a valid input. Please put the YT links in a list or place them in a text file.")