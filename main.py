"""
Za pomocą odpowiednich operacji połącz poniższe listy w słownik:
klucze = [1, 3, 5, 2, 4, 6]
wartosci = ['a', 'aaa', 'aaaaa', 'aa', 'aaaa', 'aaaaaa']
"""

k = [1, 3, 5, 2, 4, 6]
v = ['a', 'aaa', 'aaaaa', 'aa', 'aaaa', 'aaaaaa']

print("klucze = ", k)
print("wartości = ", v)

result = {}

for key in k:
    for values in v:
        result[key] = values
        v.remove(values)
        break
print("połączone listy w słownik =", result)
