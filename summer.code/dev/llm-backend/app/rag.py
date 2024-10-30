import os
import subprocess
def git_clone(repo_url):
    user_name = repo_url.split('/')[-2]
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    folder_name = user_name + '_' + repo_name
    current_directory = os.getcwd()
    destination = os.path.join(current_directory, 'repo')
    destination = os.path.join(destination, folder_name)
    if os.path.exists(destination):
        return True, destination
    try:
        result = subprocess.run(
            ['git', 'clone', repo_url, destination],
            check=True,
            text=True,
            capture_output=True
        )
        print("Clone successful:")
        print(result.stdout)
        return True, destination
    except subprocess.CalledProcessError as e:
        print("Error during clone:")
        print(e.stderr)
        return False, destination

