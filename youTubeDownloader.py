from pytubefix import YouTube
from sys import argv, exit
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
import os
import os.path

#Checking what type of input we are getting
vid_location = input("Are the video(s) in a file or will you insert them here, into the terminal? Answer file or terminal. \n")
save_location = input("Leave blank if you want to download the file in this directory or enter the desired path: \n") or "./"

#Creating the necessary functions for downloading the videos
def download_video(link, pathToSave, number):
    """Downloads the video file of the YT link"""
    
    yt = YouTube(link)
    print("Title: ", yt.title)
    print("Views: ", yt.views)
    ytd = yt.streams.get_highest_resolution()
    
    message = "Downloading video number " + str(number) + "..."
    print(message)
    ytd.download(pathToSave + "/videos/") 
    print("Done!")
    
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
    
    # Calculate the number of times to loop the audio if needed
    loops_required = int(video_clip.duration // audio_clip.duration) + 1
    audio_clips = [audio_clip] * loops_required

    # Make the looped audio
    looped_audio_clip = concatenate_audioclips(audio_clips)

    
    final_video = video_clip.set_audio(looped_audio_clip.subclip(0, video_clip.duration))
    print("Audio is set")
    
    output_file_name = os.path.basename(video_file).replace('.mp4', ' Final.mp4')
    output_file_path = os.path.join(path_to_save, output_file_name)
    final_video.write_videofile(output_file_path, codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)
    
    print(f"Combined video and audio file saved as {output_file_name}")
    
    # Closing the video and audio files
    audio_clip.close()
    video_clip.close()

if vid_location == "terminal":
    if len(argv) == 1:
        print("Please provide a link as an input after you run the program e.g.: ytdownloader.py www.youtube.com/...")
        
    audio_dir = save_location + "audios/"
    video_dir = save_location + "videos/"
    
    for i in range(1, len(argv)):
        link = argv[i]
        download_video(link, save_location, i)
        download_audio(link, save_location, i)
        combining_video_and_audio(audio_dir, video_dir, save_location)
    
    for filename in os.listdir(audio_dir):
        file_path = os.path.join(audio_dir, filename)
        os.unlink(file_path)
    
    for filename in os.listdir(video_dir):
        file_path = os.path.join(video_dir, filename)
        os.unlink(file_path)

elif vid_location == "file":
    file_path = input("Please input the path to the text file that contains the YT links: \n")
    if not os.path.isfile(file_path): 
        exit("The given path is not a file. Please enter a valid path.")
    
    file = open(file_path)
    video_number = 1
    
    for line in file:
        download_video(line, save_location, video_number)
        download_audio(line, save_location, video_number)
        video_number += 1
        
        audio_dir = save_location + "audios/"
        video_dir = save_location + "videos/"
        combining_video_and_audio(audio_dir, video_dir, save_location)
        
else:
    print("\nNot a valid input. Please put the YT links in a list or place them in a text file.")