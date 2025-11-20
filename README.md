<h1 align="center">🛡️ Tracking Pixel SOC Lab</h1>

<p align="center">
  <b>Defensive Email Telemetry • Blue Team Lab • Flask + Python</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Blue%20Team-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/badge/Tech-Python%20%7C%20Flask-informational?style=for-the-badge">
  <img src="https://img.shields.io/badge/Topic-Email%20Security-important?style=for-the-badge">
</p>

---

## 🌐 Overview

This lab simulates a **legitimate corporate security email** that contains a **1×1 tracking pixel**.  
The goal is to understand, from a defender’s perspective, how:

- A tracking pixel collects metadata (IP, User-Agent, timestamp, campaign parameters, referer)
- A backend server logs these events
- A SOC dashboard visualizes them in near real time

> This project is strictly **defensive**, **educational**, and runs in a **controlled environment**.

---

## 📚 Table of Contents

1. [Architecture & Workflow](#-architecture--workflow)
2. [Screenshots (Evidence)](#-screenshots-evidence)
3. [Implementation Steps](#-implementation-steps)
4. [Project Structure](#-project-structure)
5. [Skills Demonstrated](#-skills-demonstrated)
6. [Final Notes](#-final-notes)

---

## 🧩 Architecture & Workflow

```text
                 ┌──────────────────────────┐
                 │      Gmail / Browser      │
                 │  (user opens real email)  │
                 └─────────────┬────────────┘
                               │
                               ▼
                   ┌────────────────────────┐
                   │   HTML Email + Pixel   │
                   │ <img src="pixel.gif">  │
                   └─────────────┬──────────┘
                               │
                               ▼
         ┌──────────────────────────────────────────┐
         │           Flask Tracking Server           │
         │  /pixel.gif receives telemetry:           │
         │   • IP address                            │
         │   • User-Agent                            │
         │   • Timestamp (UTC)                       │
         │   • Query parameters (user, campaign)     │
         └──────────────┬───────────────────────────┘
                        │
                        ▼
            ┌─────────────────────────┐
            │     logs/events.jsonl   │
            │ (JSON Lines structured) │
            └─────────────┬──────────┘
                          │
                          ▼
        ┌────────────────────────────────┐
        │    SOC Dashboard (/dashboard)  │
        │  Auto-refresh every 5 seconds  │
        │   Shows all tracking events    │
        └────────────────────────────────┘

High-level workflow:

1. A real HTML email is sent to the user’s inbox.


2. When the user opens the email and images load, the email client requests /pixel.gif.


3. The Flask server logs the request into logs/events.jsonl.


4. The SOC dashboard reads this log and displays all pixel events in a table.




---

📸 Screenshots (Evidence)

1️⃣ Local HTML Email Preview

Local rendering of email.html to verify design and pixel embedding:




---

2️⃣ Real Email Delivered to Gmail

The same HTML email delivered to Gmail using Python + Gmail SMTP:




---

3️⃣ Flask Server Homepage

Simple landing page at http://127.0.0.1:5000/ confirming that the app is running:




---

4️⃣ Flask Terminal Logs

Terminal views showing the Flask development server and HTTP requests being processed
(including the email open and pixel hit):






---

🛠 Implementation Steps

This section documents the full workflow used to build and run the lab.


---

1️⃣ Create Lab Environment

mkdir tracking-pixel-soc-lab
cd tracking-pixel-soc-lab
python3 -m venv venv
source venv/bin/activate
pip install flask


---

2️⃣ Create the 1×1 Tracking Pixel

A minimal transparent GIF is generated using a single shell command:

printf '\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B' > 1x1.gif

File produced: 1x1.gif


---

3️⃣ Flask Tracking Server (app.py)

Core responsibilities:

GET /pixel.gif

Returns 1x1.gif

Logs each request (IP, User-Agent, timestamp, query parameters, referer)

Appends entries to logs/events.jsonl in JSON Lines format


GET /dashboard

Reads events.jsonl

Displays events in a table (latest on top)

Auto-refreshes using a short JavaScript timer


GET /

Minimal home page to confirm the app is running



Run the server:

python3 app.py

The server listens on:

http://127.0.0.1:5000/



---

4️⃣ SOC Dashboard (templates/dashboard.html)

The dashboard:

Shows event fields: timestamp, IP, User-Agent, referer, params

Uses simple CSS for a clean SOC-style table

Includes an auto-refresh script (setTimeout) to reload every few seconds


This emulates a lightweight analyst console for monitoring pixel activity.


---

5️⃣ Corporate Security Email (email.html)

The email template:

Styled as a modern security notification

Includes a header, body text, and footer

Addressed personally to the recipient

Contains the tracking pixel at the bottom


The crucial element is the pixel tag:

<img 
  src="http://127.0.0.1:5000/pixel.gif?user=ahmed&campaign=email-test"
  width="1"
  height="1"
  style="display:none;"
  alt=""
/>

When the email client loads images, this request triggers an entry in the logs and dashboard.


---

6️⃣ Sending a Real Email (send_email.py)

To simulate a realistic scenario, the HTML email is sent using Python and Gmail SMTP:

Uses smtplib.SMTP_SSL("smtp.gmail.com", 465)

Authenticates using a Gmail App Password (not stored in this repository)

Reads the body from email.html

Sends the email from and to the same account for safe local testing


Command:

python3 send_email.py


---

7️⃣ Opening the Email → Pixel Fires

End-to-end flow:

1. Start Flask server (python3 app.py).


2. Open Gmail and view the delivered email.


3. When images load, Gmail requests:

/pixel.gif?user=ahmed&campaign=email-test


4. Flask logs the event in logs/events.jsonl.


5. /dashboard shows the new entry with all captured fields.



This demonstrates, in a controlled environment, how email tracking works in practice.


---

📂 Project Structure

tracking-pixel-soc-lab/
│
├── app.py                 # Flask tracking server + dashboard routes
├── email.html             # Corporate-style security email with pixel
├── send_email.py          # Python script to send the email via Gmail SMTP
├── 1x1.gif                # 1×1 transparent tracking pixel
│
├── logs/
│   └── events.jsonl       # JSONL log of all pixel hits
│
├── templates/
│   └── dashboard.html     # SOC dashboard (auto-refreshing)
│
├── evidence/              # Screenshots used in this README
│   ├── dashboard.png
│   ├── emil_preview.png
│   ├── gmail.png
│   ├── terminal1.png
│   └── terminal2.png
│
└── README.md


---

🧠 Skills Demonstrated

Email security & tracking analysis

Flask-based defensive tooling

SOC dashboard design & log visualization

JSONL logging pipelines

Safe telemetry collection in a controlled lab

Use of Gmail SMTP + App Passwords for secure automation

Clear documentation and evidence-based lab reporting



---

🏁 Final Notes

This project reproduces real-world tracking pixel behavior using a fully legal, local, and defensive setup.
It is suitable for:

Security internships

SOC / Blue Team roles

Cloud Security portfolios

Detection engineering practice

Email security demonstrations and workshops


<p align="center">
  <b>Author:</b> Ahmed Tarek – Blue Team & Cloud Security 
</p>
```
