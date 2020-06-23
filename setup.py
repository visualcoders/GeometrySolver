from distutils.core import setup
setup(
    name='GeometrySolver',        
    packages=['GeometrySolver'],  
    version='0.1',      
    license='MIT',
    description='A library for our school helper',
    author='Ada BERK, Demir CAVDAR.O',
    author_email='your.email@domain.com',

    url='https://github.com/user/reponame',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    
    keywords=['geometry', 'solver', 'indie'],
    install_requires=[            
        'numpy',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', 
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
