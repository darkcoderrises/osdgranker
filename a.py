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
        if i["author"]["login"]!="darkcoderrises":
            continue
        print i["author"]["login"],
        k=0
        for j in  i["weeks"]:
            k+=int(j["a"])+int(j["c"])
        print k,total,k*1.0/total*1.0

