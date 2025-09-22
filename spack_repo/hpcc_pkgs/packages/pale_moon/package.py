# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class PaleMoon(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://rm-us.palemoon.org/release/palemoon-33.8.2.linux-x86_64-gtk3.tar.xz"

    license("UNKNOWN", checked_by="github_user1")

    version("33.8.2", sha256="d0b7f06442d8e011a8853d8a0c441862efa824804a5e0e32cd952e08e6347400")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        install_tree(".", prefix.bin)
