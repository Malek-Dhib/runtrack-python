def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erreur : Division par zéro"
    elif operator == '%':
        if num2 != 0:
            return num1 % num2
        else:
            return "Erreur : Division par zéro"
    else:
        return "Opérateur non valide"

result1 = calcule(12, '+', 3)
print("Résultat 1:", result1)

result2 = calcule(6, '*', 4)
print("Résultat 2:", result2)

result3 = calcule(12, '/', 4)
print("Résultat 3:", result3)
