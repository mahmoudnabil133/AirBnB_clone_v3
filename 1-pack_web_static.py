#!/usr/bin/python3
"compress web_stack locally"
import tarfile
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    "compress"
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    # print(os.path.exists("versions"))
    if not os.path.exists("versions"):
        local("sudo mkdir -p versions")

    arch_name = "web_static_{}.tgz".format(date)
    res = local("sudo tar -cvzf versions/{} web_static".format(arch_name))
    size = os.path.getsize("versions/{}".format(arch_name))
    print("web_static packed: versions/{} -> {}Bytes".format(arch_name, size))
