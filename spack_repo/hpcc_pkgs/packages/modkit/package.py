# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class Modkit(CargoPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/nanoporetech/modkit/archive/refs/tags/v0.6.1.tar.gz"

    version("0.6.1", sha256="31e280b0c7bd87291648f642324052a77fd88d0e25464e7e43b415b01101c9e1")

    def build(self, spec, prefix):
        cargo = which("cargo")
        cargo("install", "--root", "out", "--path", "modkit")

