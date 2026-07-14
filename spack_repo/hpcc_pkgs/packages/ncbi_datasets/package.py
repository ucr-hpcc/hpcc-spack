# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class NcbiDatasets(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.ncbi.nlm.nih.gov/datasets/"

    # NOTE: NCBI does not post past versions. If downloads are failing, redownload
    # the package and update the version and sha256sum
    version(
        "18.33.1",
        sha256="8459ef1e87433f7b1198f5703c8cc10b55f1904cd448cf7e996c0892b141cd1f",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/datasets",
    )

    resource(
        name="dataformat",
        placement="dataformat",
        expand=False,
        url="https://ftp.ncbi.nlm.nih.gov/pub/datasets/command-line/v2/linux-amd64/dataformat",
        sha256="8450cf7cbdb0ed7fece567405732cd1ff838b5352faa58abbccdeff56e1ff0e8",
    )

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("datasets", prefix.bin)
        install(join_path("dataformat", "dataformat"), prefix.bin)

        chmod = which("chmod")
        chmod("+x", prefix.bin.datasets)
        chmod("+x", prefix.bin.dataformat)
