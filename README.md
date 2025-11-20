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

----- 
🚀 Tracking Pixel SOC Lab — Enterprise‑Grade Documentation

> A full defensive email‑telemetry lab built for SOC Analyst, DFIR, and Cloud Security Engineer portfolios.



> Designed to look like a real product README — highly visual, colorful, structured, and professionally written.




---

🧭 1. Project Overview

This project replicates a real corporate security workflow by embedding a 1×1 tracking pixel inside a security‑styled HTML email. When the receiver opens the email, the browser requests the pixel, triggering:

📡 IP telemetry collection

🧭 User‑Agent fingerprinting

🕒 Timestamp logging

🔗 Referrer capture

📨 Campaign/user parameters


All incoming events are logged into a JSONL pipeline, and displayed on a live‑updating SOC dashboard.

This README acts as an enterprise‑grade manual, similar to: Wazuh, Elastic Security, CrowdStrike Labs.


---

🧩 2. Architecture & Data Flow

┌─────────────────────────────┐
 │      User Email Client       │
 │  (Gmail / Outlook / Browser) │
 └──────────────┬──────────────┘
                │
      1) Email is opened
                │
                ▼
 ┌─────────────────────────────┐
 │   HTML Security Notification │
 │     + Tracking Pixel (<img>) │
 └──────────────┬──────────────┘
                │
      2) Pixel loads automatically
                │
                ▼
 ┌────────────────────────────────────────┐
 │        Flask Telemetry Receiver        │
 │  /pixel.gif logs:                      │
 │   • IP                                 │
 │   • User‑Agent                         │
 │   • Timestamp (UTC)                    │
 │   • Query params (user/campaign)       │
 │   • Referrer                           │
 └──────────────┬─────────────────────────┘
                │
                ▼
 ┌─────────────────────────────┐
 │      logs/events.jsonl      │
 │  (JSON Lines Structured Log)│
 └──────────────┬──────────────┘
                │
                ▼
 ┌────────────────────────────────────────┐
 │      SOC Dashboard (/dashboard)        │
 │   Auto‑refresh 5s • Latest events top  │
 └────────────────────────────────────────┘


---

🖼️ 3. Live Evidence (Screenshots Integrated Into Documentation)

> These are not external add‑ons — they are real outputs from the lab, placed exactly where a professional README would expect them.



📨 3.1 Local Email Rendering (email.html)

This is the internal testing render of the HTML email before sending:




---

📬 3.2 Delivered to Gmail (Real Inbox)

The email fully renders inside Gmail, including the hidden tracking pixel.




---

📊 3.3 SOC Dashboard

This dashboard updates automatically every 5 seconds to reflect new telemetry.




---

🖥️ 3.4 Flask Server Logs (Evidence of Pixel Trigger)

Terminal output from the tracking server showing pixel hits.






---

⚙️ 4. Setup & Execution Workflow

This is the exact technical workflow used to build the system from scratch.

🔧 4.1 Create Environment

cd tracking-pixel-soc-lab
python3 -m venv venv
source venv/bin/activate
pip install flask

🖼️ 4.2 Create the Tracking Pixel (1×1 GIF)

printf '\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xFF\xFF\xFF\x21\xF9\x04\x01\x00\x00\x00\x00\x2C\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3B' > 1x1.gif

⚡ 4.3 Flask Tracking Server

/pixel.gif returns the pixel + logs telemetry

/dashboard displays logs

/ simple landing page


Run:

python3 app.py

📩 4.4 Security Alert Email (email.html)

A corporate‑style email including the embedded pixel:

<img src="http://127.0.0.1:5000/pixel.gif?user=ahmed&campaign=test" width="1" height="1" style="display:none;">

📨 4.5 Send Real Email via Gmail SMTP

python3 send_email.py

🎯 4.6 Pixel Trigger → Dashboard Update

When Gmail loads the pixel:

Server logs the request

JSONL grows

Dashboard updates live



---

📁 5. Project Structure

tracking-pixel-soc-lab/
│
├── app.py
├── email.html
├── send_email.py
├── 1x1.gif
│
├── logs/
│   └── events.jsonl
│
├── templates/
│   └── dashboard.html
│
├── evidence/
│   ├── dashboard.png
│   ├── emil_preview.png
│   ├── gmail.png
│   ├── terminal1.png
│   └── terminal2.png
│
└── README.md


---

🧠 6. What This Project Demonstrates (Employer‑Ready)

✔ Email Security Fundamentals

✔ Telemetry Collection Methods

✔ SOC Dashboard Development

✔ Flask API Logging & JSONL Pipelines

✔ Network Metadata Understanding

✔ Python Automation (SMTP, app passwords)

✔ Blue‑Team Defensive Engineering

✔ Evidence‑Driven Documentation

This is exactly the type of project that stands out for:

SOC Analyst Internships

Cloud Security Foundations

DFIR beginner roles

Defensive Security Engineering tracks



---

🏁 7. Final Notes

This lab is designed to be:

🔹 Safe

🔹 Controlled

🔹 Realistic

🔹 Enterprise‑grade


It replicates the real mechanics of email tracking that major companies use for security notifications.


---

<p align="center"><b>Author: Ahmed Tarek — Cloud Security & Blue Team</b></p>
