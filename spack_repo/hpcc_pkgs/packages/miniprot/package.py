# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class Miniprot(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/lh3/miniprot/releases/download/v0.18/miniprot-0.18.tar.bz2"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.18", sha256="307428a8da5854fa4c2f078ff0ca07756143b28e1598b8247c727ca2b87b15b1")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("zlib")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("miniprot", prefix.bin)
