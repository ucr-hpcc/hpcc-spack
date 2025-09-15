# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class Aiupred(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/doszilab/AIUPred/archive/refs/tags/2.1.2.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.1.2", sha256="9a61784fff9206bce46dc7d3ca906a557b328c3113971f58977833f0fc071aeb")

    depends_on("py-torch@2.0.1:", type=("build", "run"))
    depends_on("py-numpy@1.26.0:", type=("build", "run"))
    depends_on("py-scipy@1.13.0:", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        with open("aiupred.py", "r+") as f:
            content = f.read()
            f.seek(0,0)
            f.write("#!/usr/bin/env python3" + "\n" + content)
        chmod = which("chmod")
        chmod("+x", "aiupred.py")
        install("aiupred.py", prefix.bin)
        install("aiupred_lib.py", prefix.bin)
