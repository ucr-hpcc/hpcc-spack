# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class BwaMem2(MakefilePackage):
    """The tool bwa-mem2 is the next version of the bwa-mem algorithm in bwa. It produces
    alignment identical to bwa and is ~1.3-3.1x faster depending on the use-case, dataset and the
    running machine."""

    homepage = "https://github.com/bwa-mem2/bwa-mem2"
    url = "https://github.com/bwa-mem2/bwa-mem2/archive/refs/tags/v2.3.tar.gz"
    git = "https://github.com/bwa-mem2/bwa-mem2.git"

    license("MIT")

    version("2.3", tag="v2.3", commit="7aa5ff6c3330490e5629ab9b7327683d2dce02d6", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for exe in [
            "bwa-mem2",
            "bwa-mem2.avx",
            "bwa-mem2.avx2",
            "bwa-mem2.avx512bw",
            "bwa-mem2.sse41",
            "bwa-mem2.sse42",
        ]:
            install(join_path(self.build_directory, exe), prefix.bin)
