#coding: utf-8

def ComissaoSalario():
    Nome=input("Entre com o nome do vendedor: ")
    SalarioFixo=float(input("entre com o salário: "))
    Vendas=float(input("informe o total de vendas: "))
    
    Comissao=0.15*Vendas
    PagamentoEsperado=SalarioFixo+Comissao
    return Nome, Vendas, PagamentoEsperado

if __name__=="__main__":
    Nome, Vendas, PagamentoEsperado =ComissaoSalario()
    Strg="{0} obteve R$ {1:.2f} de comissao e vai receber {2:.2f}".format(Nome, Vendas, PagamentoEsperado)
    print(Strg)





