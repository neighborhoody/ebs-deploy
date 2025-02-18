from setuptools import setup

setup(

    # general meta
    name='ebs-deploy',
    version='2.0.1',
    author='Brian C. Dilley',
    author_email='brian.dilley@gmail.com',
    description='Python based command line tools for managing '
                'Amazon Elastic Beanstalk applications.',
    platforms='any',
    url='https://github.com/briandilley/ebs-deploy',
    download_url='https://github.com/briandilley/ebs-deploy',

    # packages
    packages=[
        'ebs_deploy',
        'ebs_deploy.commands'
    ],

    # dependencies
    install_requires=[
        'boto>=2.45.0',
        'pyyaml==5.1'
    ],
    # additional files to include
    include_package_data=True,

    # the scripts
    scripts=['scripts/ebs-deploy'],

    # wut?
    classifiers=['Intended Audience :: Developers']
)
