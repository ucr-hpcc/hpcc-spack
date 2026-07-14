# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Multiwfn(MakefilePackage):
    """Multiwfn is a very powerful program for realizing electronic wavefunction
    analysis, which is a key ingredient of quantum chemistry."""

    homepage = "http://sobereva.com/multiwfn/"
    url = "http://sobereva.com/multiwfn/misc/Multiwfn_2026.7.11_bin_Linux.zip"

    version("2026.7.11", sha256="f5f68948e19ace9d74ce59dd130984eba1bf7ad0a9f1032d235128df947ca6a2")

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
