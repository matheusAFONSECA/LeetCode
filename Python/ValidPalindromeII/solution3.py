import re       # biblioteca que permite o uso de Regex
class Solution:
    def validPalindrome(self, s: str) -> bool:

        # inverte a ordem dos caracteres da string
        s_invertido = s[::-1]

        # compara a string original com a string invertida
        if s_invertido == s:
            return True
        else:
            for letra in s_invertido:       # for para passar em cada letra da string
                s_sem_letra = s.replace(letra, '')        # tira a letra da string original
                s_invertido_sem_letra = s_invertido.replace(letra, '')          # tira a letra da string invertida

                # compara se a string sem uma das letras é um palindromo
                if s_sem_letra == s_invertido_sem_letra:
                    return True
                
            return False
    