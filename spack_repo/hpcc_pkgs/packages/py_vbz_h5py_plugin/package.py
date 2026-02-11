# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyVbzH5pyPlugin(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi = "vbz_h5py_plugin/vbz_h5py_plugin-1.0.1.tar.gz"

    version("1.0.1", sha256="c784458bb0aad6303474cb2f10956179116b35555803fd1154eb4ef362519341")

    depends_on("py-setuptools", type="build")

    depends_on("py-h5py", type=("build", "run"))

