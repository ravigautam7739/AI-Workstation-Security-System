# 🔐 AI Workstation Security System (Face Presence Detection)

A Python-based **AI security system** that monitors user presence using webcam face detection and automatically locks/shuts down the system when the authorized user leaves the workstation.

This project simulates a **smart workstation protection system** using computer vision.

---

# 🚀 Features

✔ Real-time face detection
✔ Detects user presence/absence
✔ Smart workstation monitoring
✔ Automatic shutdown when user leaves
✔ Live security status messages
✔ Webcam-based security automation

---

# 🛠 Technologies Used

* Python
* OpenCV
* Haar Cascade Face Detection
* OS module
* Time module

---

# 📂 Project Structure

```id="sec1"
ai-workstation-security-system
│
├── main.py
└── README.md
```

👉 Rename your file to **main.py** for clean structure.

---

# ⚙️ Installation

1️⃣ Install Python 3.x

2️⃣ Install required libraries:

```bash id="sec2"
pip install opencv-python
```

---

# ▶️ How to Run

```bash id="sec3"
git clone https://github.com/ravigautam7739/ai-workstation-security-system.git
cd ai-workstation-security-system
python main.py
```

---

# 🧠 How It Works

1. Webcam continuously monitors the user
2. Face detection checks if authorized user is present

### 📌 Logic:

* Face detected → System stays active

* No face detected for 2 seconds →

  ```id="sec4"
  Initiating shutdown...
  ```

* No face detected for 5 seconds →

  ```id="sec5"
  SYSTEM LOCKED
  Goodbye Boss.
  ```

3. System automatically triggers shutdown command

---

# 💻 Example Output

```id="sec6"
WELCOME BACK BOSS
Face verified. System unlocked.
```

OR

```id="sec7"
BOSS LEFT WORKSTATION
Initiating shutdown...
```

---

# 🎯 Use Cases

* Smart workstation security
* Office computer protection
* AI-based monitoring systems
* Personal desktop security
* Computer vision automation projects

---

# ⚠️ Notes

* Requires webcam
* Shutdown command works on Windows
* Good lighting improves face detection
* System may trigger if face is temporarily hidden

---

# 🔮 Future Improvements

* Face recognition for authorized users
* Lock screen instead of shutdown
* Intruder detection alerts
* Email notifications
* Multi-user authentication

---

# ⭐ Support

If you found this project useful, give it a **star ⭐**.

---

# 📱 Follow for More Projects

I regularly share **Python, AI, and automation projects**.

Stay tuned 🚀
