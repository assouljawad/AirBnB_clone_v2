#!/usr/bin/python3
""" Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function
do_deploy:
"""

from fabric.api import env, put, run
from fabric.decorators import task
from os.path import exists

env.hosts = ['54.210.121.255', '18.204.20.153']


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