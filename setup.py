from setuptools import setup

setup(name='cpf_cnpj_validate',
      version='1.6.0',
      description='Python module for brazilian register numbers for persons (CPF) and companies (CNPJ) and mask generator to string or int CPF/CNPJ.',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9'
          'Programming Language :: Python :: 3.10'
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='cpf cnpj validation generation mask',
      url='https://github.com/andrersp/pycpfcnpj',
      author='André França',
      author_email='rsp.assistencia@gmail.com',
      license='MIT',
      packages=['cpf_cnpj_validate'],
          test_suite='nose.collector',
          tests_require=['nose'],
      zip_safe=False)
