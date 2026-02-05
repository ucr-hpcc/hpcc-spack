# TODOs
- Mention config files
    - concretizer.yaml
    - toolchains.yaml
- Mention commands
    - spack location
    - spack cd
- Users configuring upstreams


# SPACK


## Introduction

Spack should *hopefully* make our lives easier when installing packages by taking the burden of compiling dependencies and software itself off of us.

Currently, Spack is installed in `/opt/linux/rocky/8.x/x86_64/`. Most/all paths mentioned from here will be relative to this directory. Configuration files are available in `spack/etc/spack`. There is a `defaults` directory containing the default configuration. **Do not edit the files in the `defaults` directory**. Instead, make/edit the files within the `spack/etc/spack` directory as they will override the settings within the corresponding `spack/etc/spack/defaults` directory.

Some config files of special importance are `config.yaml`, `repos.yaml`, and `packages.yaml`. 

### config.yaml
`config.yaml` is currently configured to store installed packages within a `${os}/{name}/{version}-{hash}` folder structure. The default structure is fairly verbose and supports multiple architectures, though we want our installed software to be universally runnable. This file also configures the build of the software to occur in the scratch directory. This will prevent it from building in the default locations of `/tmp` or the home directory. Note that two colons are included for `build_stage`, as a single colon would append to the default list rather than override it.

### repos.yaml
`repos.yaml` configures where Spack searches for packages. We have an `hpcc` repo that is used for new packages or updates to packages. There is also Spack's built in repo. If there are updates to the repos, they can be pulled using `spack repo update` which will pull the latest updates from both repos.

### packages.yaml
`packages.yaml` configures how Spack installs packages. With `packages:all:target:` we explicitly target the `x86_64_v2` architecture. This is to accomidate the older batch and highmem nodes. If/when these are removed, the target can be increased to `x86_64_v3`. `packages:all:require:` configures spack to use GCC as the compiler when C, C++, or Fortran are required by the package. This is complemented by `packages:gcc:` to set the version preference. As of the time of writing, it's set to `["@8", "@12", "@14"]`, which will first use GCC 8 (the OS-provided version) followed by GCC 12, then GCC 14 (both need to be manually installed). `packages:all:providers:` specified which packages can provide certain features. Here we only have MPI, which can be satisfied by OpenMPI, MPICH, or Intel's OneAPI. There is `packages:all:variants:` which will attempt to build all packages as "RelWithDebInfo". This might result in larger binaries, but should hopefully allow us (and maybe the users) an easier time debugging programs if there are problems. Finally there is package-specific configuration. As of the time of writing, LLVM, openmpi, mpich, slurm, and opengl are the only manually configured packages. For LLVM, it's build with `build_type=Release`, as there were problems compiling it with debug. OpenMPI and MPICH are both build with support for Slurm, so we shouldn't need to worry about specifying that variant manually. Slurm and OpenGL are both system-provided packages, but are made visible to Spack if they're required by other packages.



## Installation of Software

When requested, software can be searched for at https://packages.spack.io/

