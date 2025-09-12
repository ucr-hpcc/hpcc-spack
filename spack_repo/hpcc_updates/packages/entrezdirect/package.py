# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Entrezdirect(Package):
    """Entrez Direct (EDirect) provides access to the NCBI's suite of
    interconnected databases (publication, sequence, structure,
    gene, variation, expression, etc.) from a UNIX terminal window."""

    homepage = "https://www.ncbi.nlm.nih.gov/books/NBK179288/"
    maintainers("snehring")

    version(
        "24.7.20250910", sha256="cfb67eff0ab1530c8097cddbb98e388b009bb79a117033f9eb79345be48de869"
    )
    version(
        "22.6.20240912", sha256="ddf1aab438bfe6af7cf38f725dac6f288d0daf354197665a66d4556c91129ace"
    )
    version(
        "10.7.20190114", sha256="4152749e6a3aac71a64e9367527428714ed16cf1fb6c7eff1298cca9ef144c0d"
    )

    with when("@22.6.20240912 platform=linux target=aarch64:"):
        resource(
            name="rchive.ARM64",
            placement="rchive-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/rchive.ARM64.gz",
            sha256="48dbd770a62505e3a52cd475f564ba8ab4a20729c318114f8177d5342c519122",
        )
        resource(
            name="transmute.ARM64",
            placement="transmute-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/transmute.ARM64.gz",
            sha256="c9d5dede1c70c29839af4d40a4eb55c0788a8943dc2bde5c919c8bf0be584f34",
        )
        resource(
            name="xtract.ARM64",
            placement="xtract-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/xtract.ARM64.gz",
            sha256="1d62f612b2be6265c517af6c7a5d6bec0ce3f11bcccc6602a78ce1113bd4fc6c",
        )

    with when("@22.6.20240912 platform=darwin target=aarch64:"):
        resource(
            name="rchive.Silicon",
            placement="rchive-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/xtract.Silicon.gz",
            sha256="fd7f73d42055b35783107257eb8d96cc2b65daa00c47774cf1913ab83156719c",
        )
        resource(
            name="transmute.Silicon",
            placement="transmute-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/transmute.Silicon.gz",
            sha256="5ec32a04a29db90a98dced0dbef717da174c6a1228fdb86b94bc35d1aed26545",
        )
        resource(
            name="xtract.Silicon",
            placement="xtract-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/xtract.Silicon.gz",
            sha256="fd7f73d42055b35783107257eb8d96cc2b65daa00c47774cf1913ab83156719c",
        )

    with when("@22.6.20240912 platform=linux target=x86_64:"):
        resource(
            name="rchive.Linux",
            placement="rchive-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/rchive.Linux.gz",
            sha256="2454ca3423df31f4057d1d2ce743e14eb3142d856e688dbbc6586cd9a6b7948c",
        )
        resource(
            name="transmute.Linux",
            placement="transmute-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/transmute.Linux.gz",
            sha256="8a8746b991494f354cb94dc46740691810b673ae1ff5235cf5a60b29fb974ac2",
        )
        resource(
            name="xtract.Linux",
            placement="xtract-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/22.6.20240912/xtract.Linux.gz",
            sha256="cc3994ce640cfe9ed67f4b8c31d6d22d006503c11a8506d50a5a9fe7c0b59124",
        )

    with when("@24.7.20250910 platform=linux target=x86_64:"):
        resource(
            name="rchive.Linux",
            placement="rchive-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/24.7.20250910/rchive.Linux.gz",
            sha256="0f8fa99ccd6be6c8667ffc206a85fc45b9382b6c4156b323fd41e73c6a938c59",
        )
        resource(
            name="transmute.Linux",
            placement="transmute-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/24.7.20250910/transmute.Linux.gz",
            sha256="6e06f1c89f06cc41bf22006ed473de61295295807b0a2e54cf934084452c9b57",
        )
        resource(
            name="xtract.Linux",
            placement="xtract-bin",
            url="https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/24.7.20250910/xtract.Linux.gz",
            sha256="2fcc471f97225022642a5444ec4286e3aa5a2c0d31681a6c95fa4e4fa148ec52",
        )

    depends_on("curl", type="run")
    depends_on("perl", type="run")
    depends_on("perl-html-parser", type="run")
    depends_on("perl-libwww-perl", type="run")
    depends_on("perl-lwp-protocol-https", type="run")
    depends_on("perl-http-message", type="run")
    depends_on("perl-xml-simple", type="run")
    depends_on("python", type="run", when="@22:")

    def url_for_version(self, ver):
        pfx = "https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/versions/"
        return pfx + "{0}/edirect-{0}.tar.gz".format(ver.dotted)

    def install(self, spec, prefix):
        for i in ["rchive", "transmute", "xtract"]:
            src = f"{i}-bin"
            exe = find(src, "*")[0]
            set_executable(exe)
            copy(exe, ".")
            remove_linked_tree(src)
        install_tree(".", prefix.bin)
