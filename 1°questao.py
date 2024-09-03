def fibonacci(n):
    # Inicia a sequência de Fibonacci com os primeiros dois números
    fib_sequence = [0, 1]
    
    # Calcula os próximos números da sequência até alcançar ou ultrapassar n
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    return fib_sequence

def verifica_fibonacci(numero):
    # Gera a sequência de Fibonacci até o número fornecido
    fib_sequence = fibonacci(numero)
    
    # Verifica se o número informado pertence à sequência
    if numero in fib_sequence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

# Número a ser verificado
numero = int(input("Informe um número: "))
verifica_fibonacci(numero)
