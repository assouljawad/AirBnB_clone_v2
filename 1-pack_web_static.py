#!/usr/bin/python3
""" Write a Fabric script that generates a .tgz archive
from the contents of the web_static folder of your AirBnB
Clone repo, using the function do_pack.
"""

from fabric.decorators import task
from fabric.api import local


@task
def do_pack():
    """ create .tgz archive """
    local("mkdir -p versions ; tar -cvzf \
versions/web_static_$(date +%Y%m%d%H%M%S).tgz web_static/")
