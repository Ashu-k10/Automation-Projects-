# 📂 CleanDirectory-Automation
An automated Python utility that periodically scans directories, removes empty files, and generates detailed log reports.

---

## 📌 Overview

CleanDirectory is a Python automation tool that continuously monitors a specified directory at regular intervals.

The application scans every file inside the directory and its subdirectories, identifies empty files, deletes them automatically, and creates a timestamped log file containing the scan details.

This project demonstrates practical usage of:

- File System Automation
- Directory Traversal
- Task Scheduling
- Logging
- Command Line Arguments
- Python Standard Library

---

## 🚀 Features

✅ Recursive directory scanning

✅ Detects empty (0-byte) files

✅ Deletes empty files automatically

✅ Generates timestamp-based log files

✅ Displays total scanned files

✅ Displays number of deleted files

✅ Runs automatically every 5 seconds

✅ Supports command-line execution

---

## 🛠 Technologies Used

- Python 3
- os
- sys
- time
- schedule

---

## 📁 Project Structure

```
CleandDirectory-Automation/
│
├── SourceCode.py
├── README.md
├── requirements.txt
└── Sample_Log/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/Ashu_k10/CleandDirectory-Automation.git
```

Move into the project

```bash
cd CleanDirectory-Automation
```

Install dependencies

```bash
pip install schedule
```

---

## ▶ Usage

Run the script

```bash
python CleanDirectory.py "C:\Users\Ash\Documents\TestFolder"
```

Example

```bash
python directory_sentinel.py D:\Projects
```

---

## 📄 Log Output

A timestamp-based log file is generated automatically.

Example:

```
marvellousMon_Jul_20_12_30_11_2026.log
```

The log contains

- File Name
- File Size
- Total Files Scanned
- Total Empty Files Deleted
- Timestamp

---

## 📸 Workflow

```
Start
   │
   ▼
Read Directory Path
   │
   ▼
Validate Directory
   │
   ▼
Traverse All Files
   │
   ▼
Check File Size
   │
   ▼
Is Empty?
 ┌───────┐
 │ Yes   │────► Delete File
 └───────┘
      │
      ▼
Write Log File
      │
      ▼
Wait 5 Seconds
      │
      ▼
Repeat
```

---

## 🎯 Learning Outcomes

This project helped me understand:

- Python Automation
- Directory Traversal using `os.walk()`
- File Handling
- Logging
- Task Scheduling
- Command Line Programming
- Exception Handling
- Operating System Utilities

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a Pull Request.

---

## 📜 License

This project is licensed under All rights reserved ©

---

## 👨‍💻 Author

**Ashutosh Kadu**

Computer Engineering Student

Python • Automation • AI
