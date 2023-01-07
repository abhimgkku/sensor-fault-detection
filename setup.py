#just to create proper package libraires to share accross systems.
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function returns a list of packages required"""
    requiremnt_list:List[str] = []
    return requiremnt_list
    
setup(
    name = 'sensor',
    version ='0.0.1',
    authour = 'Abhinav Kumar',
    authour_email = 'abhinav.mg.k@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements(),
) 
