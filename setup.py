from setuptools import setup

with open('README.md') as f:
   readme = f.read()

setup(name = 'tkvideoaudio',
      version = '0.1',
      description = 'Python module for playing videos (without sound) inside tkinter Label widget using Pillow and imageio',
      long_description = readme,
      long_description_content_type = "text/markdown",
      classifiers = [
          'Development Status :: alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.11',
          'Topic :: Multimedia :: Video :: Display'
      ],
      keywords = 'tkvideoaudio tkinter video display label pillow imageio huskee audio pygame',      
      url = 'https://github.com/formazione/tkvideoaudio',
      author = 'Xenofon Konitsas (huskee), modified by @pythonprogrammi aka GiovanniPython on yt',
      author_email = 'konitsasx@gmail.com',
      license = 'MIT',
      packages = ['tkvideoaudio'],
      install_requires = [
          'imageio',
          'imageio-ffmpeg',
          'pillow',
          'pygame'
      ],
      include_package_data = True,
      zip_safe = False
)
