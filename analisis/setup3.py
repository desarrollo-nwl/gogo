from distutils.core import setup
from distutils.core import Extension
MOD = "focal"
module = Extension(MOD, sources=["focal.cpp"],
						extra_link_args=['-std=c++11','-lpqxx','-lpq','-O3','-march=native'])
setup(name = MOD, ext_modules = [module])
