# Soroush Ranjbar
import time
import edit_sound as edit
import video_compressor as compressor
from colorama import Fore , Style
import os, sys , subprocess

def main():
    print(f'{Fore.YELLOW}Warning: Before run this program please install opencv and moviepy library.\nfor install this libraries use pip install opencv-python or moviepy{Style.RESET_ALL}')
    print('====================================================')
    time.sleep(5)
    audio = edit.extract_audio()
    width , height = compressor.specify_resolution()
    compressor.compress_video(width , height)
    edit.add_audio(audio)
    print(f'{Fore.GREEN}The compressed video file is ready.{Style.RESET_ALL}')
    if sys.platform == "win32":
        os.startfile('.\\mov\\finall.mp4')
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, './mov/finall.mp4'])

main()
