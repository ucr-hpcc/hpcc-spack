# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Multiwfn(MakefilePackage):
    """Multiwfn is a very powerful program for realizing electronic wavefunction
    analysis, which is a key ingredient of quantum chemistry."""

    homepage = "http://sobereva.com/multiwfn/"
    url = "http://sobereva.com/multiwfn/misc/Multiwfn_2026.6.2_src_Linux.zip"

    version("2026.6.2", sha256="62f8436101267253d7e63e3034af4bd2e38b198c2d99428566206418cdab5424")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # Needs GCC for normal compilation
    depends_on("gcc", type="build")
    # Needs ifort for fortral
    depends_on("intel-oneapi-compilers", type="build")
    depends_on("intel-oneapi-mkl", type="build")

    def edit(self, spec, prefix):
        makefile = FileFilter("Makefile")
        # ifort is deprecated, replace with ifx
        makefile.filter("FC = .*", "FC = ifx")
        # -mkl is deprecated, replace with -qmkl
        makefile.filter("-mkl", "-qmkl")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for exe in ["Multiwfn", "Multiwfn_noGUI"]:
            install(exe, prefix.bin)
