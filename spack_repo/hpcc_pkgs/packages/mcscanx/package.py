# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *

class Mcscanx(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/wyp1125/MCScanX/archive/refs/tags/v1.0.0.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.0.0", sha256="f8d02cf76251a6a69ccd0c2b92af97f5aafa4d1ac7e907fbbacc480d2d4f238f")

    depends_on("cxx", type="build")
    depends_on("java")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)

        for exe in ["MCScanX", "MCScanX_h", "duplicate_gene_classifier"]:
            install(join_path(self.stage.source_path, exe), prefix.bin)
