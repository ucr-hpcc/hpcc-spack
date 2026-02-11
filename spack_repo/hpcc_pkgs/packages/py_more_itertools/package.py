# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyMoreItertools(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "more_itertools/more_itertools-10.8.0.tar.gz"

    version("10.8.0", sha256="f638ddf8a1a0d134181275fb5d58b086ead7c6a72429ad725c67503f13ba30bd")

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-flit-core", type="build")

    # depends_on("py-foo", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
