import tkinter as tk
from tkinter import messagebox as mb
import pygame # just for playing the alarm sound
from os import path

'''

A simple timer that takes a number of seconds and counts to 0
It might be nice if it made a sound and maybe popped up an alert

'''

alarm_file = path.abspath(path.join(path.dirname(__file__), "./assets/mixkit-rooster-crowing-in-the-morning-2462.wav"))
pygame.init()
pygame.mixer.music.load(alarm_file)

BLACK = "#000000"
WHITE = "#ffffff"
FONT = "Courier"
TIMER = None
PAUSE_TIMER = None

# Timer Start

def start():
    global TIMER
    if TIMER is None:
        TIMER = parse_time(time_entry.get())
    count_down()

def parse_time(time):
    if ':' in time:
        tl = time.split(':')
        print(tl)
        if len(tl) == 3:
            seconds = (int(tl[0]) * 3600) + (int(tl[1]) * 60) + int(tl[2])
        elif len(tl) == 2:
            seconds = (int(tl[0]) * 60) + int(tl[1])
    else:
        seconds = int(time)
    print(f"Seconds: {seconds}")
    return seconds

# Timer Pause

def pause():
    count_down(True)

# Timer Reset

def reset():
    global TIMER
    TIMER = None
    timer_text.configure(text="00:00:00")
    time_entry.delete(0, 'end')

# Timer Mechanism

def count_down(pause=False):
    global PAUSE_TIMER
    global TIMER
    hours = int(TIMER / 3600)
    # if TIMER / 60 >= 60:
    #     minutes = 0
    # else:
    #     minutes = int(TIMER / 60)
    minutes = int((TIMER % 3600) / 60)
    seconds = TIMER % 60
    time_remaining = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(f"{TIMER}->{time_remaining}")
    timer_text.configure(text=time_remaining)
    if TIMER > 0 and pause is False:
        TIMER -= 1
        PAUSE_TIMER = window.after(1000, count_down)
    elif TIMER == 0 and pause is False:
        pygame.mixer.music.play()
        mb.showinfo(message="Time's up!")
        reset()
    else:
        window.after_cancel(PAUSE_TIMER)

# UI Setup
# I want to show the timer countdown, a text entry for the time, start button,
# pause button, reset button. It might be nice to be able to enter hh:mm:ss
# time format.
window = tk.Tk()
window.title("A Simple Timer")
window.configure(padx=100, pady=100)

title_label = tk.Label(text="Timer", fg=BLACK, font=(FONT, 40, "bold"))
title_label.grid(column=0, row=0, columnspan=3)

timer_text = tk.Label(text="00:00:00", font=(FONT, 35, "bold"))
timer_text.grid(column=0, row=1, columnspan=3)

time_entry = tk.Entry(width=12, font=(FONT, 18))
time_entry.grid(column=0, row=2, columnspan=3)

start_button = tk.Button(text="Start", width=6, font=(FONT, 18), command=start)
start_button.grid(column=0, row=3)

pause_button = tk.Button(text="Pause", width=6, font=(FONT, 18), command=pause)
pause_button.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", width=6, font=(FONT, 18), command=reset)
reset_button.grid(column=2, row=3)

window.mainloop()
