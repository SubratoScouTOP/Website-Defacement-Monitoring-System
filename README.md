# Website Defacement Monitoring System

## Overview

 Website Defacement Monitoring System is a cybersecurity project that continuously monitors a website for unauthorized content modifications.

The system periodically fetches a website, extracts its DOM structure, generates a cryptographic hash, and compares it with previously stored snapshots. If significant changes are detected, the system alerts the administrator and stores evidence for further investigation.

This project demonstrates concepts such as:

- Website Integrity Monitoring
- Digital Fingerprinting
- Change Detection
- Similarity Analysis
- Severity Classification
- Logging and Auditing
- Snapshot Preservation

---

## Problem Statement

Create a tool that takes periodic snapshots of a website's DOM structure and hashes it.

If the hash changes significantly, alert the administrator to potential unauthorized website defacement.

---

## Features

### Website Monitoring

- Periodically fetches target website content.
- Extracts website DOM structure.
- Creates unique SHA-256 fingerprints.

### Change Detection

- Compares current fingerprint with previous fingerprints.
- Detects unauthorized modifications.

### Similarity Analysis

- Measures similarity between old and new DOM structures.
- Calculates percentage difference.

### Severity Classification

Classifies detected changes into:

- LOW
- MEDIUM
- HIGH
- CRITICAL

based on similarity percentage.

### Snapshot Storage

Stores HTML snapshots whenever significant changes are detected.

### Logging System

Maintains audit logs for:

- Website checks
- Change detections
- Snapshot creation
- Monitoring activities

### Database Storage

Stores:

- Timestamp
- Website URL
- Hash Value
- DOM Content

using SQLite.

---

## Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Core Development |
| Requests | Website Fetching |
| BeautifulSoup | DOM Parsing |
| SQLite | Database Storage |
| Schedule | Periodic Monitoring |
| SHA-256 | Fingerprinting |
| Git & GitHub | Version Control |

---

## Project Structure

Website_Defacement_Monitor

├── config.py

├── README.md

├── requirements.txt

├── data

│ └── hashes.db

├── logs

│ └── monitor.log

├── snapshots

│ └── snapshot files

├── src

│ ├── fetcher.py

│ ├── parser.py

│ ├── hasher.py

│ ├── database.py

│ ├── detector.py

│ ├── similarity.py

│ ├── severity.py

│ ├── logger.py

│ ├── snapshot_manager.py

│ └── monitor.py

└── venv

---

## Project Workflow

### Step 1: Website Fetching

The system fetches website content using the Requests library.

↓

### Step 2: DOM Extraction

BeautifulSoup extracts and normalizes the DOM structure.

↓

### Step 3: Hash Generation

SHA-256 generates a unique fingerprint of the DOM.

↓

### Step 4: Database Lookup

The latest stored hash is retrieved from SQLite.

↓

### Step 5: Change Detection

Current hash is compared with previous hash.

↓

### Step 6: Similarity Analysis

If a change is detected, DOM similarity percentage is calculated.

↓

### Step 7: Severity Classification

The change is classified as:

- LOW
- MEDIUM
- HIGH
- CRITICAL

↓

### Step 8: Snapshot Creation

Modified HTML content is stored as evidence.

↓

### Step 9: Logging

Monitoring activity is recorded in log files.

↓

### Step 10: Continuous Monitoring

The process repeats at fixed intervals.

---

## Severity Levels

| Similarity | Severity |
|------------|----------|
| 95% - 100% | LOW |
| 75% - 94% | MEDIUM |
| 50% - 74% | HIGH |
| Below 50% | CRITICAL |

---

## Installation

### Clone Repository

```bash
git clone https://github.com/SubratoScouTOP/Website-Defacement-Monitoring-System.git
```

### Move into Project

```bash
cd Website-Defacement-Monitoring-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\Activate.ps1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Open:

```python
config.py
```

Configure:

```python
TARGET_URL = "https://example.com"

CHECK_INTERVAL = 1

TIMEOUT = 10
```

---

## Running the Project

```bash
python src/monitor.py
```

Expected Output:

```text
Current Hash:
xxxxxxxxxxxxxxxxxxxxxxxx

Detection Result:
No changes detected.

Monitoring started...
Checking every 1 minute(s).
```

---

## Database Schema

Table:

```sql
website_hashes
```

Columns:

| Column | Description |
|----------|----------|
| id | Record ID |  .
| timestamp | Monitoring Time |
| website | Website URL |
| hash | SHA-256 Fingerprint |
| dom_content | Stored DOM |

---

## Future Enhancements

- Email Alerts
- Telegram Notifications
- Web Dashboard
- Multi-Website Monitoring
- Machine Learning Based Anomaly Detection
- Real-Time Visualization

---

## Author

Subrato Mahato

Cybersecurity Summer Project

Website Defacement Monitoring System

