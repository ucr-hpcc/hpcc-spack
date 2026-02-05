# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.autotools import AutotoolsPackage

from spack.package import *


class Gap(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz"

    version("4.15.1", sha256="6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("gmp")
    depends_on("zlib-ng")
    depends_on("readline")
    
    depends_on("gmake")
    depends_on("ncurses")
    depends_on("cddlib")
    depends_on("curl")
    depends_on("fplll")
    depends_on("mpc")
    depends_on("mpfi")
    depends_on("mpfr")
    depends_on("libzmq")
    depends_on("libxaw")

    def configure_args(self):
        args = []

        args.append("--with-gmp={}".format(self.spec['gmp'].prefix))
        args.append("--with-zlib={}".format(self.spec['zlib-ng'].prefix))
        args.append("--with-readline={}".format(self.spec['readline'].prefix))

        return args

    def build(self, spec, prefix):
        make()
        with working_dir("pkg"):
            bash = which("bash")
            bash("../bin/BuildPackages.sh", "--strict")

    def install(self, spec, prefix):
        make("install")
        install_tree("pkg", prefix.share.gap.pkg)

