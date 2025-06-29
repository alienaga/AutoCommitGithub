import datetime
import os
from pathlib import Path

def create_txt_file_with_date():
    today_str = datetime.datetime.now().strftime('%Y-%m-%d')
    now_str   = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Today's date is: {today_str}")
    print(f"Current date and time: {now_str}")

    base_dir = Path.home() / "OneDrive" / "Documents" / "GitHub" / "Logs-AutoSave"
    base_dir.mkdir(parents=True, exist_ok=True)

    file_path = base_dir / f"Logs Add {today_str}.txt"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(now_str + '\n')
    print(f"Text written successfully to file:\n  {file_path}")

def commit_and_push():
    repo_path = Path.home() / "OneDrive" / "Documents" / "GitHub" / "Logs-AutoSave"
    os.chdir(repo_path)

    # 1) On first run: init + remote + set up main branch
    if not (repo_path / ".git").exists():
        os.system('git init')
        os.system('git remote add origin https://github.com/alienaga/Logs-Automation.git')
        # create a local main that tracks origin/main (won't wipe your new file)
        os.system('git fetch origin main')
        os.system('git checkout -b main --track origin/main')

    # 2) Always pull any new remote commits
    os.system('git pull origin main --allow-unrelated-histories')

    # 3) Stage & commit your newly-written log
    now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    os.system('git add .')
    os.system(f'git commit -m "Automated commit for {now_str}"')

    # 4) Push back to GitHub
    os.system('git push origin main')

if __name__ == "__main__":
    create_txt_file_with_date()
    commit_and_push()