# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Hifiasm(MakefilePackage):
    """Hifiasm is a fast haplotype-resolved de novo assembler initially designed for PacBio HiFi
    reads. Its latest release could support the telomere-to-telomere assembly by utilizing
    ultralong Oxford Nanopore reads. Hifiasm produces arguably the best single-sample
    telomere-to-telomere assemblies combing HiFi, ultralong and Hi-C reads, and it is one of the
    best haplotype-resolved assemblers for the trio-binning assembly given parental short reads.
    For a human genome, hifiasm can produce the telomere-to-telomere assembly in one day."""

    homepage = "https://github.com/chhylp123/hifiasm"
    url = "https://github.com/chhylp123/hifiasm/archive/refs/tags/0.25.0.tar.gz"

    license("MIT")

    version("0.25.0", sha256="51633138865207a9d41630da9377d46e4921ad4fc5facaa1740ceccae8611f1f")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "hifiasm"), prefix.bin)
