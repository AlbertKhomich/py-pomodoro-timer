import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
job_done = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global timer
    global job_done
    global reps

    if timer is not None:
        window.after_cancel(timer)
        title_label.config(text="Timer")
        canvas.itemconfig(timer_text, text="00:00")
        job_done = ''
        check_label.config(text="")
        reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    global job_done
    global timer

    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            job_done += "✔"
            check_label.config(text=job_done)
            window.bell()


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = tkinter.Label(fg=GREEN, text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=203, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

button_start = tkinter.Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = tkinter.Button(text="Reset", command=reset)
button_reset.grid(column=2, row=2)

check_label = tkinter.Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()
