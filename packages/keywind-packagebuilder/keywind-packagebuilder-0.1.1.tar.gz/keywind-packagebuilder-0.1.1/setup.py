import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()
setuptools.setup(
	name="keywind-packagebuilder",
	version="0.1.1",
	author="Keywind",
	author_email="keywind127@gmail.com",
	description="Installing this package will allow you to build python packages with ease.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/keywind1207/keywind-packagebuilder",
	project_urls={
		"Bug Tracker": "https://github.com/keywind1207/keywind-packagebuilder/issues",
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
        install_requires=[
        	'markdown',
		'twine',
		'build'
	]
)