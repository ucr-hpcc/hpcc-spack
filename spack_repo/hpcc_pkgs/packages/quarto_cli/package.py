# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class QuartoCli(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    url = "https://github.com/quarto-dev/quarto-cli/releases/download/v1.8.24/quarto-1.8.24-linux-amd64.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.8.24", sha256="6b83c1c9b6f2ce6454798b42260bd2ee184551d74debe817b8aaf28b09ac22d0")

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        mkdirp(prefix.share)
        install_tree(join_path(self.stage.source_path, "bin"), prefix.bin)
        install_tree(join_path(self.stage.source_path, "share"), prefix.share)
