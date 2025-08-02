# - ***Desafio 1:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# idade = []

# # - *Reservas de Quartos:*

# # ***O sistema deve oferecer 3 tipos de quartos:*** 
# # ***"Simples", "Duplo" e "Luxo".***


# # ***Cada cliente deve escolher um quarto para sua estadia.
# # O preço da diária varia conforme o tipo de quarto:
# # Simples: R$ 100,00 por dia.
# # Duplo: R$ 150,00 por dia.
# # Luxo: R$ 250,00 por dia.***
# preço_quartos = [100.00,150.00,250.00,]
# qtd_dias = []

# # - ***Cálculo da Estadia:***

# # ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# # O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

# # Exemplo: 

# #  ***valor_cliente3 = preco_duplo * cliente3_dias***
# valor_total_cliente = preço_quartos[] * qtd_dias

# # *Pagamento:*

# # *O sistema deve exibir o valor total a ser pago por cada cliente.*

# # *Regras Adicionais:
# # Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

# # ***O sistema não deve usar loops (for, while) nem funções.**
# # O código deve considerar todos os casos possíveis de escolha dos clientes.*

cadastro1 = {'nome': input('nome: '), 'idade': int(input('idade: ')), 'quarto': input('tipo de quarto: '), 'qtd_dias': int(input('qtd de dias: '))}
if cadastro1['quarto'] == 'simples':
    cadastro1['quarto'] = 100.00
elif cadastro1['quarto'] == 'duplo':
    cadastro1['quarto'] = 150.00
elif cadastro1['quarto'] == 'luxo':
    cadastro1['quarto'] = 250.00

cliente1 = [cadastro1['nome'], cadastro1['idade']]
preço_cliente1 = cadastro1['quarto'] * cadastro1['qtd_dias']

print(cliente1[0] ,'R$' , preço_cliente1)

cadastro2 = {'nome': input('nome: '), 'idade': int(input('idade: ')), 'quarto': input('tipo de quarto: '), 'qtd_dias': int(input('qtd de dias: '))}
if cadastro2['quarto'] == 'simples':
    cadastro2['quarto'] = 100.00
elif cadastro2['quarto'] == 'duplo':
    cadastro2['quarto'] = 150.00
elif cadastro2['quarto'] == 'luxo':
    cadastro2['quarto'] = 250.00

cliente2 = [cadastro2['nome'], cadastro2['idade']]
preço_cliente2 = cadastro2['quarto'] * cadastro2['qtd_dias']

print(cliente2[0] ,'R$' , preço_cliente2)

cadastro3 = {'nome': input('nome: '), 'idade': int(input('idade: ')), 'quarto': input('tipo de quarto: '), 'qtd_dias': int(input('qtd de dias: '))}
if cadastro3['quarto'] == 'simples':
    cadastro3['quarto'] = 100.00
elif cadastro3['quarto'] == 'duplo':
    cadastro3['quarto'] = 150.00
elif cadastro3['quarto'] == 'luxo':
    cadastro3['quarto'] = 250.00

cliente3 = [cadastro3['nome'], cadastro3['idade']]
preço_cliente3 = cadastro3['quarto'] * cadastro3['qtd_dias']



print(cliente3[0] ,'R$' , preço_cliente3)
