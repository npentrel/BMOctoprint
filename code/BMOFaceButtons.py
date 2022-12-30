from gpiozero import Button #Much easier way to interact with the GPIO
import time
import psutil
from signal import pause
from subprocess import Popen, PIPE, run
import os
import random

button_right = Button(6)
button_up = Button(16)
button_left = Button (5)
button_down = Button (25)

red_button = Button(22)
green_button = Button(27)
blue_button = Button(17)

class Player():
    mpv_idle = None
    game = None
    animation_or_episode = None
    idle_vid = "/home/bmo/bmointernal/animation/BMO_Idle_loop_ColorAdjust.mp4"

    def create_player(self):
        print("creating player")
        self.mpv_idle = Popen(["mpv", "--fs", "--no-osc", "--loop", self.idle_vid],
            stdin=PIPE, stdout=PIPE, stderr=PIPE)
        time.sleep(0.5)

    def kill_animation_or_episode_if_active(self):
        if (self.animation_or_episode):
            print(self.animation_or_episode.pid)
            self.animation_or_episode.kill()

    def check_screensaver_player(self):
        player_running = False

        for process in psutil.process_iter():
            cmdline = process.cmdline()
            if self.idle_vid in cmdline:
                player_running = True

        if not player_running:
            self.create_player()

    def killallmpv(self):
        run(["killall", "mpv"])

    def video_right(self):
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_DontSayThings_ColorAdjust.mp4"])

    def video_up(self):
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_WorryBaby_ColorAdjust.mp4"])

    def video_down(self):
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_YourHand_ColorAdjust.mp4"])

    def video_left(self):
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_WelcomeFriends_ColorAdjust.mp4"])

    def video_left(self):
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_WelcomeFriends_ColorAdjust.mp4"])

    def red_button(self):
        self.kill_animation_or_episode_if_active()
        episode = random.choice(os.listdir("/home/bmo/bmointernal/videos"))
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/AT/" + episode])

    def green_button(self):
        if (self.game):
            print(self.game.pid)
            self.game.kill()
        self.kill_animation_or_episode_if_active()
        self.check_screensaver_player()
        self.animation_or_episode = Popen(["mpv", "--fs", "--no-osc", "--really-quiet",
            "/home/bmo/bmointernal/animation/BMO_video_games.mp4"])
        time.sleep(4)
        self.game = Popen(["/usr/bin/chromium-browser", "--noerrdialogs", "--disable-infobars", "--kiosk", "https://knucklebones.jaredp.co.uk/"])
        print(self.game.pid)

    def blue_button(self):
        self.killallmpv()
        if (self.game):
            self.game.kill()
        self.game = None


p = Player()

button_right.when_pressed = p.video_right
button_up.when_pressed = p.video_up
button_down.when_pressed = p.video_down
button_left.when_pressed = p.video_left

red_button.when_pressed = p.red_button
green_button.when_pressed = p.green_button
blue_button.when_pressed = p.blue_button

pause()


