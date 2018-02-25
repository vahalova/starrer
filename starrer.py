import requests
import click

URL = 'https://api.github.com/user/starred/{}'

@click.group()
def main():
    return

def get_session():
    with open('auth.cfg') as f:
        token = f.read().strip()
    headers = {'Authorization': 'token ' + token}
    session = requests.Session()
    session.headers.update(headers)
    return session

@main.command()
@click.argument("repository_name", nargs=-1)
def show(repository_name):
    """Show starred repositories on github"""
    session = get_session()
    for page in repository_name:
        adress = URL.format(page)
        req = session.get(adress)
        if req.status_code == 204:
            print("* " + adress)
        else:
            print("  " + adress)

def add_or_remove(operation, repository_name):
    """add or remove a star to/from the repository"""
    session = get_session()
    adress = URL.format(repository_name)
    if operation == "add":
        req = session.put(adress)
    elif operation == "remove":
        req = session.delete(adress)
    req.raise_for_status()

@main.command()
@click.argument("repository_name")
def add(repository_name):
    """add a star to the repository"""
    add_or_remove("add", repository_name)


@main.command()
@click.argument("repository_name")
def remove(repository_name):
    """remove a star from the repository"""
    add_or_remove("remove", repository_name)

main()
