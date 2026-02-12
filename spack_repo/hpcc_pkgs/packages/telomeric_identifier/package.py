# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.cargo import CargoPackage

from spack.package import *


class TelomericIdentifier(CargoPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "https://www.example.com"
    url = "https://github.com/tolkit/telomeric-identifier/archive/refs/tags/v0.2.7.tar.gz"

    version("0.2.65", sha256="c0fde2971029683a2bb4f451c872b0d207f421b2dac2622535894f600cc59866")

