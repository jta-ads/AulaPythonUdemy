from datetime import datetime
from dateutil.relativedelta import relativedelta

emprestimo = 1_000_000

data_emprestimo = datetime(2020, 12, 20)

delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = emprestimo / numero_parcelas

for data in data_parcelas:
     data = datetime.strftime(data,'%d/%m/%Y')
     print(data, f'R${valor_parcela:,.2f}')

print()
print(
     f'Seu emprestimo é R$ {emprestimo:,.2f}'
     f' Para pagar em {delta_anos.years} anos '
     f'({numero_parcelas} meses) em parcelas de '
     f'R${valor_parcela:,.2f}'
)