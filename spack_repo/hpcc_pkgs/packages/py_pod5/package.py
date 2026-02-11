# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPod5(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    pypi = "pod5/pod5-0.3.35.tar.gz"

    version("0.3.35", sha256="aad17af0def53e7f64a891dc7c70213bbda6f596072b9b346a20158c8a553ab6")

    depends_on("py-setuptools", type="build")
    depends_on("py-iso8601", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-arrow", type=("build", "run"))
    depends_on("py-pytz", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-polars", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-vbz-h5py-plugin", type=("build", "run"))
    depends_on("py-more-itertools", type=("build", "run"))

