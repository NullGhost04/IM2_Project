def converternidiscaya(*dolyar, **bigayan):
    results = []
    for d in dolyar:
        peso = d * bigayan["peso"]
        yen = d * bigayan["yen"]
        results.append([d, peso, yen])
    return results


results = converternidiscaya(59, 200, 500, peso=57.17, yen=146.67)

print(f"{'dolyar($)':<10}{'peso(P)':<15}{'yen(Y)':<15}")
for row in results:
    print(f"{row[0]:<10}{row[1]:<15.2f}{row[2]:<15.2f}")