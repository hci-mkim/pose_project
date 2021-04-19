# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(name='rcnnpose-pytorch',
      version='0.1.0',
      description='Extracting Joint coordinates & Angles',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      author='Min Kim',
      author_email='min1106.kim@gmail.com',
      url='https://github.com/hci-mkim/pose_project.git',
      license='MIT',
      install_requires=[
              'numpy',
              'opencv-contrib-python'
      ],
      classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Education',
              'Intended Audience :: Science/Research',
              'License :: OSI Approved :: MIT License',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.7',
              'Topic :: Scientific/Engineering',
              'Topic :: Software Development :: Libraries',
              'Topic :: Software Development :: Libraries :: Python Modules',
              'Topic :: Utilities'
      ],
      keywords=[
              'rcnnpose',
              'pytorch',
              'mask-rcnn',
              'keypoint-rcnn',
              'pose-estimation',
              'keypoint-estimation',
              'computer-vision',
              'machine-learning'
      ],
      packages=find_packages())
