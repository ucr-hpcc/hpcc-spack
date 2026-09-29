# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mega(Package):
    """About mega"""

    homepage = "https://www.megasoftware.net/"
    url = "file://{0}/megacc_11.0.13_amd64.tar.gz".format(os.getcwd())
    manual_download = True

    version("11.0.13", sha256="a20a1bc0522265b6b8b9afc3d86747befbb67629371bf87365d1e7b72bbfe53e")
    version("12.1.2", sha256="f5c944ffbaecd5e107ec8c6fed7e42b0dee7d68111406c82ad6c62d43a81c940")

#    depends_on("libc@2.34:")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("megacc", prefix.bin)
