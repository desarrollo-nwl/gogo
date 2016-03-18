from distutils.core import setup
from distutils.core import Extension
MOD = "colabora"
module = Extension(MOD, sources=["colabora.cpp"],
						extra_link_args=['-std=c++11','-lpqxx','-lpq','-O3','-march=native'])
setup(name = MOD, ext_modules = [module])
