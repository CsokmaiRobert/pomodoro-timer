# 🍅 Pomodoro Timer Application

The **Pomodoro Timer** is a productivity app based on the Pomodoro Technique. It helps users manage their time by alternating between work sessions and breaks. This application is built with Python's Tkinter library for a graphical interface.

## Features:
- **Timer for Work and Breaks:**
  - **Work Session:** Default duration of 25 minutes.
  - **Short Break:** Default duration of 5 minutes.
  - **Long Break:** Default duration of 20 minutes after four work sessions.
- **Visual Feedback:** Displays a tomato image with a dynamic countdown timer.
- **Checkmarks for Progress:** After each work session, a checkmark (✔) is added to track progress.
- **Start and Reset Controls:** Simple buttons to control the timer.

## 🚀 How It Works:
1. **Start Timer:** Click the "Start" button to begin a work session.
2. **Automatic Switching:** The timer alternates between work and break sessions based on the number of sessions completed:
   - After 4 work sessions, a long break is initiated.
   - After each work session, a short break is initiated.
3. **Reset Timer:** Click the "Reset" button to stop the timer and clear progress.
4. **Track Progress:** Visual checkmarks appear below the timer to represent completed work sessions.

## 🛠️ Tech Stack:
- **Python:** The main language used for this application.
- **Tkinter:** Provides the GUI framework for the app.

## Installation:
1. Clone the repository:
```bash
git clone https://github.com/yourusername/pomodoro-timer
cd pomodoro-timer

