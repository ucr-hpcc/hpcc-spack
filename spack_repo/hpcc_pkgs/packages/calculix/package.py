# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *

import os
import glob

class Calculix(MakefilePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://www.dhondt.de/ccx_2.23.src.tar.bz2"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.23", sha256="9c88385c10fb04f5dc6c4e98027a51bebdd8aee3920e05190d6c1dd08357d6e7")
    version("2.20", sha256="63bf6ea09e7edcae93e0145b1bb0579ea7ae82e046f6075a27c8145b72761bcf")

    depends_on("c", type="build")
    depends_on("fortran", type="build")

    depends_on("spooles+mt")
    depends_on("arpack-ng")
    depends_on("blas")

    conflicts("%gcc@14:")

    variant("precice", default=False, description="Build with preCICE adapter", when="@2.20")
    depends_on("precice", when="+precice")
    depends_on("mpi", when="+precice")
    depends_on("yaml-cpp", when="+precice")
    depends_on("cxx", when="+precice", type="build")

    resource(
        name="adapter",
        url="https://github.com/precice/calculix-adapter/archive/refs/tags/v2.20.1.tar.gz",
        sha256="3372e0d66321c2173899e1db4841c6c4f3c16ffb99067c36dba04e8a34e35d39",
        when="@2.20",
        placement="adapter"
    )

    def edit(self, spec, prefix):
        with working_dir(join_path(f"ccx_{self.version}", "src")):
            makefile = FileFilter("Makefile")
            makefile.filter("-I ../../../SPOOLES.2.2", f"-I {self.spec['spooles'].prefix.include} -std=legacy")
            makefile.filter("DIR=../../../SPOOLES.2.2", f"DIR={self.spec['spooles'].prefix.lib}")
            makefile.filter("../../../ARPACK/libarpack_INTEL.a", f"{join_path(self.spec['arpack-ng'].prefix.lib64, 'libarpack.so')} -llapack -lblas")
            makefile.filter(f"ccx_{self.version}: $(OCCXMAIN) ccx_{self.version}.a  $(LIBS)", f"ccx_{self.version}: $(OCCXMAIN) ccx_{self.version}.a", string=True)
            makefile.filter("FFLAGS = ", "FFLAGS = -std=legacy ")

            filter_file("#include <MT/spoolesMT.h>", "#include<MT.h>", "spooles.h") # TODO: Confirm if needed if spooles+mt


        if self.spec.satisfies("+precice"):
            with working_dir("adapter"):
                makefile = FileFilter("Makefile")
                makefile.filter("$(HOME)/CalculiX/ccx_$(CCX_VERSION)/src", join_path(self.stage.source_path, f"ccx_{self.version}", "src"), string=True)
                makefile.filter("/usr/include/spooles/", self.spec['spooles'].prefix.include)
                makefile.filter("-lspooles", join_path(self.spec['spooles'].prefix.lib, "spooles.a"))
                makefile.filter("ARPACK_INCLUDE    =", f"ARPACK_INCLUDE    = -I{self.spec['arpack-ng'].prefix.include}")
                makefile.filter("YAML_INCLUDE      = -I/usr/include/", f"YAML_INCLUDE      = -I{self.spec['yaml-cpp'].prefix.include}")

                filter_file('#include "CalculiX.h"', '#include "CalculiX.h"\n#include "dyna_precice.h"', f"ccx_{self.spec['calculix'].version}.c")
                src = join_path(os.path.dirname(self.module.__file__), "dyna_precice.h")
                dest = join_path(join_path(self.stage.source_path, "adapter"), "dyna_precice.h")
                copy(src, dest)

                if self.spec.satisfies("%gcc@10:"):
                    makefile.filter("FFLAGS = -Wall -O3 -fopenmp $(INCLUDES) ${ADDITIONAL_FFLAGS}", "FFLAGS = -Wall -O3 -fopenmp $(INCLUDES) ${ADDITIONAL_FFLAGS} --std=legacy -fallow-argument-mismatch", string=True)

    def build(self, spec, prefix):
        with working_dir(join_path(f"ccx_{self.version}", "src")):
            make()

        if self.spec.satisfies("+precice"):
            with working_dir(join_path(self.stage.source_path, "adapter")):
                make("clean")
                make()

    def install(self, spec, prefix):
        mkdirp(self.prefix.bin)
        with working_dir(join_path(f"ccx_{self.version}", "src")):
            install(f"ccx_{self.version}", self.prefix.bin)

        if self.spec.satisfies("+precice"):
            with working_dir(join_path("adapter", "bin")):
                install("ccx_preCICE", self.prefix.bin)

