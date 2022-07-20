from setuptools import setup, find_packages

setup(
	name='smsjet',
	version='0.1.0',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	url='https://github.com/illegalbyte/smsjet-pip',
	license='MIT',
	keywords='sms smsjet cli',
	author='IllegalByte',
	install_requires=[
		"requests",
	]
)