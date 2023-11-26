#include <iostream>
#include <vector>

int main() {
    // Criando um vetor vazio de inteiros
    std::vector<int> numeros;

    // Adicionando elementos ao vetor usando o método push_back()
    numeros.push_back(10);
    numeros.push_back(20);
    numeros.push_back(30);
    numeros.push_back(40);

    // Acessando e alterando elementos usando índices
    std::cout << "Elemento no índice 2: " << numeros[2] << std::endl;
    numeros[1] = 25; // Alterando o elemento no índice 1

    // Obtendo o tamanho do vetor usando o método size()
    std::cout << "Tamanho do vetor: " << numeros.size() << std::endl;

    // Percorrendo o vetor usando um loop for
    std::cout << "Elementos do vetor:" << std::endl;
    for (size_t i = 0; i < numeros.size(); ++i) {
        std::cout << numeros[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
