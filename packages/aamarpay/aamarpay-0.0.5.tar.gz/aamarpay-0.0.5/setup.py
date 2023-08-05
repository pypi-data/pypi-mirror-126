import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

requires = [

    'requests==2.26.0',
]
setuptools.setup(
    name='aamarpay',
    version='0.0.5',
    description='Payment gateway libarary',
    long_description='long_description',
    url='https://github.com/sanjidbillah/aamarPay-python',
    author='Masum billah sanjid',
    author_email='masumbillahsanjid@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='Payment',
    packages=setuptools.find_packages(),
    install_requires=requires
)
