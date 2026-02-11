# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

import os


class RtgTools(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/RealTimeGenomics/rtg-tools/archive/refs/tags/3.13.tar.gz"

    version("3.13", sha256="91b4af7fea769912a1bd807bb8d09a8f6b9af27034cd0b598838b48aae97425c")

    depends_on("ant", type=("build"))
    depends_on("java@:14")
    depends_on("maven")

    phases = ("build", "install")

    def build(self, spec, prefix):
        ant = which("ant")
        ant("zip-nojre")

    def install(self, spec, prefix):
        zip_name = f"rtg-tools-{self.version}-unknown-nojre.zip"
        with working_dir("dist"):
            unzip = which("unzip")
            unzip(zip_name)
            install_tree(f"rtg-tools-{self.version}-unknown", prefix.bin)