If software is not available, see the [Package Creation](#package-creation) section. If software is available, keep reading this section.

You can see what software will be installed alongside the main package by using `spack spec PACKAGE`. When installing, there are sometimes configuration options (variants) that can enable/disable certain options. For example, `openmpi` has variants for cuda, java, gpfs, etc. Most of the time the default variants are acceptable, unless there are certain features that you know are needed or that users explicitly request. Some packages (eg. openmpi, mpich) have specific flags set globally. The config for this can be found in the `spack/etc/spack/packages.yaml` file. In the case of openmpi and mpich, they will always compile with Slurm support.

More reading on the Spack spec syntax can be found in their documentation:
https://spack.readthedocs.io/en/latest/spec_syntax.html

If the spec listed is acceptable, then it can be installed using `spack install PACKAGE`. Modifiers can be added to speed up compilation, eg `spack install -p4 -j16 PACKAGE` to install up to 4 packages in parallel, using up to 16 cores per package. Module files will also automatically be generated for newly installed packages. This is thanks to the configuration file at `spack/etc/spack/modules.yaml`.



## Common Installation Problems

### Filename Too Long
I've encountered issues where the file path has been too long for some tools to handle. In this case, the build directory will likely need to be changed. Within spack's `config.yaml` file, the `config:build_stage::` variable can be changed to "/tmp/${user}" which should allow for a shorter path name. The `/tmp` directory is significantly smaller than scratch, so be sure to revert this change after installing.

### Compiler Versions

Sometimes when installing packages, compilation problems can arise. The problem I see most often is that the software needs a newer (or older) version of gcc. For example, gcc 15 changes a handful of things so older packages can't be compiled with it. The correct thing would be to submit a update to the Spack packages with a newer version, patch to allow it to compile, and/or a conflict with the problematic gcc versions(s), though the easier solution would just be to use a different compiler. Using a different version of GCC (eg. 12) can be done as follows:

```
spack install PACKAGENAME %gcc@12
```

If a certain piece of software needs a different version than it's dependency, you can specify multiple different compilers using:
```
spack install PKGA %gcc@X.X.X ^PKGB %gcc@Y.Y.Y
```

This just follows the Spack spec syntax, and more information on that can be found on their [Spec Syntax](https://spack.readthedocs.io/en/latest/spec_syntax.html) page.


### Dependencies

Sometimes you'll need to manually install dependencies. To get the dependency itself, run a `spack spec` on the software to see what variants/options the dependency is configured with. As an example, we'll use `bamtools`.

```console
$ spack spec bamtools
 -   bamtools@2.5.2~ipo build_system=cmake build_type=RelWithDebInfo generator=make arch=linux-rocky8-x86_64_v2 %cxx=gcc@8.5.0
 -       ^cmake@3.31.8~doc+ncurses+ownlibs~qtgui build_system=generic build_type=RelWithDebInfo arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -           ^curl@8.15.0~gssapi~ldap~libidn2~librtmp~libssh~libssh2+nghttp2 build_system=autotools libs:=shared,static tls:=openssl arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -               ^nghttp2@1.65.0 build_system=autotools arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -                   ^diffutils@3.12 build_system=autotools arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -                       ^libiconv@1.18 build_system=autotools libs:=shared,static arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -               ^openssl@3.4.1~docs+shared build_system=generic certs=mozilla arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -                   ^ca-certificates-mozilla@2025-08-12 build_system=generic arch=linux-rocky8-x86_64_v2 
 -               ^perl@5.42.0+cpanm+opcode+open+shared+threads build_system=generic arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -                   ^berkeley-db@18.1.40+cxx~docs+stl build_system=autotools patches:=26090f4,b231fcc arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -                   ^bzip2@1.0.8~debug~pic+shared build_system=generic arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -                   ^gdbm@1.25 build_system=autotools arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -                       ^readline@8.3 build_system=autotools patches:=21f0a03 arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -               ^pkgconf@2.5.1 build_system=autotools arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -           ^ncurses@6.5-20250705~symlinks+termlib abi=none build_system=autotools patches:=7a351bc arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
 -       ^compiler-wrapper@1.0 build_system=generic arch=linux-rocky8-x86_64_v2 
[e]      ^gcc@8.5.0~binutils+bootstrap~graphite~nvptx~piclibs~profiled~strip build_system=autotools build_type=Release languages:='c,c++,fortran' patches:=98a9c96,d4919d6 arch=linux-rocky8-x86_64_v2 
 -       ^gcc-runtime@8.5.0 build_system=generic arch=linux-rocky8-x86_64_v2 
[e]      ^glibc@2.28 build_system=autotools arch=linux-rocky8-x86_64_v2 
 -       ^gmake@4.4.1~guile build_system=generic arch=linux-rocky8-x86_64_v2 %c=gcc@8.5.0
 -       ^jsoncpp@1.9.6~ipo build_system=cmake build_type=RelWithDebInfo generator=make arch=linux-rocky8-x86_64_v2 %cxx=gcc@8.5.0
 -       ^zlib-ng@2.2.4+compat+new_strategies+opt+pic+shared build_system=autotools arch=linux-rocky8-x86_64_v2 %c,cxx=gcc@8.5.0
```

With this, we can see that gcc and glibc are provided externally `[e]`, and everything else is uninstalled. Lets pretend that `jsoncpp` had problems installing. We can see that it's full spec is `jsoncpp@1.9.6~ipo build_system=cmake build_type=RelWithDebInfo generator=make arch=linux-rocky8-x86_64_v2 %cxx=gcc@8.5.0`, so we can run `spack install jsoncpp@1.9.6~ipo build_system=cmake build_type=RelWithDebInfo generator=make arch=linux-rocky8-x86_64_v2 %cxx=gcc@8.5.0`. If we find that it cant install using gcc@8, but *can* install using gcc 12, we can attempt to reinstall bamtools using `spack spec bamtools ^jsoncpp %gcc@12`



## Package Creation

### Environment Setup

Rather than doing everything from the pkgadmin account, it's encouraged to get the install working on your local user first, then push an update to the git repo, update the repo through the pkgadmin account, then install it through pkgadmin. This can/will reduce the number of half-installed packages.

To get an environment set up for development, I do the following:
```console
SPACK_PATH="${HOME}/bigdata/spack_dev"
mkdir -p ${SPACK_PATH}
cd ${SPACK_PATH}
git clone https://github.com/spack/spack.git
source ${SPACK_PATH}/spack/share/spack/setup-env.sh
cat > ${SPACK_PATH}/spack/etc/spack/repos.yaml << EOF
repos:
  hpcc:
    git: git@github.com:ucr-hpcc/hpcc-spack.git
    destination: ${SPACK_PATH}/repos/hpcc-spack
  builtin:
    destination: ${SPACK_PATH}/repos/spack-packages
EOF
spack repo update
```

From here, every time you want to develop a spack package, just be sure to source the `setup-env.sh` file located at `${SPACK_PATH}/spack/share/spack/setup-env.sh`


### Creating A Package

Whether you just need to update a version (and don't want to go through the multi-day/week process of getting it merged into the spack-packages repo) or want to add new software, you can create new spack packages in the "hpcc" namespace repo. You can find the location of the repos by using the `spack repo ls` command. **Please dont modify the builtin repo.** The builtin repo should be what Spack provides, any updates to existing packages should be copied to the hpcc_updates repo.

Creation of the initial `package.py` file can be made using the `spack create` command. For example, if the file originates on GitHub, you can copy the download from the release and use `spack create -N hpcc_pkgs https://github.com/EXAMPLE/PKG/archive/refs/tags/v9.9.9.tar.gz`. Including `-N hpcc_pkgs` is important to make sure that it's created under the hpcc_pkgs namespace, rather than builtin or hpcc_updates. This command should also grab multiple releases. I typically just grab the latest version though.


### Good Example Packages

- **From Source (CMake)**
    - [Slim (isn't the BEST example...)](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/slim/package.py)
    - [anchorwave (AVX, SSE)](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/anchorwave/package.py)
- **From Source (Makefile)**
    - [bwa_mem2](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/bwa_mem2/package.py)
    - [MCScanX](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/mcscanx/package.py)
    - [CalculiX (Good complicated install)](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/calculix/package.py)
- **From Source (Non-standard)**
    - [famsa (Custom compilation)](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/famsa/package.py)
- **Python Package**
    - [py_amptk](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/py_amptk/package.py)
- **Binary Download**
    - [Admixture](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/admixture/package.py)
    - [Aiupred](https://github.com/ucr-hpcc/hpcc-spack/blob/develop/spack_repo/hpcc_pkgs/packages/aiupred/package.py), 



## Starting from scratch

Spack should ease the herculean task of installing hundreds of pieces of software by hand. The module-logging system should give an idea on how popular software is, and *most* are available through Spack. When reinstalling, aim to just install the latest version of the packages and not worry about maintaining older versions. The exception to this would probably be for CUDA (11.8 needed for K80s) and compilers, where different versions offer flexibility for users. If a user requests an older version, then install it.


### Configuration

Before attempting to install, make sure the `packages.yaml` file has the correct compiler versions. At the time of writing, Rocky 8 provides GCC 8, and we also want to install GCC 12 and 14. In this case, the `packages.yaml` file should look like:
```yaml
packages:
  gcc:
    require:
    - one_of: ["@8", "@12", "@14"]
```
This will prioritize using GCC 8, then 12, then 14.

### Package Installation

Using the module system, you'll need to figure out all of the packages that need to be installed. Installing hundreds of packages at once should be possible, though throwing them all it might also lead to errors due to problematic packages. The first thing would be to generate a spec of all of the software (eg. `spack spec PKG1 PKG2 PKG3 .... PKGN`). You might need to use `--deprecated`, as some software might depend only on deprecated software. This might take some time (>10 minutes) to generate. If there are problematic packages, remove them to handle manually later. After that, running a `spack install PKG1 PKG2 PKG3 ... PKGN` should work to install all software.



## User Usage of Spack

We also provide Spack to our users. This is beneficial for situations where users want/need specific versions, want special compiler options, or want to build more optimized builds.
#TODO: Finish

