
from . import cpf
from . import cnpj


def mask_cpf_cnpj(cpf_cnpj: str):

    cpf_cnpj_str = f'{cpf_cnpj}'
    cpf_cnpj = "".join([x for x in f'{cpf_cnpj_str}' if x.isnumeric()])

    if len(cpf_cnpj) <= 6:
        cpf_cnpj = cpf_cnpj.zfill(6)
    elif len(cpf_cnpj) >= 12:
        cpf_cnpj = cpf_cnpj.zfill(14)
    else:
        cpf_cnpj = cpf_cnpj.zfill(11)

    if cpf.validate(cpf_cnpj):
        return f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}'
    elif cnpj.validate(cpf_cnpj):
        return f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:14]}'
    elif len(cpf_cnpj) == 6:
        return f"***.{cpf_cnpj[:3]}.{cpf_cnpj[3:]}-**"
    return cpf_cnpj_str
