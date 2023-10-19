from setuptools import setup

setup(
    name='modneat-python',
    version='0.0.9',
    author='kato-mahiro, cesar.gomes, mirrorballu2',
    author_email='katomasahiro10@gmail.com',
    maintainer='kato-mahiro',
    maintainer_email='katomasahiro10@gmail.com',
    url='https://github.com/kato-mahiro/modneat-python',
    license="BSD",
    description='A Modulatory NEAT (NeuroEvolution of Augmenting Topologies) implementation',
    long_description='Python implementation of NEAT (NeuroEvolution of Augmenting Topologies), a method ' +
                     'developed by Kenneth O. Stanley for evolving arbitrary neural networks.',
    packages=['modneat', 'modneat/iznn', 'modneat/nn', 'modneat/ctrnn', 'modneat/report_utils'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering'
    ]
)
