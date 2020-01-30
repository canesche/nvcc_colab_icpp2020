from distutils.core import setup

setup(
    name='NVCCPlugin',
    version='0.0.3',
    author='Andrei Nechaev, M. Canesche',
    author_email='michael.canesche@gmail.com',
    py_modules=['nvcc_plugin', 'nvcc.nvcc', 'common.helper'],
    url='htpps://github.com/canesche/nvcc_colab_icpp2020',
    license='LICENSE',
    description='Jupyter notebook plugin to run CUDA C/C++, GCC code',
    # long_description=open('README.md').read(),
)
