```python
# ==========================================================
# Program : Automated GitHub Code Pusher
# Author  : Ashutosh Kadu
# Purpose : Automatically push code to GitHub at a
#           specified time
# ==========================================================

import os
import subprocess
import time
from datetime import datetime

# ==========================================================
# Function : run_git_command
# Description : Execute Git command
# ==========================================================

def run_git_command(command):

    try:
        result = subprocess.run(
            command,
            shell=True,
            text=True,
            capture_output=True
        )

        if result.returncode != 0:
            print("Git Command Failed:")
            print(result.stderr)
            return False

        print(result.stdout)
        return True

    except Exception as e:
        print("Error:", e)
        return False


# ==========================================================
# Function : push_to_github
# Description : Add, commit and push code to GitHub
# ==========================================================

def push_to_github():

    print("\n==========================================")
    print("Starting GitHub Automation")
    print("==========================================")

    # Check Git repository
    if not run_git_command("git status"):
        return

    # Add all changed files
    print("\nAdding files...")
    if not run_git_command("git add ."):
        return

    # Commit changes
    commit_message = (
        "Automated code update - "
        + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    print("\nCreating commit...")
    if not run_git_command(
        f'git commit -m "{commit_message}"'
    ):
        print("No new changes to commit.")
        return

    # Push to GitHub
    print("\nPushing code to GitHub...")

    if run_git_command("git push origin main"):
        print("\n==========================================")
        print("Code Successfully Pushed to GitHub")
        print("==========================================")
    else:
        print("\nGitHub Push Failed")


# ==========================================================
# Function : wait_until
# Description : Wait until specified time
# ==========================================================

def wait_until(target_time):

    print("==========================================")
    print("GitHub Automation Started")
    print("==========================================")

    print("Scheduled Time :", target_time)
    print("Current Time   :", datetime.now().strftime("%H:%M:%S"))

    while True:

        current_time = datetime.now().strftime("%H:%M")

        if current_time == target_time:
            break

        time.sleep(20)


# ==========================================================
# Function : main
# Description : Driver Code
# ==========================================================

def main():

    # ------------------------------------------
    # Set scheduled time
    # Format: HH:MM
    # ------------------------------------------

    scheduled_time = "18:30"

    print("GitHub Code Push Scheduler")
    print("------------------------------------------")

    print(
        "Code will be pushed automatically at:",
        scheduled_time
    )

    # Wait until scheduled time
    wait_until(scheduled_time)

    # Push code
    push_to_github()


# ==========================================================
# Program Entry Point
# ==========================================================

if __name__ == "__main__":
    main()
```
