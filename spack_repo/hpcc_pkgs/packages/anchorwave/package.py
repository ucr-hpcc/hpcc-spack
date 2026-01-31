# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *

import os


class Anchorwave(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/baoxingsong/AnchorWave/archive/refs/tags/v1.2.6.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    license("MIT", checked_by="emwjacobson")

    version("1.2.6", sha256="568cd3943c464d0294717232a73f7e4fe13f8db34146871e9ca870eb676a30d9")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("minimap2")
    depends_on("zlib-ng")
    depends_on("python")

    @run_before("cmake")
    def config_cpu(self):
        simd_features = [
            ("avx512", "CMakeLists_avx512.txt"),
            ("avx2", "CMakeLists_avx2.txt"),
            ("sse4_1", "CMakeLists_sse4.1.txt"),
            ("sse2", "CMakeLists_sse2.txt"),
        ]

        for feature, filename in simd_features:
            if feature in self.spec.target:
                print(F"USING TARGET {feature}")
                os.remove("CMakeLists.txt")
                os.rename(filename, "CMakeLists.txt")
                break

    def cmake_args(self):
        args = []
        return args
