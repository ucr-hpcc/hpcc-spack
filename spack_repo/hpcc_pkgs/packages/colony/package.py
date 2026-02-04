# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
import glob
from spack_repo.builtin.build_systems.generic import Package
from spack.package import *

class Colony(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.zsl.org/about-zsl/resources/software/colony/thank-you"
    url = "file://{0}/colony2_Lnx_15_07_2025.zip".format(os.getcwd())
    manual_download = True

    version("2.0.7.2", sha256="e40e1cf06e0f27bc0160d5badc8c65a574f1b095c3f6eb713d13103fbe083a8d")

    depends_on("intel-oneapi-compilers", type="run")
    depends_on("intel-oneapi-mpi", type="run")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        chmod = which("chmod")
        for exe in ["ColonyBatchRun.out", "colony2s.ifort.out", "colony2p.ifort.impi2018.out"]:
            chmod("+x", exe)
            install(exe, prefix.bin)
