Pycpfcnpj
=======

Description
-----------
Python module for brazilian register numbers for persons (CPF) and companies (CNPJ). If want this validation in your web application, please check [my tiny web component](https://github.com/matheuscas/wc-input-cpf-cnpj) that does exactly that. ;)

**Python 3 ready!**

[![Build Status](https://travis-ci.org/matheuscas/pycpfcnpj.png?branch=master)](https://travis-ci.org/matheuscas/pycpfcnpj)
[![codecov](https://codecov.io/gh/matheuscas/pycpfcnpj/branch/master/graph/badge.svg)](https://codecov.io/gh/matheuscas/pycpfcnpj)
[![PyPI version](https://badge.fury.io/py/pycpfcnpj.svg)](https://badge.fury.io/py/pycpfcnpj)
![Python versions](https://img.shields.io/pypi/pyversions/pycpfcnpj)



#### Related projects
- [Pycnpj-crawler](https://github.com/matheuscas/pycnpj-crawler): Python module that crawls data for a given CNPJ on the government website of each state (please check the supported states).
-  Library forked from [pycpfcnpj](https://github.com/matheuscas/pycpfcnpj)
- The main purpose of the fork was to add mask for cpf or cnpj from int or string.


### How to install
Now you can install this module with pip! Yeah! :D

```
pip install cpf-cnpj-validate
```

### Quick Start
To use pycpfcnpj is simples like as every python module should be!

```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'

print cpfcnpj.validate(cpf_number)
print cpfcnpj.validate(masked_cpf_number)
print cpfcnpj.validate(cnpj_number)
print cpfcnpj.validate(masked_cnpj_number)

Expected output:
>>>True
>>>True
>>>True
>>>True
```
Simple like that. =)

You can use, as well, the cpf and cnpj packages. The cpfcnpj is like a Facade to the other modules. Make yourself confortable.

Oh, fork and contribute either if you want to.

Obs.: There is no dependencies.

Oh, and before I forget, You can generate, only and only for test purposes, a CPF or CNPJ number using the 'gen' module. Easy like above:

```python
from pycpfcnpj import gen
gen.cpf()
gen.cnpj()

Expected output:
>>> 49384063495
>>> 20788274885880
```

And you also can generate CPF or CǸPJ with punctuation marks. :)

```python
from pycpfcnpj import gen
gen.cpf_with_punctuation()
gen.cnpj_with_punctuation()

Expected output:
>>> 048.891.866-97
>>> 63.212.638/0361-35
```

And you also can format a cpf or cnpj number with valid mask

```python
from pycpfcnpj import mask
only_number_cnpj: str = "63212638036135"
with_mask_cnpj: str = mask.mask_cpf_cnpj(only_number_cnpj)
only_number_cpf: int = 4889186697
with_mask_cpf: str = mask.mask_cpf_cnpj(only_number_cpf)
print(with_mask_cnpj)
print(with_mask_cpf)

Expected output:
>>> 63.212.638/0361-35
>>> 048.891.866-97
```
Have fun!

In portuguese:
--------------

Módulo python para validar números de CPF e CNPJ.

### Como instalar:
Agora você pode instalar o pycpfcnpj usando o pip!\m/

```
pip install cpf-cnpj-validate
```

#### Projetos relacionados
- [Pycnpj-crawler](https://github.com/matheuscas/pycnpj-crawler)

### Como usar
```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'

print cpfcnpj.validate(cpf_number)
print cpfcnpj.validate(cpf_number_mascara)
print cpfcnpj.validate(cnpj_number)
print cpfcnpj.validate(cnpj_number_mascara)

Expected output:
>>>True
>>>True
>>>True
>>>True
```

Simples assim! Você também pode usar os pacotes internos que tratam em separado os números de CPF e CNPJ. O módulo 'cpfcnpj' é um tipo de interface para os módulos mais especificos e se encarrega de saber quando você está passando um CPF ou um CNPJ.

Fique à vontade em contribuir com o projeto ou da maneira que quiser. Ah, sim: pure python (sem dependências ;) ).

Ah, e antes que eu me esqueça, você pode gerar, só e apenas somente para fins de teste, um número de CPF ou CNPJ utilizando o módulo 'gen'. Fácil como acima:

```python
from pycpfcnpj import gen
gen.cpf()
gen.cnpj()

Expected output:
>>> 49384063495
>>> 20788274885880
```

E você também pode gerar CPF ou CNPJ com pontuação :)

```python
from pycpfcnpj import gen
gen.cpf_with_punctuation()
gen.cnpj_with_punctuation()

Expected output:
>>> 048.891.866-97
>>> 63.212.638/0361-35
```


Divirta-se!

Changelog
-----------
1.6.0
- Remove python 2.7 support
- Add python 3.8 support

1.1
- Handles CPF and CNPJ numbers with punctuation marks.

1.2
- Use `sys` rather than `six` to check python's version and keeps this project 100% free of dependencies.

1.3
- Generate CPF and CNPJ numbers with punctuation marks.

1.4
- Adding support to unicode values.

1.5
- Better CPF and CNPJ generation

1.5.1
- Use regex to remove punctuation


Log de mudanças
-----------
1.6.0
- Remove suporte para python 2.7
- Adiciona suporte para python 3.8

1.1
- Trata números de CPF e CPNJ com sinais de pontuação

1.2
- Uso do `sys` em vez do `six` para verificar a versão do Python e evitando o uso de libs terceiras

1.3
- Gera números de CPF e CNPJ com pontuação.

1.4
- Suporte a unicode.

1.5
- Geração de CPF e CNPJ mais eficiente.

1.5.1
- Regex para remover a pontuação.
