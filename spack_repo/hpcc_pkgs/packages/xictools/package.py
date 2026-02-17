# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *

import os
import glob

class Xictools(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/wrcad/xictools/archive/refs/tags/xt-4.3.23.tar.gz"

    version("4.3.23", sha256="f329d71bf637ed09921de6b0f6fdc38443d1a97617ca528a4eafa1be37c99e72")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("gmake", type="build")

    depends_on("gsl")
    depends_on("libjpeg")
    depends_on("libtiff")
    depends_on("ncurses")
    depends_on("qt@5+opengl")

    phases = ("configure", "build", "install")

    def setup_run_environment(self, env):
        env.set("grpref", "QT5")
        for directory in ("xictools/bin", "xictools/mozy/bin", "xictools/wrspice.current/bin", "xictools/xic.current/bin"):
            env.prepend_path("PATH", join_path(self.spec.prefix, directory))

    def configure(self, spec, prefix):
        os.rename("Makefile.sample", "Makefile")
        ff = FileFilter("Makefile")
        ff.filter("--prefix=.*$", "--prefix={}".format(prefix))
        ff.filter("#GFXLOC = --enable-qt5=/usr/lib64/qt5", "GFXLOC = --enable-qt5={}".format(spec['qt'].prefix))

    def build(self, spec, prefix):
        make("-j", "all")

    def install(self, spec, prefix):
        # This will install all tools
        make("install")
        
