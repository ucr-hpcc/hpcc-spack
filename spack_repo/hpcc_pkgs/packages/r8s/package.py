# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class R8s(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://phoenixnap.dl.sourceforge.net/project/r8s/"
    url = "https://sourceforge.net/projects/r8s/files/r8s1.81.tar.gz"

    build_directory = "src"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version(
        "1.81",
        sha256="9e89d7851d74d74487d147b77177a717e6c659b485c9b67f516340a6ed595080",
        url="https://sourceforge.net/projects/r8s/files/r8s1.81.tar.gz",
    )

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install(join_path(self.build_directory, "r8s"), join_path(prefix.bin, "r8s"))
        set_executable(join_path(prefix.bin, "r8s"))
