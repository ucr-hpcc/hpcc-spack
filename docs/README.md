# TODOs
Mention config files
    concretizer.yaml
    toolchains.yaml


# SPACK


## Introduction

Spack should *hopefully* make our lives easier when installing packages by taking the burden of compiling dependencies and software itself off of us.

Currently, Spack is installed in `/opt/linux/rocky/8.x/x86_64/`. Most/all paths mentioned from here will be relative to this directory. Configuration files are available in `spack/etc/spack`. There is a `defaults` directory containing the default configuration. **Do not edit the files in the `defaults` directory**. Instead, make/edit the files within the `spack/etc/spack` directory as they will override the settings within the corresponding `spack/etc/spack/defaults` directory.

Some config files of special importance are `config.yaml`, `repos.yaml`, and `packages.yaml`. 

`config.yaml` is currently configured to store installed packages within a `${os}/{name}/{version}-{hash}` folder structure. The default structure is fairly verbose and supports multiple architectures, though we want our installed software to be universally runnable. This file also configures the build of the software to occur in the scratch directory. This will prevent it from building in the default locations of `/tmp` or the home directory. Note that two colons are included for `build_stage`, as a single colon would append to the default list rather than override it.

`repos.yaml` configures where Spack searches for packages. We have an `hpcc` repo that is used for new packages or updates to packages. There is also Spack's built in repo. If there are updates to the repos, they can be pulled using `spack repo update` which will pull the latest updates from both repos.

`packages.yaml` configures how Spack installs packages. With `packages:all:target:` we explicitly target the `x86_64_v2` architecture. This is to accomidate the older batch and highmem nodes. If/when these are removed, the target can be increased to `x86_64_v3`. `packages:all:require:` configures spack to use GCC as the compiler when C, C++, or Fortran are required by the package. This is complemented by `packages:gcc:` to set the version preference. As of the time of writing, it's set to `["@8", "@12", "@14"]`, which will first use GCC 8 (the OS-provided version) followed by GCC 12, then GCC 14 (both need to be manually installed). `packages:all:providers:` specified which packages can provide certain features. Here we only have MPI, which can be satisfied by OpenMPI, MPICH, or Intel's OneAPI. There is `packages:all:variants:` which will attempt to build all packages as "RelWithDebInfo". This might result in larger binaries, but should hopefully allow us (and maybe the users) an easier time debugging programs if there are problems. Finally there is package-specific configuration. As of the time of writing, LLVM, openmpi, mpich, slurm, and opengl are the only manually configured packages. For LLVM, it's build with `build_type=Release`, as there were problems compiling it with debug. OpenMPI and MPICH are both build with support for Slurm, so we shouldn't need to worry about specifying that variant manually. Slurm and OpenGL are both system-provided packages, but are made visible to Spack if they're required by other packages.



## Installation of Software

When requested, software can be searched for at https://packages.spack.io/

If software is not available, see the [Package Creation](#package-creation) section. If software is available, keep reading this section.

You can see what software will be installed alongside the main package by using `spack spec PACKAGE`. When installing, there are sometimes configuration options (variants) that can enable/disable certain options. For example, `openmpi` has variants for cuda, java, gpfs, etc. Most of the time the default variants are acceptable, unless there are certain features that you know are needed or that users explicitly request. Some packages (eg. openmpi, mpich) have specific flags set globally. The config for this can be found in the `spack/etc/spack/packages.yaml` file. In the case of openmpi and mpich, they will always compile with Slurm support.

More reading on the Spack spec syntax can be found in their documentation:
https://spack.readthedocs.io/en/latest/spec_syntax.html

If the spec listed is acceptable, then it can be installed using `spack install PACKAGE`. Modifiers can be added to speed up compilation, eg `spack install -p4 -j16 PACKAGE` to install up to 4 packages in parallel, using up to 16 cores per package. Module files should also automatically be generated for newly installed packages. This is thanks to the configuration file at `spack/etc/spack/modules.yaml`.


# TODO: Finish below




## Installation Problems

#TODO
- File name too long
	- Change config:build_stage:: to "/tmp/${user}" for shorter path name
- Change build_type to Release instead of RelWithDebInfo (eg. llvm throws errors compiling with RelWithDebInfo, probably isnt too important that it's compiled w/ debug though)


### Compiler Versions

Sometimes when installing packages, compilation problems can arise. The problem I see most often is that the software needs a newer (or older) version of gcc. For example, gcc 15 changes a handful of things so older packages can't be compiled with it. The correct thing would be to submit a update to the Spack packages with a newer version or a patch to allow it to compile. The easier solution would just be to use a different compiler. Using a different version of GCC can be done as follows:

```
#TODO: Confirm this is how different compiler versions are used
spack install PACKAGENAME %gcc@14.1  # Replace 14.1 with whatever other versions are available
```

If a certain piece of software, but some dependency needs a different version, you can specify multiple different compilers using:
```
spack install PKGA %gcc@X.X.X ^PKGB %gcc@Y.Y.Y
```

This just follows the Spack spec syntax, and more information on that can be found on their [Spec Syntax](https://spack.readthedocs.io/en/latest/spec_syntax.html) page.


### Dependencies

Sometimes you'll need to manually install dependencies
#TODO


## Package Creation

Whether you just need to update a version (and don't want to go through the multi-day/week process of getting it merged into the spack-packages repo) or want to add new software, you can create new spack packages in the "hpcc" namespace repo at `$HPCC_MODULES/../spack/repo/`
#TODO

### Good Example Packages

**From Source (CMake)**: # TODO (QT?)
**From Source (Makefile)**: # TODO
**Python Package**: # TODO
**Binary Download**: # TODO (globusconnectpersonal?)



## Starting from scratch

Spack should ease the herculean task of installing hundreds of pieces of software by hand. The module-logging system should give an idea on how popular software is, and *most* are available through Spack. When reinstalling, aim to just install the latest version of the packages and not worry about maintaining older versions. The exception to this would probably be for CUDA (11.8 needed for K80s) and compilers, where different versions offer flexibility for users. If a user requests an older version, then install it.


### Compilers

Before attempting to install, make sure the `packages.yaml` file **does not** have
```yaml
packages:
  gcc:
    require:
    - one_of: [.....]
```

With no outside compilers installed, this will attempt to prioritize versions of gcc that doesn't exist. If `packages.yaml` includes this, remove it and be prepared to readd it later.

Attempt to install compilers first, these being:
```
gcc@12+binutils
gcc@14+binutils		# Some example GCC versions to install
intel-oneapi-compilers
llvm
```
**Note** the +binutils variant. Newer versions of gcc need to be compiled with binutils. This constraint *should* be automatically handled by Spack, but the `os=rhel` constraint doesn't seem to apply for Rocky, so manually add it. 

Once all compilers are installed, the `packages.yaml` file can be configured to include
```yaml
packages:
  gcc:
    require:
    - one_of: ["@8", "@12", "@14"]
```


### User Packages

#TODO: Update, the below is wrong
Attempting to install multiple packages in a single spec is generally discouraged, as it will attempt to reuse as many packages as possible. This can make it harder to install certain packages and sometimes conflict with versions.

