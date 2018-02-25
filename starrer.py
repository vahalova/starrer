import requests
import click

URL = 'https://api.github.com/user/starred/{}/{}'

@click.group()
def main():
    return

@main.command()
@click.argument("repository_name", nargs=-1)
def show(repository_name):
    """Shows starred repositories on github"""
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    for page in repository_name:
        adress = page.split("/")
        owner =  adress[0]
        repo = adress[1]
        adress = URL.format(owner, repo)
        req = requests.get(adress, headers=headers)
        if req.status_code == 204:
            print("* " + adress)
        else:
            print("  " + adress)

@main.command()
@click.argument("repository_name")
def add(repository_name):
    """adds a star to the repository"""
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    adress = repository_name.split("/")
    owner =  adress[0]
    repo = adress[1]
    adress = URL.format(owner, repo)
    req = requests.put(adress, headers=headers)
    req.raise_for_status()

@main.command()
@click.argument("repository_name")
def remove(repository_name):
    """remove a star from the repository"""
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    adress = repository_name.split("/")
    owner =  adress[0]
    repo = adress[1]
    adress = URL.format(owner, repo)
    req = requests.delete(adress, headers=headers)
    req.raise_for_status()

main()
