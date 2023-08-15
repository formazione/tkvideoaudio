""" tkVideo: Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio

Copyright © 2020 Xenofon Konitsas <konitsasx@gmail.com>
Released under the terms of the MIT license (https://opensource.org/licenses/MIT) as described in LICENSE.md

"""

try:
    import Tkinter as tk  # for Python2 (although it has already reached EOL)
except ImportError:
    import tkinter as tk  # for Python3
import threading
import imageio
from PIL import Image, ImageTk
import pygame
import os
from pathlib import Path

class tkvideo():
    """ 
        Main class of tkVideo. Handles loading and playing 
        the video inside the selected label.
        
        :keyword path: 
            Path of video file
        :keyword label: 
            Name of label that will house the player
        :param loop:
            If equal to 0, the video only plays once, 
            if not it plays in an infinite loop (default 0)
        :param size:
            Changes the video's dimensions (2-tuple, 
            default is 640x360) 
    
    """
    def __init__(self, path, label, loop = 0, size = (640,360)):
        self.path = path
        self.audiofname = Path(path).stem + ".mp3"
        print(self.path)
        print(self.audiofname)
        self.label = label
        self.loop = loop
        self.size = size

    
    def load(self, path, label, loop):
        """
            Loads the video's frames recursively onto the selected label widget's image parameter.
            Loop parameter controls whether the function will run in an infinite loop
            or once.
        """
        frame_data = imageio.get_reader(path)

        if loop == 1:
            while True:
                for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image
        else:
            for image in frame_data.iter_data():
                    frame_image = ImageTk.PhotoImage(Image.fromarray(image).resize(self.size))
                    label.config(image=frame_image)
                    label.image = frame_image

    def ffmeg2audio(self):
        if self.audiofname not in os.listdir():
            print("Creating audio.mp3 file. Will be done just the first time.")
            os.system(f"ffmpeg -i {self.path} {self.audiofname}")
            print("Getting audio from video to play it together.")

    def audio(self):
        self.ffmeg2audio()
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(self.audiofname)
        pygame.mixer.music.play()

    def play(self):
        """
            Creates and starts a thread as a daemon that plays the video by rapidly going through
            the video's frames.
        """
        thread = threading.Thread(target=self.load, args=(self.path, self.label, self.loop))
        thread.daemon = 1
        thread.start()
        thread2 = threading.Thread(target=self.audio, args=(""))
        thread2.daemon = 2
        thread2.start()
