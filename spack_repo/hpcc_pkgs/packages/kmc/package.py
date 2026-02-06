# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *

import os


class Kmc(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/refresh-bio/KMC/releases/download/v3.2.4/KMC3.2.4.linux.x64.tar.gz"

    version("3.2.4", sha256="158f2084f8d928b3f33b8aaf7d1220fee4183bf46837787e5e6b16bbdf54d31d")

    depends_on("c", type="build")
    depends_on("cxx", type="build")

    stages = ['install']

    def install(self, spec, prefix):
        install_tree(".", prefix)
 
# Saved in case someone more daring than I wants to accomplish building this from source

#    conflicts("target=:x86_64_v2")
#
#    # Needed because included zlib is broken
#    resource(
#        name="zlib",
#        url="https://github.com/madler/zlib/archive/refs/tags/v1.3.1.tar.gz",
#        sha256="17e88863f3600672ab49182f217281b6fc4d3c762bde361935e436a95214d05c",
#        placement="3rd_party/zlib",
#    )
#
#    def edit(self, spec, prefix):
#        os.rmdir(join_path("3rd_party", "cloudflare"))
#        ln = which("ln")
#        ln("-s", "zlib", join_path("3rd_party", "cloudflare"))
#
#        makefile = FileFilter("Makefile")
#        #makefile.filter("LIB_ZLIB=.*", f"LIB_ZLIB={self.spec['zlib'].prefix.lib}")
#        #makefile.filter("kmc: $(KMC_CLI_OBJS) $(LIB_KMC_CORE) $(LIB_ZLIB)", "kmc: $(KMC_CLI_OBJS) $(LIB_KMC_CORE)", string=True)
#        #makefile.filter("kmc_tools: $(KMC_TOOLS_OBJS) $(KMC_API_OBJS) $(KFF_OBJS) $(LIB_ZLIB)", "kmc_tools: $(KMC_TOOLS_OBJS) $(KMC_API_OBJS) $(KFF_OBJS)", string=True)
#        #makefile.filter("-I 3rd_party/cloudflare", f"-I{spec['zlib'].prefix.include}")
#        # https://github.com/refresh-bio/KMC/issues/79
#        makefile.filter("STATIC_CFLAGS = -static -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", f"STATIC_CFLAGS = -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", string=True)
#        makefile.filter("STATIC_LFLAGS = -static -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", f"STATIC_LFLAGS = -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", string=True)
#        #makefile.filter("STATIC_CFLAGS = -static -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", f"STATIC_CFLAGS = -lpthread", string=True)
#        #makefile.filter("STATIC_LFLAGS = -static -Wl,--whole-archive -lpthread -Wl,--no-whole-archive", f"STATIC_LFLAGS = -lpthread", string=True)
#
#        #filter_file('#include "small_sort.h"', '#include "small_sort.h"\n#include "raduls.h"', "kmc_core/kmc.h")
#
##        with working_dir(join_path("3rd_party", "cloudflare")):
##            bash = which("bash")
##            bash("./configure")
#
#    def build(self, spec, prefix):
#        make("kmc")
##        make("kmc_tools")
