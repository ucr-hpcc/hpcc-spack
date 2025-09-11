# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Cactus(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/ComparativeGenomicsToolkit/cactus/releases/download/v2.9.9/cactus-bin-v2.9.9.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.9.9", sha256="60a02eb14cef92a1dc087ddb5e9672f403ce305e3067863db6c525325c03cd82")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        install_tree(".", prefix)
