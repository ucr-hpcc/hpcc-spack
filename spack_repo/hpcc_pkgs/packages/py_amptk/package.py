# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class PyAmptk(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://files.pythonhosted.org/packages/cb/9a/344a26e92830900ed2319d4263f93a9b2344fb751680da842def9bd8bc21/amptk-1.6.0-py3-none-any.whl"

    license("UNKNOWN")

    version("1.6.0", sha256="93cd043be1acde8e061bf6f338c18adcd383970cba6753bb18cfe3fa6a0b4aed")

    depends_on("python@3.3:3.10", type=("build", "run"))
    depends_on("py-setuptools@:80", type=("build", "run"))

    depends_on("py-edlib", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    #depends_on("py-pyfastx", type=("build", "run"))  # Doesn't (yet) exist in spack
    depends_on("py-biopython", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-natsort", type=("build", "run"))
    depends_on("py-biom-format", type=("build", "run"))
    depends_on("py-distro", type=("build", "run"))

    def config_settings(self, spec, prefix):
        # FIXME: Add configuration settings to be passed to the build backend
        # FIXME: If not needed, delete this function
        settings = {}
        return settings
