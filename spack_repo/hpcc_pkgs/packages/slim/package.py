# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class Slim(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/MesserLab/SLiM/archive/refs/tags/v5.1.tar.gz"

    version("5.1", sha256="e8341014271d12cd872c78738c4c80e57864fb0fb2e33b44ae6b7aedf364fc56")
    version("5.0", sha256="8a5ed1f30a434730fee1446fae554523051d8429532a51946a7a1da812e52b4a")
    version("4.3", sha256="b390a6638a915d6f955608610bca6e94fc0f4d62f5ad07376b2aa98756e8c81d")
    version("4.2.2", sha256="bb63b73e878fb6c15a49f33c3bf1a67047ebb6a11e3d17f930780461dd450400")
    version("4.2.1", sha256="718654ee64e9212f0a33ddffe6e0f33ec56e372824422115f83f0ca7600e9f38")
    version("4.2", sha256="52aaa0296221af706eacf648cbd8fe0ef7ffb9a7462e84605845e287f5bc332b")
    version("4.1", sha256="a9e7c5d2dfea845d838ebf2f2be0a3c74c0ab55ec653ae6ddb8bbdd50df28dd9")
    version("4.0.1", sha256="a44564023db372cd438b4e6c729a4ba59200d1217a63b3694ca7903436886cc2")
    version("4.0", sha256="d53ce9fc4ac00fa1dc3fc046ac21adb461ead46c1a0c54a72537a74873abf894")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
