import subprocess as cmd

#new_file = "C:/03git/test.md"
#name_repo = "03GIT"
message = "commit14"

#github_repo = "https://github.com:iryna-kurhuzenkava/"
#gitlab_repo = "https://gitlab.com:kurhuzenkava/"
#bitbacket_repo = "https://bitbucket.org:iryna-kurhuzenkava/"

git_repo = {"github_repo": "git@github.com:iryna-kurhuzenkava/03GIT.git",
            "gitlab_repo": "git@gitlab.com:kurhuzenkava/03GIT.git",
            "bitbacket_repo": "git@bitbucket.org:iryna-kurhuzenkava/03git.git"}


def git_push_automation():
    for repo, url in git_repo.items():
    #try:
        cmd.run(f'git add --all') #check=True, shell=True)
        cmd.run(f'git commit -m "{message}"') #check=True, shell=True)
        cmd.run(f'git remote add {repo} {url}')
        cmd.run('git fetch')
        cmd.run(f'git push -u {repo} master') #check=True, shell=True)
        print("Success")
        #return True
    #except:
        #print("Error git automation")

git_push_automation()