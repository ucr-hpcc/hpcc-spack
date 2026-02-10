# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import glob

from spack_repo.builtin.build_systems.python import PythonPackage

from spack.package import *


class PyPtv(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    #url = "https://gitlab.pasteur.fr/vlegrand/ptv/-/archive/v4.3/ptv-v4.3.tar.gz"
    pypi = "phagetermvirome/phagetermvirome-4.3.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("4.3", sha256="c0f79dccfd81cd39805c6bd5da410efa209e2a06aacb52c13f24c642813e4ee6")

    depends_on("py-poetry-core", type="build")
    depends_on("python@3.9:3.12", type=("build", "run"))
    depends_on("py-numpy@1.25.2:", type=("build", "run"))
    depends_on("py-matplotlib@3.7.2:", type=("build", "run"))
    depends_on("py-pandas@2.1.0:", type=("build", "run"))
    depends_on("py-reportlab@4.0.0:", type=("build", "run"))
    depends_on("py-scipy@1.11.2:", type=("build", "run"))
    depends_on("py-statsmodels@0.14.0:", type=("build", "run"))
    depends_on("py-scikit-learn@1.3.0:", type=("build", "run"))
    
    phases = ("edit", "install")

    def edit(self, spec, prefix):
        files = glob.glob("phagetermvirome/*.py")
        for file in files:
            filter_file("from utilities", "from phagetermvirome.utilities", file)
            filter_file("from SeqStats", "from phagetermvirome.SeqStats", file)
            filter_file("from common_readsCoverage_processing", "from phagetermvirome.common_readsCoverage_processing", file)
            filter_file("from readsCoverage_res", "from phagetermvirome.readsCoverage_res", file)
            filter_file("from functions_PhageTerm", "from phagetermvirome.functions_PhageTerm", file)
            filter_file("from common_readsCoverage_processing", "from phagetermvirome.common_readsCoverage_processing", file)
            filter_file("from IData_handling", "from phagetermvirome.IData_handling", file)
            filter_file("from main_utils", "from phagetermvirome.main_utils", file)
