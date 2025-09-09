# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install bwa-mem2
#
# You can edit this file again by typing:
#
#     spack edit bwa-mem2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.makefile import MakefilePackage
from spack.package import *


class BwaMem2(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/bwa-mem2/bwa-mem2/archive/refs/tags/v2.3.tar.gz"
    git = "https://github.com/bwa-mem2/bwa-mem2.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.3", tag="v2.3", commit="7aa5ff6c3330490e5629ab9b7327683d2dce02d6", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def edit(self, spec, prefix):
        # FIXME: Edit the Makefile if necessary
        # FIXME: If not needed delete this function
        # makefile = FileFilter("Makefile")
        # makefile.filter("CC = .*", "CC = cc")
        pass

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        for exe in [ 
            "bwa-mem2",
            "bwa-mem2.avx",
            "bwa-mem2.avx2",
            "bwa-mem2.avx512bw",
            "bwa-mem2.sse41", 
            "bwa-mem2.sse42"
        ]:
            install(join_path(self.build_directory, exe), prefix.bin)
