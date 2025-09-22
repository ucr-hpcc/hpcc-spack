# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Cgmaptools(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/guoweilong/cgmaptools/archive/refs/tags/v0.1.3.tar.gz"

    version("0.1.3", sha256="0d323674f75a8bb16a6d680e629d82880b16bf9f013a8b240b997e46dea7b506")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("python", type="run")
    depends_on("R", type="run")

    def install(self, spec, prefix):
        bash = which("bash")
        bash("install.sh")

        for DIR in ["bin", "include", "src"]:
            mkdirp(join_path(prefix, DIR))
            install_tree(DIR, join_path(prefix, DIR))
