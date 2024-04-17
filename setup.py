from setuptools import setup, find_packages

setup(
    name='gemstone_price_prediction', 
    version='0.1.0',  # Initial development version
    author='Girupa Shankar', 
    author_email='girupashankar20@example.com',  
    description='A data science project to predict gemstone prices.',  # Short description
    long_description=open('README.md').read(),  # Long description from the README
    long_description_content_type='text/markdown',  # Specifies that long description is Markdown
    url='https://github.com/girupashankar/gemstonePricePrediction',  # Link to your project repository
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        'numpy',  
        'pandas',
        'scikit-learn',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Assuming your project is MIT Licensed
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8', 
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',  # Minimum version requirement of Python
    entry_points={  # Allows you to make command-line executables
        'console_scripts': [
            'predict_prices=gemstone_price_prediction.main:main',  # Adjust this to your package and entry function
        ],
    },
    keywords='data science machine learning gemstone price prediction',  # Relevant keywords
    project_urls={  # Additional URLs that are relevant to your project
        'Bug Reports': 'https://github.com/girupashankar/gemstonePricePrediction/issues',
        'Source': 'https://github.com/girupashankar/gemstonePricePrediction',
    },
)
