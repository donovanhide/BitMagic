###
### copy this file to local_build.py and edit to suit
### for compiler flags and such influencing the optimisation
### of the BitMagic library
###

### for the 64 bit version
define_macros = [ ("BM64OPT", None) ]

### for Intel CPUs
extra_compile_args = ["-m64", "-msse2"]
### for AMD64
#extra_compile_args = ["-mtune=athlon64"]

### libraries in funny places
include_dirs = ["/usr/local/include"]
library_dirs = ["/usr/local/lib"]
