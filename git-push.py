import subprocess

def git_push(repo_path):
    try:
        # Run 'git push' command
        result = subprocess.run(['git', 'push'], cwd=repo_path, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Git push successful.")
            print(result.stdout)
        else:
            print("Git push failed.")
            print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

repo_path = r'C:\Users\aditg\Documents\ProjectSekai'

git_push(repo_path)
