#!/usr/bin/python3
"compress web_stack locally"


import tarfile
from fabric.api import local
from datetime import datetime
from fabric.api import put, run, env
import os

env.hosts = ['54.157.170.194', '52.23.178.5']


def do_deploy(archive_path):
    "compress"
    try:
        if not os.path.exists(archive_path):
            return False
        filename = archive_path.split('/')[-1]
        no_tgz = '/data/web_static/releases/' + filename.split('.')[0]

        if put(archive_path, '/tmp/').failed:
            return False
        if run("sudo mkdir -p {}".format(no_tgz)).failed:
            return False
        if run("sudo tar -xzf /tmp/{} -C {}".format(filename, no_tgz)).failed:
            return False
        if run("sudo rm -f /tmp/{}".format(filename)).failed:
            return False
        imgs = '/data/web_static/releases/web_static_20240310095451/images/*'
        stys = '/data/web_static/releases/web_static_20240310095451/styles/*'
        if run("sudo rm -rf {}".format(imgs)).failed:
            return False
        if run("sudo rm -rf {}".format(stys)).failed:
            return False
        if run("sudo mv -f {}/web_static/* {}".format(no_tgz, no_tgz)).failed:
            return False
        if run("sudo rm -rf {}/web_static".format(no_tgz)).failed:
            return False
        if run("sudo rm -f /data/web_static/current").failed:
            return False
        link = '/data/web_static/current'
        if run("sudo ln -s {} {}".format(no_tgz, link)).failed:
            return False
        return True

    except Exception as e:
        return False
