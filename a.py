from github import Github
import requests
import json

user=raw_input()
password=raw_input()

g=Github(user,password)

a=g.get_user().name

k=0

for repo in g.get_user().get_repos():
    k+=1
    if k==1:
        continue
    owner=""
    if repo.parent:
        owner=repo.parent.owner.login
    else: 
        owner=repo.owner.login
    url="https://api.github.com/repos/"+owner+"/"+repo.name+"/stats/contributors"
    print repo.name,owner,url,
    r=requests.get(url)
    repoItem=json.loads(r.text or r.content)

    for i in repoItem:
        if i["author"]["login"]!="darkcoderrises":
            continue
        print i["author"]["login"],
        k=0
        for j in  i["weeks"]:
            k+=int(j["a"])+int(j["c"])
        print k
