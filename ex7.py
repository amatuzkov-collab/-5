n, k, m = map(int, input().split())

pryamo = abs(k - m)
naoborot = n - pryamo

otvet = min(pryamo, naoborot) - 1
print(otvet)
