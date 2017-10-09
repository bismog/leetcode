from distutils.core import setup, Extension
 
module1 = Extension('jay',
                    sources = ['cmodule.c'])
 
setup(name = 'jay',
      version = '1.0',
      description = 'This is a demo package from Jay.',
      ext_modules = [module1])

