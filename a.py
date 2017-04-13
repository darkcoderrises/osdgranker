from github import Github
import requests
import json

user_name = raw_input()
password = raw_input()

g = Github(user_name,password)

user = raw_input()

a = g.get_user(user).name

for repo in g.get_user(user).get_repos():
    owner= repo.parent.owner.login if repo.parent else repo.owner.login
    
    url="https://api.github.com/repos/"+owner+"/"+repo.name+"/stats/contributors"
    print repo.name, owner, url,
    
    r = requests.get(url)
    repoItem = json.loads(r.text or r.content)

    contributionsUrl = "https://api.github.com/repos/"+owner+"/"+repo.name+"/languages"
    req_contri = requests.get(contributionsUrl)
    
    repoContributions = json.loads(req_contri.text or req_contri.content)
    repoContributions = [int(repoContributions[i]) for i in repoItem]
    total = sum(repoContributions)

    for i in repoItem:
        if i["author"]["login"]!=user:
            continue
        print i["author"]["login"],
        
        k=0
        for j in i["weeks"]:
            k+=int(j["a"])+int(j["c"])
        print k, total, float(k)/total

