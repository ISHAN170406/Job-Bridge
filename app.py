import os
import random
import time
from datetime import datetime

# Configurable settings
file_to_modify = "commit_log.txt"
min_commits = 1
max_commits = 5

# Total time span in a day (in seconds) to spread commits
day_start = 9  # 9 AM
day_end = 23   # 11 PM
total_day_seconds = (day_end - day_start) * 3600

def random_string():
    return f"Commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def make_commit(commit_num):
    with open(file_to_modify, 'a') as f:
        f.write(f"{random_string()}\n")

    os.system("git add .")
    os.system(f'git commit -m "Auto commit #{commit_num}"')
    os.system("git push origin main")
    print(f"[+] Commit #{commit_num} pushed.")

def main():
    commit_count = random.randint(min_commits, max_commits)
    print(f"[~] Will make {commit_count} commits today.")

    # Generate random commit times (in seconds from day start)
    random_seconds = sorted(random.sample(range(total_day_seconds), commit_count))

    for i, seconds in enumerate(random_seconds, 1):
        if i != 1:
            # Wait until the next commit (relative wait)
            wait = seconds - random_seconds[i - 2]
            print(f"[~] Waiting {wait} seconds before next commit...")
            time.sleep(wait)

        make_commit(i)

if __name__ == "__main__":
    # Optional: delay start of the script by 0–30 minutes
    startup_delay = random.randint(0, 1800)
    print(f"[~] Startup delay: {startup_delay} seconds")
    time.sleep(startup_delay)

    main()
