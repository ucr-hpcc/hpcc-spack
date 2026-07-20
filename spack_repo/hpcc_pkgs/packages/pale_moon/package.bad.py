# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package
from spack.package import *


class PaleMoon(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
#    url = "https://rm-us.palemoon.org/release/palemoon-33.8.2.linux-x86_64-gtk3.tar.xz"
    git = "https://repo.palemoon.org/MoonchildProductions/Pale-Moon.git"

    version("34.3.1", commit="0d869b85feca1409f5aadb55e6eaabb08db134ad", submodules=True)

    phases = ["build", "install"]

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("gmake", type="build")

    depends_on("gtkplus")
    depends_on("openssl")
    depends_on("sqlite")
    depends_on("pulseaudio")
    depends_on("python")
    depends_on("alsa-lib")
    depends_on("nasm")

    def build(self, spec, prefix):
        src = join_path(self.package_dir, "mozconfig")
        dst = join_path(self.stage.source_path, ".mozconfig")
        copy(src, dst)

        mach = Executable("./mach")
        mach("build")

    def install(self, spec, prefix):
        return
        install_tree(".", prefix.bin)
