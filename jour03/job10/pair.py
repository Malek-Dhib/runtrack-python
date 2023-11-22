def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            return "Pair"
        else:
            return "Impair"
    else:
        return "Le nombre n'est pas un entier positif."

result1 = verifier_pair_impair(4)
print("Résultat 1:", result1)

result2 = verifier_pair_impair(7)
print("Résultat 2:", result2)

result3 = verifier_pair_impair(0)
print("Résultat 3:", result3)

result4 = verifier_pair_impair(11)
print("Résultat 4:", result4)

result5 = verifier_pair_impair(-3)
print("Résultat 5:", result5)

result6 = verifier_pair_impair(2.5)
print("Résultat 6:", result6)
