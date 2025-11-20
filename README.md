# 🛡️ Tracking Pixel SOC Lab – Email Security & Blue Team Simulation

This repository contains a **fully defensive email tracking lab** built with **Python + Flask**.  
The goal is to simulate how a real corporate security email uses a **1×1 tracking pixel** and how a defender (SOC / Blue Team) can:

- Collect events (IP, User-Agent, timestamp, campaign params)
- Log them in a structured format
- Visualize them in a simple SOC dashboard
- Prove the concept using a **real email sent to myself**

> ❗ This project is **NOT** phishing, NOT offensive, and must only be used in **legal, controlled lab environments**.

---

## 🧩 Architecture Overview

The following diagram shows the end-to-end flow of the lab:

```text
                   ┌──────────────────────────┐
                   │       Email Client        │
                   │   (Gmail / Browser)       │
                   └─────────────┬────────────┘
                                 │
                                 │ 1) User opens email
                                 ▼
                    ┌─────────────────────────┐
                    │   HTML Email + Pixel    │
                    │ <img src="SERVER/pixel">│
                    └─────────────┬───────────┘
                                 │
                                 │ 2) Browser requests /pixel.gif
                                 ▼
                ┌──────────────────────────────────┐
                │        Flask Tracking Server      │
                │  /pixel.gif endpoint receives     │
                │  • IP address                     │
                │  • User-Agent                     │
                │  • Timestamp (UTC)                │
                │  • Query params (user, campaign)  │
                └───────────────┬──────────────────┘
                                │
                                │ 3) Append event
                                ▼
                    ┌──────────────────────────┐
                    │       JSONL Log File      │
                    │   logs/events.jsonl       │
                    └─────────────┬────────────┘
                                  │
                                  │ 4) Read & display
                                  ▼
                    ┌──────────────────────────┐
                    │   SOC Dashboard (Flask)   │
                    │ Auto-refresh every 5 sec  │
                    │ Shows all pixel events    │
                    └───────────────────────────┘
