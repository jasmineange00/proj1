def convert_to_peso_yen(dollar_amount):
    yen_rate = 146.67
    peso_rate = 57.17
    return dollar_amount * yen_rate, dollar_amount * peso_rate

currency = [59, 200, 500]
nestedListYen = []
nestedListPeso = []

for amount in currency:
    yen, peso = convert_to_peso_yen(amount)
    nestedListYen.append([yen])
    nestedListPeso.append([peso])

print(f"{'USD':>6}  {'YEN':>10}  {'PESO':>10}")
for i in range(len(currency)):
    usd = currency[i]
    yen = nestedListYen[i][0]
    peso = nestedListPeso[i][0]
    print(f"{usd:>6}  {yen:>10.2f}  {peso:>10.2f}")
