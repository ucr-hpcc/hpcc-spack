# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Phobius(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://software.sbc.su.se/files/phobius101_linux.tgz"

    version(
        "1.01",
        sha256="caf6256d04f8977578b8f0914ee4f4a5bf7bd82af1e67af3932c7762a6627f3e",
        url="https://software.sbc.su.se/files/phobius101_linux.tgz"
    )

    depends_on("perl")
    depends_on("gnuplot")

    phases = ("edit", "install")

    def edit(self, spec, prefix):
        filter_file("/usr/bin/perl", join_path(spec['perl'].prefix.bin, "perl"), "phobius.pl")

    def install(self, spec, prefix):
        install_tree(".", prefix.bin)
