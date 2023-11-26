#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // var aux
        vector<int> result;         // definindo um vetor aux para pegar as posições
        int sum = 0;                // guarda a soma
        int verifica = target;      // ajuda a verificar se a resposta foi a certa
        int i = 0;                  // var de controle do for
        int j = 0;                  // var de controle do while

        while(j != -1)
        {
            // passando pelo vetor
            for(i; i < nums.size(); i++){

                // realizando a soma do valor
                sum = sum + nums[i];
                // cout << "soma:" << sum << endl;

                // definindo condição para pegar a posição do vetor
                if (sum <= target)
                {
                    result.push_back(i);    // pegando a posição do vetor
                    verifica = sum;
                }
                
            }

            // verifica se pode sair do while -> caso contrário faz o for novamente, mas com uma posição na frente
            if (verifica != target)
            {
                j++;                // incrementa a posição que o loop for vai começar
                i = j;              // define a nova posição que o loop for vai ocorrer
                sum = 0;            // zera a soma
                result.clear();     // limpa as posições pegas de forma errada

                if (j == nums.size())   // caso não tenha como conseguir o valor alvo
                {
                    j = -1;             // sai do loop while
                    result.clear();     // limpa as posições pegas de forma errada
                }
                
            } else {
                j = -1;             // sai do loop while
            }
        }
        
        // retornando os vetores
        return result;
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



    // Obtendo o tamanho do vetor usando o método size()
    cout << "Tamanho do vetor: " << numeros.size() << endl;    

    return 0;
}
