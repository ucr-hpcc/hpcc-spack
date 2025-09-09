# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPyspoa(PythonPackage):
    """Python bindings to spoa"""

    homepage = "https://github.com/nanoporetech/pyspoa"
    pypi = "pyspoa/pyspoa-0.0.8.tar.gz"

    license("MIT")

    version("0.3.1", sha256="4c198cb67a69792b0bb272bbf9397e078d764a4995c0e351b947ede95b53ffa2")
    version("0.0.8", sha256="8299d18066b498a6ef294c5a33a99266ded06eeb022f67488d2caecba974b0a4")

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated

    depends_on("py-setuptools", type="build")
    depends_on("cmake@3:", type="build")
    depends_on("py-pybind11@2.4:", type=("build", "run"))
