# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Admixture(Package):
    """ADMIXTURE is a software tool for maximum likelihood estimation of individual ancestries
    from multilocus SNP genotype datasets. It uses the same statistical model as STRUCTURE but
    calculates estimates much more rapidly using a fast numerical optimization algorithm."""

    homepage = "https://dalexander.github.io/admixture/index.html"
    url = "https://dalexander.github.io/admixture/binaries/admixture_linux-1.3.0.tar.gz"

    license("UNKNOWN")

    version("1.3.0", sha256="353e8b170c81f8d95946bf18bc78afda5d6bd32645b2a68658bd6781ff35703c")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(
            join_path(self.stage.source_path, f"admixture_linux-{spec.version}", "admixture"),
            prefix.bin,
        )
