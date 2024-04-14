import subprocess

def git_pull(repo_path):
    try:
        # Run 'git pull' command
        result = subprocess.run(['git', 'pull'], cwd=repo_path, capture_output=True, text=True)
        
<<<<<<< HEAD
=======
        # Check if the command was successful
>>>>>>> origin/main
        if result.returncode == 0:
            print("Git pull successful.")
            print(result.stdout)
        else:
            print("Git pull failed.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the Git repository
repo_path = r'C:\Users\aditg\Documents\ProjectSekai'

<<<<<<< HEAD
=======
# Call the function with the repository path
>>>>>>> origin/main
git_pull(repo_path)
