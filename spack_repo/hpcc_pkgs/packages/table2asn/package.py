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

    # Package doesn't have historical releases.
    # Update the "version" when a new version is released it's updated and update the sha256sum
    version(
        "1.29.324",
        url="https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/linux64.table2asn.gz",
        sha256="785bed9880856b208ed84d9765ca094b7c7d12d2225781c2a1854b650d3984bf",
    )

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        os.rename("linux64.table2asn", "table2asn")
        install("table2asn", prefix.bin)

        chmod = which("chmod")
        chmod("+x", prefix.bin.table2asn)
