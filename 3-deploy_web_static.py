#!/usr/bin/python3
"compress web_stack locally"
import tarfile
from fabric.api import local
from datetime import datetime
from fabric.api import put, run, env
import os

env.hosts = ['54.157.170.194', '52.23.178.5']


def do_pack():
    "compress"
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    arch_name = "web_static_{}.tgz".format(date)
    local("mkdir -p versions")
    res = local("tar -cvzf versions/{} web_static".format(arch_name))
    size = os.path.getsize("versions/{}".format(arch_name))
    print("web_static packed: versions/{} -> {}Bytes".format(arch_name, size))

    return ('versions/{}'.format(arch_name))


def do_deploy(archive_path):
    "compress"
    if not os.path.exists(archive_path):
        return False
    try:
        filename = archive_path.split('/')[-1]
        no_tgz = '/data/web_static/releases/' + filename.split('.')[0]
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(no_tgz))
        run("sudo tar -xzf /tmp/{} -C {}".format(filename, no_tgz))
        run("sudo rm /tmp/{}".format(filename))
        run("sudo mv {}/web_static/* {}".format(no_tgz, no_tgz))
        run("sudo rm -rf {}/web_static".format(no_tgz))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(no_tgz))
        return True
    except Exception as e:
        return False


def deploy():
    "full deployment"
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
