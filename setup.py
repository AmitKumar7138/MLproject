from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path)->List[str]:
    '''
    this function will return liat of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(HYPEN_E_DOT)
            
    return requirements
    

setup(
    name = 'MLproject',
    version= '0.0.1',
    author= 'Amit Kumar',
    author_email='amitprataprana41@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt'),
    
) 
