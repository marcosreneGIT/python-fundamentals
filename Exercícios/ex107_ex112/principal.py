from ex107_ex112.utilidadesCeV import moeda
from ex107_ex112.utilidadesCeV import dado

preco = dado.leia_dinheiro('Informe o preço: R$')
moeda.resumo(preco, 20, 20)
