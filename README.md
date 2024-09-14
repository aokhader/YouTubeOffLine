# YouTubeOffLine

YouTubeOffline is a Python program that will allow you to download YouTube videos and watch them on the go without having to connect to the internet. 

From the command line, you will be able to download YouTube videos by the link to the video, and it will print out details about the given video as well as download the video. You can input a list of YouTube links into the terminal directly or put them into a text file and, when prompted, input the path to the text file.

This works by creating a temporary directory for the audio and video streams and accessing the most recent one, which would be the current input's video and audio streams. Once accessed, it creates a video and audio clip using the streams and sets the video's audio to be the audio stream. Finally, it creates the final video and adds the tag "Final" in the end to signify the final version.

To play the final video, play it using a video player for MP4 files e.g. Media Player for Windows.

## References

This program was originally designed to use the PyTube library, but recently there was a HTTP error that was raised by the internal servers of PyTube. To fix that PyTube recommended us to use PyTubeFix instead. As of right now, the program only downloads the video file without the audio.

To fix the audio issue, I had to get the audio file on its own and combine the video and audio files using MoviePy, a Python library for video editing.