#!/usr/bin/python3
""" Write a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers, using the function
do_deploy:
"""

from fabric.api import *
from fabric.decorators import task, runs_once
from os.path import exists
import time

env.hosts = ['54.84.34.40', '34.204.60.217']


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


@runs_once
@task
def do_pack():
    """ create .tgz archive """
    try:
        local("mkdir -p versions")
        date = time.strftime('%Y%m%d%H%M%S')
        fileName = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(fileName))
        return fileName
    except Exception:
        return False


@task
def deploy():
    """deploy"""
    file = do_pack()
    if file is False:
        return False
    return do_deploy(file)
