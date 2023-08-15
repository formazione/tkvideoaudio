import tkinter as tk
from tkvideoaudio import tkvideo
import pygame


root = tk.Tk()
root.title("video play")
label_video=tk.Label(root)
label_video.pack()
video_file=tkvideo("001.mp4",label_video,loop=1,size=(800,600))
video_file.play()
root.mainloop()
pygame.quit()