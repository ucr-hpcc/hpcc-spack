# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Taxonkit(Package):
    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/shenwei356/taxonkit/archive/refs/tags/v0.20.0.tar.gz"

    version("0.20.0", sha256="eb5a6641264f84997eaa22df7c9cad735c100b434dfd62c2560aba78164f34f6")

    depends_on("go", type="build")

    def install(self, spec, prefix):
        go = which("go")
        go("build", "-C", "taxonkit")

        mkdirp(prefix.bin)
        install(join_path("taxonkit", "taxonkit"), prefix.bin)
