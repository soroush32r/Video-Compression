# Soroush Ranjbar
import cv2
from colorama import Style , Fore

def video_resoultion() :
    cap = cv2.VideoCapture('./mov/input.mp4')
    ret, frame = cap.read()
    width  = int(cap.get(3)) 
    height = int(cap.get(4))
    print('====================================================')
    print('Your video resolution is :' , width , '*' , height) 
    return width , height


def specify_resolution():
    video_width , video_height = video_resoultion()
    while True:
        print('Please enter your suggested resolution')
        width = int(input('Enter width  >> ') or '%d' %(video_width / 2))
        height = int(input('Enter height >> ') or '%d' %(video_height / 2))
        if width > video_width and height < video_height :
            word = 'width'
        elif width < video_width and height > video_height :
            word = 'height'
        elif width > video_width and height > video_height :
            word = 'width and height'
        else :
            break
        print(f'{Fore.RED}Warning: The entered %s is bigger than video file %s. Continue?{Style.RESET_ALL}' %(word , word))
        cont = input('[Y]es or [N]o >> ')
        if cont == 'Y' or cont == 'y' :
            break
        else :
            continue    
    print('Suggested resulotion is :', width , '*', height)
    print('====================================================')
    return width , height


def compress_video(width,height):  
  cap = cv2.VideoCapture('./mov/input.mp4')
  fps = cap.get(cv2.CAP_PROP_FPS)
  print('The video file fps is :' , fps)

  fourcc = cv2.VideoWriter_fourcc(*'mp4v')
  out = cv2.VideoWriter('./mov/output.mp4',fourcc, fps, (width,height))
  print(f'{Fore.GREEN}Video file compression started please wait...{Style.RESET_ALL}')
  while True:
      ret, frame = cap.read()
      if ret == True:
          b = cv2.resize(frame,(width,height),fx=0,fy=0, interpolation = cv2.INTER_LANCZOS4)
          out.write(b)
      else:
          break
      
  cap.release()
  out.release()
  cv2.destroyAllWindows()
  print(f'{Fore.GREEN}Compression completed{Style.RESET_ALL}')
  print('====================================================')
