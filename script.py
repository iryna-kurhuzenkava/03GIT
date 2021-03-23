import git

local_repo = "C:/03git/.git"
commit = "commit09"
new_file = "C:/03git/test.md"

github_repo = "https://github.com:iryna-kurhuzenkava/03GIT.git"
gitlab_repo = "https://gitlab.com:kurhuzenkava/03GIT.git"
bitbacket_repo = "https://bitbucket.org:iryna-kurhuzenkava/03git.git"

#github_repo = "https://github.com:iryna-kurhuzenkava/"
#gitlab_repo = "https://gitlab.com:kurhuzenkava/"
#bitbacket_repo = "https://bitbucket.org:iryna-kurhuzenkava/"

git_repo = [github_repo, gitlab_repo, bitbacket_repo]

def git_push(o):
    for item in o:
       #try:
           repo = git.Repo(local_repo)
           #repo.git.add(update=True)
           repo.git.add(new_file)
           repo.index.commit(commit)
           #repo.create_remote("newrepo", item)
           origin = repo.remote(name = item)
           origin.push(all=True)
           #origin.push()
       #except git.exc.GitCommandError as error:
           #print('Some error occured while pushing the code')    

git_push(git_repo)