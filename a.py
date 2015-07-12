from github import Github

user=raw_input()
password=raw_input()

g=Github(user,password)

a=g.get_user().name

for repo in g.get_user().get_repos():
    if repo.parent:
        print repo.name,repo.parent.owner.login
    else: 
        print repo.name,repo.owner.login
