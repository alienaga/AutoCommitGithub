import datetime
import os
from pathlib import Path

def create_txt_file_with_date():
    # Generate today's date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Build dynamic file path
    base_dir = Path.home() / "OneDrive" / "Documents" / "GitHub" / "Logs-AutoSave"
    file_path = base_dir / f"Logs Add {current_date}.txt"

    # Create the directory if it doesn't exist
    base_dir.mkdir(parents=True, exist_ok=True)

    # Write the current date to the file
    with open(file_path, 'w') as file:
        file.write(current_date + '\n')
        print("Text written successfully to file.")

    print(f"Your log file was saved here:\n{file_path}")

def commit_and_push():
    repo_path = Path.home() / "OneDrive" / "Documents" / "GitHub" / "Logs-AutoSave"
    os.chdir(repo_path)

    # Initialize Git if not already a repo
    if not (repo_path / ".git").exists():
        os.system('git init')
        os.system('git remote add origin https://github.com/alienaga/Logs-Automation.git')
        os.system('git pull origin main --allow-unrelated-histories')
    
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Schedule Automated commit for {current_date}"

    os.system('git add .')
    os.system(f'git commit -m "{commit_message}"')

    # 🛠 Add this line to avoid rejection due to upstream changes
    os.system('git pull origin master --allow-unrelated-histories')

    os.system('git push origin master')

if __name__ == "__main__":
    create_txt_file_with_date()
    commit_and_push()