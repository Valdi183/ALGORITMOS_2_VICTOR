#Recursividad para calcular el factorial de un número.
"""
El proceso que utiliza este algoritmo para hallar el factorial se divide en dos sencillos pasos:
    1. Si el número es 0, devolver 1 (caso base del algoritmo).
    2. En caso contrario, devolver el número multiplicado por el factorial del número menos 1 (hasta
    llegar al caso base del algoritmo)
"""
def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
    if n == 0:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva


def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    