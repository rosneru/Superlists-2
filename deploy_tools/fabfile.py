from fabric import task, Connection
import patchwork.files as files

import random

REPO_URL = 'https://github.com/rosneru/Superlists-2'


@task()
def deploy(c: Connection):
    site_folder = f'/home/{c.user}/sites/{c.host}'
    c.run(f'mkdir -p {site_folder}')
    with c.cd(site_folder):
        _get_latest_source(c)
        _update_virtualenv(c)
        _create_or_update_dotenv()
        _update_static_files(c)
        _update_database(c)


def _get_latest_source(c: Connection):
    if not c.run(f'test -d .git', warn=True):
        c.run(f'git clone {REPO_URL} .')
    else:
        c.run('git pull')


def _update_virtualenv(c: Connection):
    if not c.run('test -f virtualenv/bin/pip', warn=True):
        c.run('python3 -m venv virtualenv')
    c.run('./virtualenv/bin/pip install -r requirements.txt')


def _create_or_update_dotenv(c: Connection):
    files.append(c, '.env', 'DJANGO_DEBUG_FALSE=y')
    files.append(c, '.env', f'SITENAME={c.host}')
    current_contents = c.run('cat .env')
    if 'DJANGO_SECRET_KEY' not in current_contents:
        new_secret = ''.join(random.SystemRandom().choices(
            'abcdefghijklmnopqrstuvwxyz0123456789', k=50
        ))
        files.append(c, '.env', f'DJANGO_SECRET_KEY={new_secret}')


def _update_static_files(c: Connection):
    c.run('./virtualenv/bin/python manage.py collectstatic --noinput')


def _update_database(c: Connection):
    c.run('./virtualenv/bin/python manage.py migrate --noinput')
