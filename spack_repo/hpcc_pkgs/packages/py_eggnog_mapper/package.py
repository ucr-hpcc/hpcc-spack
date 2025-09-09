# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyEggnogMapper(PythonPackage):
    """EggNOG-mapper is a tool for fast functional annotation of novel sequences. It uses
    precomputed orthologous groups and phylogenies from the eggNOG database to transfer
    functional information from fine-grained orthologs only."""

    homepage = "https://github.com/eggnogdb/eggnog-mapper/"
    url = "https://files.pythonhosted.org/packages/66/dd/cf5bfcfe81530c3694ef2cd038f106c192cc97e953f2be48729e3c92f5f5/eggnog_mapper-2.1.13-py3-none-any.whl"

    license("AGPL-3.0-only")

    version("2.1.13", sha256="1d8956a1c9262da43960fa27c26b851292b9d544ccb2dbac7c98031a765761a4")

    depends_on("python@3.7:3.11", type=("build", "run"))

    depends_on("py-setuptools", type="build")
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-xlsxwriter", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))
