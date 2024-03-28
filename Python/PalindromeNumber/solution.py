class Solution:
    def isPalindrome(self, x: int) -> bool:

        # um n° negativo não pode ser um palíndromo
        if x < int(0):
            return False
        
        else:
            # Converte o valor para uma string, inverte a ordem dos caracteres e converte de volta para inteiro
            x_invertido = int(str(x)[::-1])

            if x == x_invertido:
                return True
            else:
                return False
    