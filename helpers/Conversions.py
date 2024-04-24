import moviepy.editor as mp
import os

def mp4_to_mp3(mp4_file_path):
    
    #Load MP4
    clip = mp.AudioFileClip(mp4_file_path)

    #Convert to mp3 and save
    clip.write_audiofile(mp4_file_path.replace(".mp4", "") + ".mp3")

    #Delete Mp4 File
    os.remove(mp4_file_path)


