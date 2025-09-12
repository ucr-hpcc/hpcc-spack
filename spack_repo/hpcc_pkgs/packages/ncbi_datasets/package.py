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
        sha256="200c6ef8df827768904dba7b4f4694c8b598599612a385cd2dce67ae2839ed0f",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets",
    )

    resource(
        name="dataformat",
        placement="dataformat",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/dataformat",
        sha256="ffdc54e8dcf5542c5369b29ecfe71e8153ab74034eb3f1522fcc42eb4629447b",
    )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("datasets", prefix.bin)
        install(join_path("dataformat", "dataformat"), prefix.bin)

        chmod = which("chmod")
        chmod("+x", prefix.bin.datasets)
        chmod("+x", prefix.bin.dataformat)
