#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap; // mapa para armazenar número e índice

        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];

            // Verifica se o complemento está presente no mapa
            if (numMap.find(complement) != numMap.end()) {
                // Retorna os índices cujos números somados são iguais ao target
                return {numMap[complement], i};
            }

            // Adiciona o número atual e seu índice ao mapa
            numMap[nums[i]] = i;
        }

        // Se não houver uma solução, retorna um vetor vazio
        return {};
    }
};

int main() {
    // var aux
    vector<int> numeros;    // Criando um vetor vazio de inteiros
    vector<int> resultado;    // Criando um vetor vazio de inteiros - que guarda os resultados
    int alvo;               // definindo o alvo da soma
    Solution s;             // instanciando o objeto Solution para usar a função twoSum

    // Adicionando elementos ao vetor usando o método push_back() para adicionar valores no vetor

    // case 1
    // numeros.push_back(2);
    // numeros.push_back(7);
    // numeros.push_back(11);
    // numeros.push_back(19);

    // case 2
    // numeros.push_back(3);
    // numeros.push_back(2);
    // numeros.push_back(4);
    
    // case 3
    numeros.push_back(3);
    numeros.push_back(2);
    numeros.push_back(3);

    // definindo o alvo da soma
    
    //case 1
    // alvo = 9;

    // case 2 e 3
    alvo = 6;

    // chamando a função solution e mandando o valor para um vector
    resultado = s.twoSum(numeros, alvo);

    // mostrando os elementos do vetor numeros
    cout << "Elementos do vetor numero:" << endl;
    for (size_t i = 0; i < numeros.size(); ++i) {
        cout << numeros[i] << " ";
    }
    cout << endl;

    // elemento alvo da soma
    cout << "Elemento alvo: " << alvo << endl;

    // mostrando os elementos do vetor resultados
    cout << "Elementos do vetor de resultado:" << endl;
    for (size_t i = 0; i < resultado.size(); ++i) {
        cout << resultado[i] << " ";
    }
    cout << endl;   

    return 0;
}
