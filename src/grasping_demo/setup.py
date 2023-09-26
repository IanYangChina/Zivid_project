## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml-DPYTHON_VERSION=2.7
setup_args = generate_distutils_setup(
    packages=['pcd_processing', 'utils'],
    package_dir={'': 'src'},
    requires=['open3d', 'numpy-quaternion', 'numba==0.47']
)

setup(**setup_args)
