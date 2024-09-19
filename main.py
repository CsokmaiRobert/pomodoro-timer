from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
clicked = 0
reps = 0
timer = None

def restart_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    global reps
    reps = 0
    global clicked
    clicked = 0

def start_timer():
    global clicked
    clicked += 1

    if clicked == 1:
        global reps
        reps += 1

        work_secs = WORK_MIN * 60
        short_break_secs = SHORT_BREAK_MIN * 60
        long_break_secs = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_secs)
            timer_label.config(text="Break", fg=RED)
        elif reps % 2 == 0:
            count_down(short_break_secs)
            timer_label.config(text="Break", fg=PINK)
        else:
            count_down(work_secs)
            timer_label.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            marks = ""
            for _ in range(math.floor(reps / 2)):
                marks += "✔"
            checkmark.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=restart_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(column=1, row=3)


window.mainloop()