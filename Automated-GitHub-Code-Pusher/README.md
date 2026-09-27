# 🚀 Automated GitHub Code Pusher

A simple Python automation script that automatically **adds, commits, and pushes code to a GitHub repository at a specified time**.

This project is useful for automating repetitive Git operations such as:

- `git add`
- `git commit`
- `git push`

The script waits until the configured time and then automatically pushes the latest changes to the configured GitHub branch.

---

## 📌 Features

- ⏰ Schedule GitHub pushes for a specific time
- 📁 Automatically detect changes in the project
- ➕ Automatically run `git add .`
- 💾 Automatically create a commit
- 🚀 Automatically push changes to GitHub
- 🕒 Uses the computer's local system time
- 🐍 Built completely with Python
- 📋 Displays Git operation status and errors

---

## 🛠️ Technologies Used

- Python 3
- Git
- GitHub
- Python `subprocess`
- Python `datetime`
- Python `time`

No external Python packages are required.

---

## 📂 Project Structure

```text
Automated-GitHub-Code-Pusher/
│
├── github_automation.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Prerequisites

Before running the project, install:

### 1. Python

Check whether Python is installed:

```bash
python --version
```

or:

```bash
python3 --version
```

### 2. Git

Check Git installation:

```bash
git --version
```

### 3. GitHub Repository

Your project must already be connected to a GitHub repository.

Check the remote repository:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/username/my-project.git
```

---

## 🔧 Setup

### Step 1 — Clone your repository

```bash
git clone https://github.com/USERNAME/REPOSITORY.git
```

Move into the project:

```bash
cd REPOSITORY
```

---

### Step 2 — Add the automation script

Copy:

```text
github_automation.py
```

into your project directory.

---

### Step 3 — Configure the scheduled time

Open:

```text
github_automation.py
```

Find:

```python
scheduled_time = "18:30"
```

Change it to your required time.

For example:

```python
scheduled_time = "21:00"
```

The format is:

```text
HH:MM
```

---

## ▶️ Run the Automation

Execute:

```bash
python github_automation.py
```

The program will wait until the configured time.

Example:

```text
GitHub Code Push Scheduler
------------------------------------------
Code will be pushed automatically at: 18:30

==========================================
GitHub Automation Started
==========================================

Scheduled Time : 18:30
Current Time   : 18:12:32
```

At 18:30, the script automatically performs:

```text
git status
      ↓
git add .
      ↓
git commit
      ↓
git push origin main
```

---

## 📤 Example Output

```text
Adding files...

Creating commit...

Pushing code to GitHub...

==========================================
Code Successfully Pushed to GitHub
==========================================
```

---

## 🔐 GitHub Authentication

The script does not store a GitHub password or Personal Access Token inside the Python source code.

Git authentication should be configured separately using one of the following:

- Git Credential Manager
- SSH authentication
- GitHub CLI
- Appropriate Git credentials

For security, **never hard-code a GitHub Personal Access Token in the source code**.

---

## ⚠️ Important

The Python script must be running before the scheduled time.

For example:

```text
16:00 → Start Python script
        ↓
        Waiting...
        ↓
18:30 → Git operations execute
        ↓
        GitHub updated
```

If the computer is shut down or the Python process is stopped, the script cannot perform the push.

For fully automatic execution without keeping the Python script open, the project can be extended using:

- Windows Task Scheduler
- Linux/macOS `cron`
- GitHub Actions

---

## 📝 Custom Commit Message

The script automatically generates a commit message similar to:

```text
Automated code update - 2026-09-27 18:30:00
```

This is generated using:

```python
datetime.now()
```

---

## 🔄 Git Workflow

```text
       Project Files
            │
            ↓
       git status
            │
            ↓
        git add .
            │
            ↓
       git commit
            │
            ↓
        git push
            │
            ↓
        GitHub
```

---

## 🎯 Future Improvements

Possible improvements include:

- Multiple scheduled push times
- Custom commit messages
- Automatic GitHub repository creation
- Email notifications
- Discord/Telegram notifications
- Push failure notifications
- Automatic retry mechanism
- Windows Task Scheduler integration
- Linux/macOS cron integration
- GitHub Actions integration
- GUI-based scheduler
- Configuration through `.env` file

---

## 👨‍💻 Author

**Ashutosh Kadu**

Python • Git • GitHub • Automation

---

## 📄 License

This project is intended for educational and personal automation purposes.
