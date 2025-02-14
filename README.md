<h1>My changes to the original code</h1>

I added a way to listen to audio.
First time you run the example.py (or your script), it will create an mp3 (it needs ffmpeg installed).
Then it will play the mp3 with the audio togheter with the video using pygame (you have to pip install pygame).
Tha's all. See ya.
To install tkvideoaudio (not tkvideo) write this:

pip install tkvideoaudio@git+https://github.com/formazione/tkvideoaudio

Then use the same example:
```py
''' to install tkvideoaudio 
pip install tkvideoaudio@git+https://github.com/formazione/tkvideoaudio
'''

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
```

Change the name of the video as the name of your video, add a path if it is not in the folder
where you are working. The first time it will get the audio from the video and play it along.
The following times there will be no need to get the audio again. To get the audio it needs
ffmp, so install it, it's free and very useful to elaborate audio, video, convert formats etc.


<h1><strong>NOTE: This repository is archived as I'm no longer able to work on this project. Thanks to everyone who contributed to this.</strong></h1>
<hr></hr>
<p align="center">
  <a href="https://github.com/huskeee/tkvideo">
    <img src="https://raw.githubusercontent.com/huskeee/tkvideo/master/images/logo.png" alt="Logo" >
  </a>

  <h1 align="center">tkVideo</h1>

  <p align="center">
    Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio
    <br />

</p>

<p align = center>
	<a href="https://github.com/huskeee/tkvideo/graphs/contributors">
		<img src="https://img.shields.io/github/contributors/huskeee/tkvideo.svg?style=flat-square" alt="Contributors" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/network/members">
		<img src="https://img.shields.io/github/forks/huskeee/tkvideo.svg?style=flat-square" alt="Forks" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/stargazers">
		<img src="https://img.shields.io/github/stars/huskeee/tkvideo.svg?style=flat-squarem/huskeee/tkvideo/network/members" alt="Stargazers" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/issues">
		<img src="https://img.shields.io/github/issues/huskeee/tkvideo.svg?style=flat-square" alt="Issues" />
	</a>
	<a href="https://github.com/huskeee/tkvideo/blob/master/LICENSE">
		<img src="https://img.shields.io/github/license/huskeee/tkvideo.svg?style=flat-square" alt="MIT License" />
	</a>
</p>





<!-- ABOUT THE PROJECT -->
## About The Project

tkVideo is a Python module for playing videos in GUIs created with tkinter. It does so by binding to a `tkinter.Label` widget of the user's choice and rapidly changing its image object.


### Built With

* [tkinter (Python built-in)](https://docs.python.org/3/library/tkinter.html)
* [imageio](https://imageio.github.io)
* [Pillow](https://pypi.org/project/Pillow/)


## Installation

### End-users:

 * Clone the repo and run `setup.py`
```sh
git clone https://github.com/huskeee/tkvideo.git
python ./tkvideo/setup.py
```
or
 * Install the package from PyPI (tkvideoaudio is not on PyPI)
```sh
pip install tkvideo
```

### Developers and contributors
 * Clone the repo and install the module in developer mode
```sh
git clone https://github.com/formazione/tkvideoaudio.git
python ./tkvideoaudio/setup.py develop
```
or
 * Install the package from PyPI in editable mode (tkvideoaudio is not on PyPI)
```sh
pip install -e tkvideo
```

This will create a shim between your code and the module binaries that gets updated every time you change your code.


<!-- USAGE EXAMPLES -->
## Usage

* Import tkinter and tkvideo
* Create `Tk()` parent and the label you'd like to use
* Create `tkvideo` object with its parameters (video file path, label name, whether to loop the video or not and size of the video)
* Start the player thread with `<player_name>.play()`
* Start the Tk main loop

Example code:
```py
from tkinter import *
from tkvideo import tkvideo

root = Tk()
my_label = Label(root)
my_label.pack()
player = tkvideo("C:\\path\\to\\video.mp4", my_label, loop = 1, size = (1280,720))
player.play()

root.mainloop()
```

## Issues / suggestions

Have a problem that needs to be solved or a suggestion to make? See the [issues](https://github.com/huskeee/tkvideo/issues) page.


## License

Distributed under the MIT License. See `LICENSE` for more information.



## Contact

Xenofon Konitsas - [@huskeeeeee](https://twitter.com/huskeeeeee) - konitsasx@gmail.com

Project Link: [https://github.com/huskeee/tkvideo](https://github.com/huskeee/tkvideo)


## Special thanks to

* [@Pythonista](https://stackoverflow.com/users/5230901/pythonista) on StackOverflow for the frame loading code





##### Readme file created using [Othneil Drew's awesome template ♥](https://github.com/othneildrew/Best-README-Template)
