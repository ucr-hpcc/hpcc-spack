# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Cramino(CargoPackage):
    """A fast quality control tool for Oxford Nanopore sequencing data."""

    homepage = "https://github.com/wdecoster/cramino"
    url = "https://github.com/wdecoster/cramino/archive/refs/tags/1.4.0.tar.gz"

    version("1.4.0", sha256="dbe28360ae6330a3a0fd98bdade7a2b09b777cb547d843db60d97ab34f15a342")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("llvm+clang@:21", type="build")
    depends_on("gmake", type="build", when="%gcc")
