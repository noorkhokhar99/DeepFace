from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import subprocess
import setuptools

_VERSION = '0.1.1'

cwd = os.path.dirname(os.path.abspath(__file__))
subprocess.check_output(["bash", "deepface/detectors/dlib/download.sh"], cwd=cwd)
subprocess.check_output(["bash", "deepface/detectors/ssd/download.sh"], cwd=cwd)
subprocess.check_output(["bash", "deepface/recognizers/vggface/download.sh"], cwd=cwd)
subprocess.check_output(["bash", "deepface/recognizers/vggface2_resnet/download.sh"], cwd=cwd)

# 'opencv-python >= 3.3.1'
REQUIRED_PACKAGES = [
    'tensorflow >= 1.7.0',
    'dill >= 0.2.7.1',
    'dlib==19.12.0',
    'h5py >= 2.8.0',
    'matplotlib >= 2.2.2',
    'numpy >= 1.14.3',
    'pyyaml >= 3.0.0',
    'scikit-learn >= 0.18.1',
    'scikit-image >= 0.13.1',
    'scipy >= 1.1.0',
    'tqdm >= 4.23.4',
]

DEPENDENCY_LINKS = [
]

setuptools.setup(
    name='deepface',
    version=_VERSION,
    description=
    'Deep Learning Models for Face Detection/Recognition/Alignments, implemented in Tensorflow',
    install_requires=REQUIRED_PACKAGES,
    dependency_links=DEPENDENCY_LINKS,
    url='https://github.com/ildoonet/deepface',
    license='Apache License 2.0',
    package_dir={},
    packages=setuptools.find_packages(exclude=['tests']),
    package_data={'deepface': ['detectors/dlib/shape_predictor_68_face_landmarks.dat',
                               'detectors/ssd/graph_inception_v2_fddb.pb',
                               'detectors/ssd/graph_mobilenet_v2_fddb_180627.pb',
                               'detectors/ssd/graph_mobilenet_v2_all_180627.pb',
                               'confs/basic.yaml',
                               'recognizers/vggface/weight.mat',
                               'recognizers/vggface/db_blackpink.pkl',
                               'recognizers/vggface2_resnet/db_blackpink.pkl',
                               'recognizers/vggface2_resnet/labels.npy',
                               'recognizers/vggface2_resnet/weight.h5']
                  },
)
