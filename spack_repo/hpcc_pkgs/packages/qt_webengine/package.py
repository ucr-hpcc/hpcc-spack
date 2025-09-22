# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack_repo.builtin.packages.qt_base.package import QtBase, QtPackage
from spack_repo.builtin.build_systems.cmake import CMakePackage
from spack.package import *


class QtWebengine(QtPackage):
    """FIXME: Put a proper description of your package here."""

    #url = QtPackage.get_url(__qualname__)
    #list_url = QtPackage.get_list_url(__qualname__)
    git = QtPackage.get_git(__qualname__)

    # FIXME: Add proper versions here.
    # version("1.2.4")
    version("6.9.1-BROKEN", tag="v6.9.1", commit="d0012809afa1ca30210948d281f48fbc7160fc0c", submodules=True)
    version("6.9.0-BROKEN", tag="v6.9.0", commit="444c84a6c36de4f17d1dbd87710ff5659b71c8bc", submodules=True)
    version("6.8.3-BROKEN", tag="v6.8.3", commit="b586c4eb65d8e46ab2c255e1a141676043a650da", submodules=True)
    version("6.8.2-BROKEN", tag="v6.8.2", commit="6d0b62682d11533b8caf46f1e8b94df89d5defae", submodules=True)
    version("6.8.1-BROKEN", tag="v6.8.1", commit="d2bc1e02bc4c9eeb58cecfdc64bc29f449733012", submodules=True)
    version("6.8.0-BROKEN", tag="v6.8.0", commit="583cf6b8ea10debf2c4ff98592d8f992ce8f560c", submodules=True)
    version("6.7.3-BROKEN", tag="v6.7.3", commit="d29628dfd9f78da12afe8d6072e8e6358cded301", submodules=True)
    version("6.7.2-BROKEN", tag="v6.7.2", commit="445cd4e7784d294a3df8ad3f7b85a7a4988c0bbd", submodules=True)
    version("6.7.1-BROKEN", tag="v6.7.1", commit="2ccbc2bb78bfd1cc03b45361553f4c3d63b31c26", submodules=True)
    version("6.7.0-BROKEN", tag="v6.7.0", commit="1a3e3a233d91037215851ac2821397fc9a846e64", submodules=True)

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    depends_on("gcc", type=("build", "link", "run"))
    conflicts("gcc@:8")
    #depends_on("python")

    depends_on("qt-base +gui+network")
    depends_on("qt-declarative")
#    depends_on("qt-quick3d")
    depends_on("dbus")
    depends_on("nss")
    depends_on("gperf")
    depends_on("py-html5lib")
    depends_on("node-js@14.9:")

    depends_on("libxkbfile")
    depends_on("libxtst")
    depends_on("libxshmfence")
    depends_on("libxi")
    depends_on("libxrandr")
    depends_on("libxcursor")
    depends_on("libxcomposite")
    depends_on("libxdamage")

    for _v in QtBase.versions:
        v = str(_v)
        depends_on("qt-base@" + v, when="@" + v)

    def cmake_args(self):
        args = super().cmake_args() + [
            # Compilation of chromium bugs out w/o explicitly stating gcc's include path
            "-DCMAKE_CXX_STANDARD_INCLUDE_DIRECTORIES={0}".format(join_path(self.spec['gcc'].prefix.include, "c++", self.spec['gcc'].version))
        ]
        return args

    def setup_run_environment(self, env):
        super().setup_run_environment(env)
        env.set("QTWEBENGINEPROCESS_PATH", self.prefix.libexec)
        env.set("QTWEBENGINE_RESOURCES_PATH", self.prefix.resources)
        env.set("QTWEBENGINE_LOCALES_PATH", self.prefix.translations)
        #env.set("QTWEBENGINE_DICTIONARIES_PATH", self.prefix.resources)
