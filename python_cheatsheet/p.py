# import modin.pandas as pd


def pygithub_example():
    from github import Github
    import json
    with open('../../secrets/github.json') as json_file:
        data = json.load(json_file)
    token=data['secret']
    g = Github(token)
    for repo in g.get_user().get_repos():
        print(f"{repo.name} :")
        branch = repo.get_branch("master")
        commits = repo.get_commits()
        for commit in commits:
            print( f"{commit.commit.last_modified}|{commit.commit.author.name} > {commit.commit.message}\n" )
        contents = repo.get_contents("")
        while contents:
            file_content = contents.pop(0)
            if file_content.type == "dir":
                contents.extend(repo.get_contents(file_content.path))
            else:
                print(file_content)
pygithub_example()