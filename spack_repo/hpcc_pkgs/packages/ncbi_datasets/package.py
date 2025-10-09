# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class NcbiDatasets(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.ncbi.nlm.nih.gov/datasets/"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version(
        "latest",
        sha256="2c24dcf224d7a210fe5490c7468fd38ae597ef95c2d478d61aed3332e85eb17a",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets",
    )

    resource(
        name="dataformat",
        placement="dataformat",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/dataformat",
        sha256="25be373cb3adff36efbfc76dcd828dd976eaeb006de88324a062ba4f8a6f9830",
    )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("datasets", prefix.bin)
        install(join_path("dataformat", "dataformat"), prefix.bin)

        chmod = which("chmod")
        chmod("+x", prefix.bin.datasets)
        chmod("+x", prefix.bin.dataformat)
