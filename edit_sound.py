# Soroush Ranjbar
import moviepy.editor
from colorama import Fore , Style
import os 

def extract_audio(): 
    print(f'{Fore.GREEN}Extracting audio from video please wait...')
    video = moviepy.editor.VideoFileClip('./mov/input.mp4')
    audio = video.audio
    print(f'Extracting completed.{Style.RESET_ALL}')
    return audio

def add_audio(audio): 
    print(f'{Fore.GREEN}Adding audio to compressed video file please wait...{Style.RESET_ALL}')         
    my_clip = moviepy.editor.VideoFileClip('./mov/output.mp4')
    my_clip = my_clip.set_audio(audio)
    my_clip.write_videofile('./mov/finall.mp4')
    os.remove('./mov/output.mp4')
    print(f'{Fore.GREEN}Adding completed.{Style.RESET_ALL}')
    print('====================================================')
    
