# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Mzmine(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/mzmine/mzmine/releases/download/v4.7.29/mzmine_Linux_portable-4.7.29.zip"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("4.7.29", sha256="df082c2605850d1836fdd028e6fe4dc6a4154e53f614e3bc42a1128e1952db83")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("java", type=("build", "run"))

    def install(self, spec, prefix):
        install_tree(".", prefix)
        chmod = which("chmod")
        chmod("+x", prefix.bin.mzmine)
