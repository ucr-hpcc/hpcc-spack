# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Table2asn(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2025-03-03", url="https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/linux64.table2asn.gz", sha256="ff9fedb26eb4e955d4748ef943f371632999f85fc56efff2722fa0728d101bea")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        os.rename("linux64.table2asn", "table2asn")
        install("table2asn", prefix.bin)

        chmod = which("chmod")
        chmod("+x", prefix.bin.table2asn)
