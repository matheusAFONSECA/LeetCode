class Solution:
    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        # Função para verificar se a substring é um palíndromo
        while left < right:
            if s[left] != s[right]:
                # Se os caracteres não forem iguais, não é um palíndromo
                return False
            # Move os ponteiros para o centro da string
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        # Dois ponteiros para percorrer a string da esquerda para a direita e da direita para a esquerda
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # Se os caracteres não forem iguais, tentamos ignorar um deles
                # e ver se a substring restante é um palíndromo
                return self.is_palindrome(s, left + 1, right) or \
                       self.is_palindrome(s, left, right - 1)
            # Move os ponteiros para a próxima posição
            left += 1
            right -= 1
        # Se chegarmos ao final do loop sem retornar False, a string é um palíndromo
        return True
