import subprocess as cmd

new_file = "C:/03git/test.md"
name_repo = "03GIT"
message = "commit13"

github_repo = "https://github.com:iryna-kurhuzenkava/"
gitlab_repo = "https://gitlab.com:kurhuzenkava/"
bitbacket_repo = "https://bitbucket.org:iryna-kurhuzenkava/"

git_repo = [github_repo, gitlab_repo, bitbacket_repo]


def git_push_automation():
    for item in git_repo:
    #try:
        cmd.run(f'git add --all', check=True, shell=True)
        cmd.run(f'git commit -m "{message}"') #check=True, shell=True)
        cmd.run(f'git remote set-url --push {name_repo} {item}', check=True, shell=True)
        print("Success")
        #return True
    #except:
        #print("Error git automation")

git_push_automation()