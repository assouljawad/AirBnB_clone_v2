#!/usr/bin/python3
""" script (based on the file 3-deploy_web_static.py) that deletes
out-of-date archives, using the function do_clean:
"""

from fabric.api import env, put, run, local
from fabric.decorators import task
from os.path import exists

env.hosts = ['54.210.121.255', '18.204.20.153']


@task
def do_clean(number=0):
    """deletes out-of-date archives"""
    num = 1
    if int(number) != 0:
        num = int(number)
    local("ls -dt ./versions/* | head -n -{} \
| xargs rm -rf".format(num))
    run("ls -dt /data/web_static/releases/* | head -n -{}\
| xargs rm -rf".format(num))


@task
def do_deploy(archive_path):
    """do_deploy function """
    if not exists(archive_path):
        return False
    ar_fl = archive_path.split('/')[-1]
    ar_nm = ar_fl.replace('.tgz', '')
    print(ar_fl, ar_nm)
    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(ar_nm))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}\
            '.format(ar_fl, ar_nm))
        run('rm -rf /tmp/{}'.format(ar_fl))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}'.format(ar_nm, ar_nm))
        run('rm -rf /data/web_static/releases/{}/web_static\
            '.format(ar_nm))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ \
            /data/web_static/current'.format(ar_nm))
        return True
    except Exception:
        return False


@task
def do_pack():
    """ create .tgz archive """
    local("mkdir -p versions ; tar -cvzf \
versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static/")
