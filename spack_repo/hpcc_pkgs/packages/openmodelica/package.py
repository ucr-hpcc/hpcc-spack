# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack_repo.builtin.packages.boost.package import Boost

from spack.package import *


class Openmodelica(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    git = "https://github.com/OpenModelica/OpenModelica.git"

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.25.4-BROKEN", tag="v1.25.4", commit="51e02b5f5f4e0d1f6ce751cbbea59af07ffc4026", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("boost@:1.86") # Boost 1.87 removes boost::asio::io_service
    depends_on(Boost.with_default_variants)
    depends_on("qt-base@6: +gui+opengl+network")
    depends_on("qt-5compat")
    depends_on("qt-svg")
    depends_on("qt-webengine")
    depends_on("qt-tools")
    depends_on("hwloc")
    depends_on("opencl")
    depends_on("openblas")
#    depends_on("lapack")
#    depends_on("blas")
    depends_on("hdf5")
    depends_on("expat")
    depends_on("curl")
    depends_on("ncurses")
    depends_on("readline")
    depends_on("openscenegraph")
    depends_on("krb5")
    depends_on("keyutils")
    depends_on("openssl")
    depends_on("java", type=("build", "link", "run"))

    conflicts("%gcc@:8", msg="OpenModelica needs gcc >= 9") # Needs support for c++17. Not added until gcc@9
    conflicts("qt-base~opengl") # Force qwt to use qt-base built with opengl

    def cmake_args(self):
        args = [
            "-DOM_USE_CCACHE=OFF",
            "-DOM_QT_MAJOR_VERSION=6",
            "-DOM_OMEDIT_ENABLE_QTWEBENGINE=ON",
        ]
        return args

