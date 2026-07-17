# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class Vcflib(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/vcflib/vcflib/releases/download/v1.0.14/vcflib-1.0.14-src.tar.gz"

    version("1.0.15", sha256="178e8c27fffc5324ac73f1c4b35f407184271b57f82aedc2efb9703df6ee3d49")
    version("1.0.14", sha256="27ba26a3c48ba3911e760de1c5633d46b57e1e8dce9ad41e8cb3de299d2d6053")

    conflicts("%gcc@:11")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("zig@0.13", when="@1.0.14")
    depends_on("zig@0.15", when="@1.0.15")
    depends_on("py-pybind11")

    depends_on("htslib")
    depends_on("python")
    depends_on("xz")
    depends_on("libdeflate")
    depends_on("curl")
    depends_on("openssl")
    depends_on("nghttp2")
    depends_on("bzip2")
    depends_on("zlib-ng")

    def cmake_args(self):
        args = [
            "-DWFA_GITMODULE=ON", # Use optimized version
        ]
        return args
