# 🛡️ Website Defacement Monitoring System

A Python-based Website Defacement Monitoring System that continuously monitors websites, detects unauthorized content changes, classifies their severity, stores historical records, sends email alerts, and provides an admin dashboard for monitoring activities.

---

## 📌 Features

### ✅ Website Monitoring
- Periodically checks target websites.
- Automatically fetches webpage content.

### ✅ DOM Parsing
- Extracts meaningful HTML content.
- Removes unnecessary formatting noise.

### ✅ SHA-256 Hashing
- Generates a unique hash for webpage content.
- Enables fast change detection.

### ✅ Change Detection
- Detects modifications in website content.
- Identifies whether content has changed or not.

### ✅ SQLite Database
- Stores:
  - Timestamp
  - Website URL
  - Hash Value
  - DOM Content

### ✅ Logging System
- Records monitoring activities.
- Maintains event history.

### ✅ Similarity Analysis
- Compares previous and current webpage content.
- Calculates similarity percentage.

### ✅ Severity Classification
| Similarity | Severity |
|------------|----------|
| ≥95% | LOW |
| 70%-94% | MEDIUM |
| 40%-69% | HIGH |
| <40% | CRITICAL |

### ✅ Snapshot Generation
- Saves HTML snapshots during severe incidents.

### ✅ Email Alerts
- Sends email notifications for HIGH and CRITICAL attacks.

### ✅ Automated Monitoring
- Runs continuously using scheduled checks.

### ✅ Flask Dashboard
- Provides a simple admin interface.

---

# 📂 Project Structure

```text
Website_Defacement_Monitor/
│
├── dashboard/
│   ├── app.py
│   ├── templates/
│   │      └── index.html
│   └── static/
│          └── style.css
│
├── data/
│
├── logs/
│
├── snapshots/
│
├── src/
│   ├── fetcher.py
│   ├── parser.py
│   ├── hasher.py
│   ├── detector.py
│   ├── database.py
│   ├── logger.py
│   ├── similarity.py
│   ├── severity.py
│   ├── snapshot_manager.py
│   ├── email_alert.py
│   └── monitor.py
│
├── config.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/SubratoScouTOP/Website-Defacement-Monitoring-System.git
```

Move into the project:

```bash
cd Website-Defacement-Monitoring-System
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

Modify `config.py`:

```python
TARGET_URL = "https://example.com"

CHECK_INTERVAL = 1

TIMEOUT = 10
```

For email alerts:

```python
SMTP_SERVER = "smtp.gmail.com"

SMTP_PORT = 587

EMAIL_SENDER = "your_email@gmail.com"

EMAIL_PASSWORD = "your_app_password"

EMAIL_RECEIVER = "receiver@gmail.com"
```

---

# 🚀 Running the Monitor

```bash
python src/monitor.py
```

---

# 🌐 Running the Dashboard

```bash
python dashboard/app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🔄 Workflow

```text
Target Website
       │
       ▼
fetcher.py
       │
       ▼
parser.py
       │
       ▼
hasher.py
       │
       ▼
detector.py
       │
       ▼
database.py
       │
       ▼
similarity.py
       │
       ▼
severity.py
       │
       ▼
HIGH / CRITICAL ?
       │
 ┌─────┴─────┐
 │           │
No          Yes
 │           │
 ▼           ▼
Continue  snapshot_manager.py
                │
                ▼
          email_alert.py
                │
                ▼
             logger.py
                │
                ▼
          Flask Dashboard
```

---

# 📧 Alert Mechanism

When a website is modified:

1. Detect change.
2. Calculate similarity percentage.
3. Determine severity level.
4. Save HTML snapshot (HIGH/CRITICAL).
5. Send email alert.
6. Log the incident.
7. Store information in database.

---

# 🛠 Technologies Used

- Python
- Flask
- SQLite3
- Requests
- BeautifulSoup4
- hashlib
- difflib
- smtplib
- Schedule
- HTML
- CSS

---

# Future Improvements

- React Dashboard
- Live Monitoring
- Auto Refresh
- Charts and Statistics
- Multiple Website Monitoring
- User Authentication
- Docker Deployment
- Cloud Deployment
- REST API
- SMS Notifications

---

# Author

**Subrato Mahato**

GitHub:
https://github.com/SubratoScouTOP

---

# License

This project is intended for educational and research purposes.