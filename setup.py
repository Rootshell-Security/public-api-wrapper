from setuptools import setup, find_packages

setup(
    name='rootshell_platform_api',
    version='0.2.0',
    description='A Package to interact with Rootshells Public API',
    long_description=open('README_PI.md').read(),
    long_description_content_type='text/markdown',
    author='Chris',
    author_email='chris.mills@rootshellsecurity.net',
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.3',
        'python-dotenv>=1.0.1',
        'click>=8.1.7',
    ],
    extras_require={
        'dev': [
            'requests-mock>=1.12.1',
        ],
    },
    entry_points={
        'console_scripts': [
            'rootshell_platform = rootshell_platform_api.cli:cli',
        ],
    },
    python_requires='>=3.7',
)
