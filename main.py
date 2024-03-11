import os
import datetime


def create_txt_file_with_date():
    # Get the current date
    current_date = datetime.datetime.now().strftime('%Y-%m-%d-%X')

    # Define the file name
    new_file_name = datetime.datetime.now().strftime('%Y-%m-%d')
    file_name = r"C:\Users\aliag\OneDrive\Documents\GitHub\Logs-Automation\Logs Add "+new_file_name+".txt"

    # Write the current date to the file
    with open(file_name, 'w') as file:
            file.write(current_date + '\n')
            print("Text appended successfully.")

def commit_and_push():
    # Navigate to your repository directory
    os.chdir(r'C:\Users\aliag\OneDrive\Documents\GitHub\Logs-Automation')

    # Add all changes to the staging area
    os.system('git add .')
    # Commit changes with current date as message
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    commit_message = f"Schedule Automated commit for {current_date}"
    os.system(f'git commit -m "{commit_message}"')

    # Push changes to remote repository
    os.system('git push origin main')

if __name__ == "__main__":
    create_txt_file_with_date()
    commit_and_push()