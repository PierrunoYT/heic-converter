from setuptools import setup, find_packages

setup(
    name='heic-converter',
    version='0.1.0',
    description='A simple HEIC image converter',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/heic-converter',
    packages=find_packages(),
    install_requires=[
        'pillow-heif>=0.20.0',
        'Pillow>=10.1.0',
    ],
    entry_points={
        'console_scripts': [
            'heic-converter=heic_converter:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='heic converter image',
    python_requires='>=3.7',
)