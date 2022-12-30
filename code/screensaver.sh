#!/bin/bash
process() {
while read input; do
	case "$input" in
		# UNBLANK*) killall mpvs ;;
		BLANK*) DISPLAY=:0 mpv --fs --loop --no-osc /home/bmo/bmointernal/animation/BMO_Idle_loop_ColorAdjust.mp4 & ;;
	esac
done
}

/usr/bin/xscreensaver-command -watch | process
