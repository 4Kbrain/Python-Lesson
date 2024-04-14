import subprocess

def git_push(repo_path):
    try:
        # Run 'git push' command
        result = subprocess.run(['git', 'push'], cwd=repo_path, capture_output=True, text=True)
        
<<<<<<< HEAD
=======
        # Check if the command was successful
>>>>>>> origin/main
        if result.returncode == 0:
            print("Git push successful.")
            print(result.stdout)
        else:
            print("Git push failed.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

<<<<<<< HEAD
repo_path = r'C:\Users\aditg\Documents\ProjectSekai'

=======
# Path to the Git repository
repo_path = r'C:\Users\aditg\Documents\ProjectSekai'

# Call the function with the repository path
>>>>>>> origin/main
git_push(repo_path)
