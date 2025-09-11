# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Globusconnectpersonal(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://downloads.globus.org/globus-connect-personal/linux/stable/globusconnectpersonal-latest.tgz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    depends_on("python@3:", type="run")
    depends_on("tk", type="run")
    depends_on("tcl-tcllib", type="run")

    # FIXME: Add proper versions and checksums here.
    version("latest", sha256="37b0a3b5eb110f965d1817507be3174394050cdee76ab14271be176765872017")

    def install(self, spec, prefix):
        install_tree(".", prefix.bin)
