# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mosdepth(Package):
    """fast BAM/CRAM depth calculation for WGS, exome, or targeted sequencing."""

    homepage = "https://github.com/brentp/mosdepth/"
    url = "https://github.com/brentp/mosdepth/archive/refs/tags/v0.3.11.tar.gz"

    license("MIT")

    version("0.3.11", sha256="4becd1e74a81ed590588ed2745ef7f1443d0a5aad35f9880a2d452d56a7227ff")

    depends_on("nim", type="build")
    depends_on("htslib", type=("build", "run"))

    def setup_run_environment(self, env: EnvironmentModifications) -> None:
        env.prepend_path("LD_LIBRARY_PATH", self.spec['htslib'].prefix.lib)

    def install(self, spec, prefix):
        nimble = Executable("nimble")
        nimble("install", "-y")

        mkdirp(prefix.bin)
        install(join_path(self.stage.source_path, "mosdepth"), prefix.bin)
