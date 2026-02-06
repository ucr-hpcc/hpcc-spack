# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Kronatools(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/marbl/Krona/archive/refs/tags/v2.8.1.tar.gz"

    version("2.8.1", sha256="d57eb342427c179bc0431b8a6088313f54326e233762b5652e8a90ce3ca4027d")

    depends_on("perl")

    phases = ("edit", "install")

    def edit(self, spec, prefix):
        # Their "install" just symlinks files. Move them instead
        filter_file(
            "system('ln', '-sf', \"$scriptPath/$script.pl\", \"$path/bin/kt$script\")",
            "system('mv', \"$scriptPath/$script.pl\", \"$path/bin/kt$script\")",
            join_path("KronaTools", "install.pl"),
            string = True
        )

    def install(self, spec, prefix):
        with working_dir("KronaTools"):
            perl = which("perl")
            perl("./install.pl", f"--prefix={prefix}")

            bash = which("bash")
            bash("updateTaxonomy.sh", join_path(prefix, "taxonomy"))
            bash("updateTaxonomy.sh", join_path(prefix, "taxonomy"), "--accessions")
