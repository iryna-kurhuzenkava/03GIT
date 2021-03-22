import git

local_repo = "C:/03git/.git"
commit = "commit06"
new_file = "C:/03git/test.md"

github_repo = "https://github.com/iryna-kurhuzenkava/"
gitlab_repo = "https://gitlab.com/kurhuzenkava/"
bitbacket_repo = "https://bitbucket.org/iryna-kurhuzenkava/"

git_repo = [github_repo, gitlab_repo, bitbacket_repo]

def git_push():
    for item in git_repo:
       try:
           repo = git.Repo(local_repo)
           #repo.git.add(update=True)
           repo.git.add(new_file)
           repo.index.commit(commit)
           origin = repo.remote(name="03GIT")
           origin.push(all=True)
       except git.exc.GitCommandError as error:
           print('Some error occured while pushing the code')    

git_push()