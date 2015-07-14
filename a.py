from github import Github
import requests
import json

User=raw_input()
password=raw_input()

g=Github(User,password)

user=raw_input()

a=g.get_user(user).name

for repo in g.get_user(user).get_repos():
    owner=""
    if repo.parent:
        owner=repo.parent.owner.login
    else: 
        owner=repo.owner.login
    url="https://api.github.com/repos/"+owner+"/"+repo.name+"/stats/contributors"
    print repo.name,owner,url,
    r=requests.get(url)
    repoItem=json.loads(r.text or r.content)

    url1="https://api.github.com/repos/"+owner+"/"+repo.name+"/languages"
    r1 = requests.get(url1)
    repoItem1 = json.loads(r1.text or r1.content)
    total=0
    for i in repoItem1:
        total += int(repoItem1[i])

    for i in repoItem:
        if i["author"]["login"]!=user:
            continue
        print i["author"]["login"],
        k=0
        for j in  i["weeks"]:
            k+=int(j["a"])+int(j["c"])
        print k,total,k*1.0/total*1.0

