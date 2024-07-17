from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#379b46"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_after = None
start_tracker = 0

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Resets the timer to zero"""
    global reps,start_tracker
    window.after_cancel(timer_after)
    reps = 0
    canvas.itemconfig(timer_canvas, text='00:00')
    change_state_text('Work')
    check_mark.config(text='')
    start_tracker = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def change_state_text(new_text, color=GREEN):
    """Changes text of the current (i.e. Work,Break and long break)\n Takes name of current state and optional
    argument as color"""
    timer_text.config(text=new_text, fg=color)


def start_timer():
    """Starts the timer"""
    # Countdown Call
    global reps,start_tracker
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    start_tracker+=1

    if start_tracker == 1:
        # count_down(1 * 60)
        # Work time
        if reps % 2 != 0:
            count_down(work_sec)
            change_state_text('Work')
        #Long break Time
        elif reps == 8:
            count_down(long_break_sec)
            change_state_text('Break', RED)

        # Short break time
        else:
            count_down(short_break_sec)
            change_state_text('Break', PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(starting_time):
    """ Starts the countdown """
    # time_in_sec = starting_time * 60
    minute_hand = math.floor(starting_time / 60)
    second_hand = starting_time % 60

    # if second_hand == 0:
    #     second_hand = "00"
    if second_hand < 10:
        second_hand = f'0{second_hand}'
    canvas.itemconfig(timer_canvas, text=f'{minute_hand}:{second_hand}')

    if starting_time > 0:
        global timer_after
        timer_after = window.after(1000, count_down, starting_time - 1)
    else:
        start_timer()
        num_of_checkmarks = math.floor(reps / 2)
        check_mark.config(text=f"{'✔' * num_of_checkmarks}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Tomato Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=tomato_img)
timer_canvas = canvas.create_text(102, 133, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Timer text
timer_text = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer_text.grid(column=1, row=0)

# Start Button
start_button = Button(text='Start', font=(FONT_NAME, 12, 'bold'), command=start_timer)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = Button(text='Reset', font=(FONT_NAME, 12, 'bold'), command=reset_timer)
reset_button.grid(column=2, row=2)

# Check Mark
check_mark = Label(font=(FONT_NAME, 12, 'bold'), fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
