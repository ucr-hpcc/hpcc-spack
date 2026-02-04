# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Famsa(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git = "git@github.com:refresh-bio/FAMSA.git"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.4.1", tag="v2.4.1", commit="45c9b2b4d15e4526212a0e968f130395eef05bb7", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    conflicts("%gcc@:11")

    phases = ["build", "install"]

    def build(self, spec, prefix):
        simd_features = [
            "avx512",
            "avx2",
            "avx",
            "sse4",
        ]
        
        platform = None
        for feature in simd_features:
            if feature in self.spec.target:
                platform = feature
                break

        gmake = which("gmake")
        if platform:
            gmake(f"PLATFORM={platform}")
        else:
            gmake()

    def install(self, spec, prefix):
        install_tree("bin", prefix.bin)
