
"""Zadanie 3.
Liderem nazywamy element, który występuje więcej niż 𝑘
2
, gdzie 𝑘 jest liczbą rozpatrywanych elementów. Załóżmy, że mamy ciąg liczb całkowitych zapisanych na papierowej taśmie. Zakładając ponadto,
że na taśmie znajduje się lider, zastanawiamy się, na ile sposobów możemy przeciąć taśmę na dwie
części w taki sposób, by na obu znalazł się lider, którego wartość jest taka sama.
Przykład danych wejściowych:
6
4 3 4 4 4 2
Wyjście:
2
Komentarze:
1. W pierwszym wierszu wejścia znajduje się liczba całkowita 2 ≤ 𝑛 ≤ 10000, która oznacza liczbę
liczb na taśmie. Drugi wiersz wejścia zawiera ciąg liczb całkowitych z przedziału (−10000; 10000).
2. Liczba 2 na wyjściu oznacza, że taśmę można przeciąć na dwa sposoby, tj. zawierający liczbę 4 i 3
4 4 4 2 albo 4 3 4 i 4 4 2. Tylko w ten sposób spełnimy warunki zadania.
Na podstawie powyższych informacji napisz program, który realizuje powyższy algorytm w oparciu o
dane wprowadzone przez użytkownika i/lub wczytuje z pliku tekstowego. Program powinien poinformować użytkownika o liczbie cięć oraz o liczbach na obu częściach taśmy, a także zapisać wyniki w
nowym pliku tekstowym."""


from typing import Optional

k = 6
numbers = [5, 3, 5, 5, 5, 2]


def find_leader(nums: list[int]) -> Optional[int]:
    counts = {nums.count(x): x for x in set(nums)}
    if max(counts.keys()) > len(nums) // 2:
        return counts[max(counts.keys())]


def calculate_ways(nums: list[int]) -> int:
    result = 0
    for i in range(1, len(nums)):
        if find_leader(nums[:i]) == find_leader(nums[i:]):
            result += 1
    return result


print(calculate_ways(numbers))
