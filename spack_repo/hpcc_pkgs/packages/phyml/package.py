# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage
from spack.package import *


class Phyml(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/stephaneguindon/phyml/archive/refs/tags/v3.3.20250515.tar.gz"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("3.3.20250515", sha256="c8d09f52f080a95dde8d7d797da5874796a148158cd18f956110cdba13cd3368")

    depends_on("c", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")

    # MPI is broken for this package.
    #depends_on("mpi", when="+mpi", type=("build", "link", "run"))

    #variant("mpi", default=True, description="Enable MPI build")

    #def setup_build_environment(self, env):
    #    if self.spec.satisfies("+mpi"):
    #        env["CC"] = self.spec["mpi"].mpicc 

    def autoreconf(self, spec, prefix):
        autoreconf("--install", "--verbose", "--force")

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = [
            "--enable-phyml",
        ]

        #if self.spec.satisfies("+mpi"):
        #    args.append("--enable-phyml-mpi")

        return args
