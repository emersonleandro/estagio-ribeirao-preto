def verifica_letra_a(string):
    # Converte a string para minúsculas para tratar 'A' e 'a' de forma unificada
    string_minuscula = string.lower()
    
    # Conta a ocorrência da letra 'a'
    contagem = string_minuscula.count('a')
    
    # Verifica se a letra 'a' existe na string
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# String a ser verificada
string = input("Informe uma string: ")
verifica_letra_a(string)
