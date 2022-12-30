# BMOctoprint - Octoprint + Bullseye

This is a fork of [BMOctoprint](https://katzcreates.com/portfolio/bmoctoprint). When I worked on the project, I encountered some challenges which I've addressed and wanted to share in case they are helpful to others.

## Changes I've made

- Using Raspian Bullseye
  - Running [the install script for the speakers](https://learn.adafruit.com/adafruit-speaker-bonnet-for-raspberry-pi/raspberry-pi-usage) under Raspian Buster did not work for me. Upgrading to Raspian Bullseye worked!
- OMXplayer -> `mvp` player
  - OMXplayer does not come installed on Bullseye. If you install Buster and then upgrade you will retain OMXplayer. You can also use VLC. In my case both OMXplayer and VLC had weird video issues when playing any video. I don't know if this is a codec issue or an issue with the hardware acceleration but I wasn't able to fix this. Luckily `mvp` player worked out of the box. This changes `BMOFaceButtons.py`. `mvp` player suppresses the screensaver when starting. I have found no way of disabling that so I've adjusted `screensaver.sh` to not kill the player when the `UNBLANK` signal is received. This does mean that BMO will **never** go into energy saving mode and you have to manually turn BMO off and you need to kill/minimize the video player to use the pi. I've programmed the blue button too kill the `mvp` player. If OMXplayer works for you, you should go with [the original setup](https://github.com/katzcreates/BMOctoprint).
- Removing Octoprint
  - The person this BMO is for doesn't 3d print. So I changed the functionality to:
    - Red button: play a random video from the `/home/bmo/bmointernal/videos` folder
    - Green button: play "who wants to play video games" clip and then open [knucklebones](https://knucklebones.jaredp.co.uk/)
    - Blue button: kill all `mvp` player instances and any running chrome game instance
- One script
  - This set up runs `BMOFaceButtons.py` in the background from startup to listen for button presses

<br/>
<br/>
<br/>
<br/>

Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
