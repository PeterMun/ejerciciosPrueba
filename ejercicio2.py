def solve(S):
    # cuentas la frecuencua de los caracteres
    contrador_caracteres = [0] * 26
    for char in S:
        contrador_caracteres[ord(char) - ord('a')] += 1

    # Contar cuántos caracteres tienen un recuento impar
    odd_count = sum(count % 2 for count in contrador_caracteres)

    # palindromo
    if odd_count <= 1:
        return 0

    operations = 0
    for count in contrador_caracteres:
        if count % 2 != 0:
            operations += 1
    return operations - 1

S = input("Ingrese una cadena: ")
print(solve(S))
