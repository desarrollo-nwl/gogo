from distutils.core import setup
from distutils.core import Extension
MOD = "analisis_cpp"
module = Extension(MOD, sources=["analisis_cpp.cpp"],
	extra_link_args=['-I/usr/include/ctemplate','-std=c++11','-lpqxx','-lpq','-lctemplate','-pthread','-O3','-march=native'])
setup(name = MOD, ext_modules = [module])
