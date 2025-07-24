import  datetime
import time
import pygame

sound="Wavy_1.mp3"

def setTime(alarm_time):
  running=True
  
  while running:
    current_time=datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    
    if current_time==alarm_time:
      print("Wake Up🎶🎶😁😁")
      pygame.mixer.init()
      pygame.mixer.music.load(sound)
      pygame.mixer.music.play()
      while pygame.mixer.music.get_busy():
         time.sleep(1)
      running=False
    time.sleep(1)    


if __name__ == "__main__":
  print(datetime.datetime.now().strftime("%H:%M:%S"))
  alarm_time=input("enter the alram time (HH:MM:SS)")
  setTime(alarm_time)