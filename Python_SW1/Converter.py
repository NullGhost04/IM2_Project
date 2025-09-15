def convert_currency(dolyar, peso=57.17, japanyen=146.67):
    results = []
    for d in dolyar:
        convertpeso = d * peso
        convertyen = d * japanyen
        results.append((d, convertpeso, convertyen))
    return results

inputhere = input("Enter currency in ($): ")
dolyarlist = [int(x.strip()) for x in inputhere.split(",")]

results = convert_currency(dolyarlist)

print(f"\n{'Dollar($)':<10}{'Phil Peso(P)':<15}{'Jpn Yen(Y)':<15}")
for d, p, y in results:
    print(f"{d:<10}{p:<15.2f}{y:<15.2f}")