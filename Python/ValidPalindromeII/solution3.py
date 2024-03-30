import re       # biblioteca que permite o uso de Regex
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # transformando as letras da string em minusculas
        s = s.lower()

        # remove os caracteres especiais que a strins 's' possui
        s_caracteres = re.sub(r'[^a-zA-Z0-9]', '', s)

        # inverte a ordem dos caracteres da string
        s_invertido = s_caracteres[::-1]

        # compara a string original com a string invertida
        if s_invertido == s_caracteres:
            return True
        else:
            return False
    