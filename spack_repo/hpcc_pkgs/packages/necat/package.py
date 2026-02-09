# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Necat(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/xiaochuanle/NECAT/archive/refs/tags/v0.0.1_update20200803.tar.gz"

    version("0.0.1_update20200803", sha256="5ddd147b5be6b1fac2f6c10b18c9b587838f2304d2584087c4ed6f628eced06c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("perl")
    depends_on("zlib-ng")

    build_directory = "src"

    def install(self, spec, prefix):
        install_tree("Linux-amd64", prefix)
