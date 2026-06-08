# Website Defacement Monitoring System

## Project Overview

The Website Defacement Monitoring System is a cybersecurity project designed to detect unauthorized modifications to website content.

The system periodically fetches a website, extracts its DOM structure, generates a SHA-256 hash, and compares it with previously stored hashes. If a change is detected, the system alerts the administrator and stores a snapshot for further investigation.

---

## Problem Statement

Create a tool that takes periodic snapshots of a website's DOM structure and hashes it. If the hash changes significantly, alert the admin to potential unauthorized defacement.

---

## Features

- Website content monitoring
- DOM structure extraction
- SHA-256 fingerprint generation
- SQLite database storage
- Change detection
- Automated periodic monitoring
- Snapshot storage for forensic analysis
- GitHub-based project management

---

## Technologies Used

- Python 3.14
- Requests
- BeautifulSoup4
- SQLite3
- Schedule
- VS Code
- Git & GitHub

---

## Project Structure

Website_Defacement_Monitor

├── config.py

├── data/

├── snapshots/

└── src/

├── fetcher.py

├── parser.py

├── hasher.py

├── database.py

├── detector.py

├── snapshot_manager.py

└── monitor.py

---

## Installation

```bash
git clone https://github.com/SubratoScouTOP/Website-Defacement-Monitoring-System.git

cd Website-Defacement-Monitoring-System

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

## Run

```bash
python src/monitor.py
```

---

## Workflow

Website
↓
Fetch HTML
↓
Parse DOM
↓
Generate SHA-256 Hash
↓
Compare With Previous Hash
↓
Detect Changes
↓
Store Snapshot
↓
Alert Administrator

---

## Future Scope

- Email alerts
- SMS notifications
- Flask dashboard
- Severity-based detection
- Machine learning based anomaly detection
- Multi-website monitoring

---

## Author

Subrato Mahato

Cyber Security Summer Project