# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Spooles(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://www.netlib.org/linalg/spooles/spooles.2.2.tgz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.2", sha256="a84559a0e987a1e423055ef4fdf3035d55b65bbe4bf915efaa1a35bef7f8c5dd")

    depends_on("c", type="build")

    variant("mt", default=False, description="Enable MT")
    variant("mpi", default=False, description="Enable MPI")
    depends_on("mpi", when="+mpi")

    def edit(self, spec, prefix):
        filter_file("CC = .*", "CC = cc", "Make.inc")

        if self.spec.satisfies("+mt"):
            filter_file("#cd MT", "\tcd MT", "makefile")
            filter_file("cd src ; make spoolesMT.a", "cd src ; make makeLib", join_path("MT", "makefile"))

        if self.spec.satisfies("+mpi"):
            filter_file("#cd MPI", "\tcd MPI", "makefile")
            filter_file("/usr/local/mpich-1.0.13", self.spec['mpi'].prefix, "Make.inc")
            filter_file("-L$(MPI_INSTALL_DIR)/lib/solaris/ch_p4", self.spec['mpi'].prefix.lib, "Make.inc")
            filter_file("cd src ; make spoolesMPI.a", "cd src ; make makeLib", join_path("MT", "makefile"))
            

    def build(self, spec, prefix):
        make("lib")

    def install(self, spec, prefix):
        mkdirp(self.prefix.lib)
        mkdirp(self.prefix.include)
        
        install("spooles.a", self.prefix.lib)
        install_tree(".", self.prefix.include)
