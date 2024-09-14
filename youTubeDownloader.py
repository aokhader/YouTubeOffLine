from pytubefix import YouTube
from sys import argv, exit
from moviepy.editor import VideoFileClip, AudioFileClip, ipython_display
import os
import os.path

#Checking what type of input we are getting
vid_location = input("Are the video(s) in a file or will you insert them here, into the terminal? Answer file or terminal. \n")
save_location = input("Leave blank if you want to download the file in this directory or enter the desired path: \n") or "./"

def download_video(link, pathToSave, number):
    """Downloads the video file of the YT link"""
    
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    ytd = yt.streams.get_highest_resolution()
    
    message = "Downloading video number " + str(number) + "..."
    print(message)
    ytd.download(pathToSave + "/videos/") 
    print("Done! \n")
    
def download_audio(link, pathToSave, number):
    """Downloads the audio file of the YT link"""
    
    yt = YouTube(link)
    audio_streams = yt.streams.filter(adaptive=True, type='audio')
    yt_audio = audio_streams[-1]
    
    message = "Downloading audio number " + str(number) + "..."
    print(message)
    yt_audio.download(pathToSave + "/audios/") 
    print("Done! \n")
    
def find_most_recent_file(directory, extension):
    """Find the most recent file with the given extension in the directory."""

    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(extension)]
    if not files:
        return None
    most_recent_file = max(files, key=os.path.getctime)
    return most_recent_file

def combining_video_and_audio(audio_path, video_path, path_to_save):
    """Combines the video and audio files into one video

    Args:
        audio_path (string): path in which the audio was saved
        video_path (string): path in which the video was saved
        path_to_save (string): path to save the final video
    """
    print("Combining audio and video...")
    audio_file = find_most_recent_file(audio_path, ".webm")
    video_file = find_most_recent_file(video_path, ".mp4")
    
    audio_clip = AudioFileClip(audio_file)
    video_clip = VideoFileClip(video_file)
    
    final_video = video_clip.set_audio(audio_clip)
    final_video.ipython_display(width = 480)
    
    output_file_name = os.path.basename(video_file).replace('.mp4', '_final.mp4')
    output_file_path = os.path.join(path_to_save, output_file_name)
    final_video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")
    
    print(f"Combined video and audio file saved as {output_file_path}")
    

if vid_location == "terminal":
    for i in range(1, len(argv)):
        link = argv[i]
        download_video(link, save_location, i)
        download_audio(link, save_location, i)
        
        audio_dir = save_location + "audios/"
        video_dir = save_location + "videos/"
        combining_video_and_audio(audio_dir, video_dir, save_location)
        
        
elif vid_location == "file":
    file_path = input("Please input the path to the text file that contains the YT links: \n")
    if not os.path.isfile(file_path): 
        exit("The given path is not a file. Please enter a valid path.")
    
    file = open(file_path)
    video_number = 1
    
    for line in file:
        download_video(line, save_location, video_number)
        video_number += 1
        
else:
    print("\nNot a valid input. Please put the YT links in a list or place them in a text file.")