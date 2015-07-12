from github import Github

user=raw_input()
password=raw_input()

g=Github(user,password)

for repo in g.get_user().get_repos():
    print repo.name
