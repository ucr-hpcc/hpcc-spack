# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class King(Package):
    """KING (Kinship-based INference for Gwas) is a toolset that makes use of
    high-throughput SNP data for relationship inference, family visualization,
    quality control, population structure, ancestry inference, association
    mapping, and risk prediction."""

    homepage = "https://www.kingrelatedness.com/"
    url = "https://www.kingrelatedness.com/executables/KING2.3.2code.tar.gz"
    list_url = "https://www.kingrelatedness.com/history.shtml"

    license("UNKNOWN")

    version("2.3.2", sha256="b6c636ac99d2207d0c2435122abdc4bcd87260ccadaf27dc68df9000b4143a5b")
    version("2.2.9", sha256="47e63c544afc44b266acbd8450e9fe0ef93a8c043a1387dd29e2a069580b3b1f")
    version("2.1.8", sha256="f55ea9ee4f3d8fd8f47e1ed7d30f344f6bd391ad9cf043dbd73ecf39be2fb873")

    depends_on("cxx", type="build")
    depends_on("zlib-api")

    phases = ["build", "install"]

    def url_for_version(self, version):
        return f"https://www.kingrelatedness.com/executables/KING{version}code.tar.gz"

    def build(self, spec, prefix):
        # The tarball is a flat directory of .cpp/.h files with no build system;
        # compile as documented on https://www.kingrelatedness.com/Download.shtml
        cxx = Executable(self.compiler.cxx)
        cxx(
            "-O2",
            self.compiler.openmp_flag,
            "-o",
            "king",
            *find(".", "*.cpp", recursive=False),
            *spec["zlib-api"].libs.ld_flags.split(),
            "-lm",
        )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("king", prefix.bin)
