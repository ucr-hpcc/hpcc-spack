# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyFunannotate(PythonPackage):
    """funannotate is a pipeline for genome annotation (built specifically for fungi, but will
    also work with higher eukaryotes)"""

    homepage = "https://github.com/nextgenusfs/funannotate"
    url = "https://files.pythonhosted.org/packages/d7/b4/e2818055cccf699137f1ce430f86651854c75c71fe659ea898924a5f5d9b/funannotate-1.8.17-py3-none-any.whl"

    license("BSD-2-Clause")

    version("1.8.17", sha256="fcd2969d68fdbec38fd4a110865e28726289cdb6a819ae6161b4f842ec4e8646")

    # FIXME: Only add the python/pip/wheel dependencies if you need specific versions
    # or need to change the dependency type. Generic python/pip/wheel dependencies are
    # added implicity by the PythonPackage base class.
    depends_on("python@3.6.0:3.9", type=("build", "run"))
    # depends_on("py-pip@X.Y:", type="build")
    # depends_on("py-wheel@X.Y:", type="build")

    # FIXME: Add a build backend, usually defined in pyproject.toml. If no such file
    # exists, use setuptools.
    # depends_on("py-setuptools", type="build")
    # depends_on("py-hatchling", type="build")
    # depends_on("py-flit-core", type="build")
    # depends_on("py-poetry-core", type="build")

    # FIXME: Add additional dependencies if required.
    # depends_on("py-foo", type=("build", "run"))

    depends_on("py-biopython@:1.79", type=("build", "run"))
    depends_on("py-goatools", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-distro", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
