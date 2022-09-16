from setuptools import setup

package_name = 'ros2_course_python'

setup(
    name=package_name,
    version='0.0.1',
    packages=[],
    py_modules = ['talker'],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Charles Stolz',
    author_email='charles.stolz@torc.ai',
    maintainer='Charles Stolz',
    maintainer_email='charles.stolz@torc.ai',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='ROS2 course examples',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_py_node = talker:main',
        ],
    },
)
