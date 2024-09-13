# YouTubeOffLine

YouTubeOffline is a Python program that will allow you to download YouTube videos and watch them on the go without having to connect to the internet. 

From the command line, you will be able to download YouTube videos by the link to the video, and it will print out details about the given video as well as download the video. You can input a list of YouTube links into the terminal directly or put them into a text file and, when prompted, input the path to the text file.

This program was originally designed to use the PyTube library, but recently there was a HTTP error that was raised by the internal servers of PyTube. To fix that PyTube recommended us to use PyTubeFix instead. As of right now, the program only downloads the video file without the audio.