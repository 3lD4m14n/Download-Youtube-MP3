import os
from pytube import YouTube
from moviepy.editor import *

def download_audio(url, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Download YouTube video
    youtube = YouTube(url)
    video = youtube.streams.filter(only_audio=True).first()
    video.download(output_folder)

    # Convert video file to MP3 audio
    video_file = os.path.join(output_folder, video.default_filename)
    mp3_file = os.path.splitext(video_file)[0] + '.mp3'
    video_clip = AudioFileClip(video_file)
    video_clip.write_audiofile(mp3_file)

    # Remove the original video file
    os.remove(video_file)

    print(f"The audio has been successfully downloaded to: {mp3_file}")

# Output folder for the audio file
output_folder = "/home/ddmc/Música/"
while True:
    # YouTube video URL
    url = input("Enter the YouTube video URL or 0 to exit: ")

    if url == 0:
        break

    # Call the function to download the audio
    download_audio(url, output_folder)
