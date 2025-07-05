import subprocess
import sys

def run_git_command(command):
    """Run a git command and return the result"""
    try:
        result = subprocess.run(['git'] + command.split(), 
                              capture_output=True, 
                              text=True, 
                              check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {e}")
        print(f"Error output: {e.stderr}")
        return None
    except FileNotFoundError:
        print("Git is not installed or not in PATH")
        return None

def main():
    # Example git commands
    print("Git Status:")
    status = run_git_command("status")
    if status:
        print(status)
    
    print("\nGit Branches:")
    branches = run_git_command("branch")
    if branches:
        print(branches)

if __name__ == "__main__":
    main()