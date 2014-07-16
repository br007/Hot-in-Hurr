Hot-in-Hurr
===========

A program that plays nelly's hot in hurrr using a raspberry pi, temperature sensor and the hot in hurrr mp3

Make sure to change the song name in line to match your mp3 on line 55












Known Issues:

1. I have been noticing issues, where the pygame module will not play music and describe that
  
  
  
  File "hotinhurr.py", line 54, in <module>
    pygame.mixer.init()
pygame.error: No available audio device


Upon a reboot, the music begins to work again.
