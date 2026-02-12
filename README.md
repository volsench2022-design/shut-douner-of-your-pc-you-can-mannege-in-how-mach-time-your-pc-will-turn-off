🖥️ Shutdown / Restart Scheduler (Python Tkinter)

<img width="512" height="474" alt="Screenshot 2026-02-12 161730" src="https://github.com/user-attachments/assets/cdc32039-3fba-466d-a922-3ffa29ed6d97" />
A simple and user-friendly desktop application built with Python and Tkinter that allows users to schedule a system shutdown or restart with a countdown timer.

This tool provides a clean GUI interface to control Windows shutdown commands safely and conveniently.

🚀 Features

⏳ Schedule system shutdown with custom timer (seconds)

🔄 Schedule system restart

❌ Cancel scheduled shutdown/restart instantly

📊 Real-time countdown display inside the app

📂 Quick access to project folder

👤 Displays current system user and OS

🎨 Clean dark-themed interface

🛠️ Built With

Python 3

Tkinter (GUI)

os module (System commands)

💻 How It Works

The application uses Windows system commands:

shutdown /s /t <seconds> → Shutdown after specified time

shutdown /r /t <seconds> → Restart after specified time

shutdown /a → Cancel scheduled operation

A Tkinter-based countdown timer runs alongside the system timer for real-time UI feedback.

📦 Installation & Usage

Make sure Python 3 is installed.

Clone this repository:

git clone https://github.com/yourusername/your-repository-name.git


Navigate into the project folder:

cd your-repository-name


Run the script:

python your_script_name.py

⚠️ Important Notes

This application is designed for Windows OS only.

Administrator permissions may be required for shutdown commands.

Always save your work before scheduling a shutdown.

🎯 Future Improvements (Optional Ideas)

Add hours & minutes input instead of only seconds

Add system tray support

Add sound notification before execution

Add Linux/macOS support

📄 License

This project is open-source and available under the MIT License.
