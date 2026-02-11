# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PySmudgeplot(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    pypi = "smudgeplot/smudgeplot-0.5.3.tar.gz"

    version("0.5.3", sha256="f551a812cca280e4cd5341fe4167aa50039d5dae7ae64ca5d00c41c0fa0aca3b")

    depends_on("c", type="build")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
    depends_on("py-matplotlib@3.4.0:", type=("build", "run"))
    depends_on("py-pandas@1.3.0:", type=("build", "run"))

