## Udacity-Concat

![Udacity Concat](https://github.com/victorneo/udacity-concat/raw/master/concat.png "Udacity Concat")

This is a Python script for concatenating small, individual partial lectures
downloaded from Udacity into proper lecture videos. No more lecture videos that
last for only 45 seconds!

### Requirements

You will need Python 2.7.x and `ffmpeg` installed to run this script. On macOS,
you can install `ffmpeg` using homebrew:

    brew install ffmpeg

### How to Use

Be sure to download the entire course videos from Udacity. Once videos are
downloaded, unzip them and you will be presented with a whole list of
directories, each representing one major lecture topic. 

Copy / download the `encode.py` script into the unzipped directory and run

    python encode.py

in your shell. This will begin the encoding process to generate proper lecture
videos.


### License

Copyright 2017 Victor Neo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
