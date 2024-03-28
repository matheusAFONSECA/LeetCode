#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

class Solution {
public:
    vector< vector<int> > threeSum(vector<int>& nums) {

        // var aux
        vector< vector<int> > resultado;    // vetor de vetores que guarda o resultado

        int n = nums.size();    // tamanho do vetor
        int sum;                // soma a cada trinca
        
        // Sort na array de entrada
        sort(nums.begin(), nums.end());
        
        // iterando ao longo da array
        for (int i = 0; i < n - 2; ++i) {

            // evitando duplicatas
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            // pesquisa em dois pontos
            int left = i + 1, right = n - 1;
            while (left < right) {

                // realiza a soma do numero a esquerda, do centro e da direita
                sum = nums[i] + nums[left] + nums[right];

                if (sum == 0) {     // caso a soma seja '0' -> resultado esperado

                    // adiciona o valor da soma na lista de resoltados
                    resultado.push_back({nums[i], nums[left], nums[right]});
                    
                    // Evita duplicatas
                    while (left < right && nums[left] == nums[left + 1])
                        left++;
                    while (left < right && nums[right] == nums[right - 1])
                        right--;
                    
                    left++;     // posição do centro vira esquerda
                    right--;    // posição da direita continua

                } else if (sum < 0) {
                    left++;
                } else {
                    right--;
                }
            }

        }
        
        return resultado;       // retorna a lista de combinações
        
    }
};

int main(){
    // var
    vector<int> numeros;            // Criando um vetor vazio de inteiros
    vector< vector<int> > resultado;  // vetor de vetores que guarda os resultados dados
    Solution s;                     // instanciando o objeto solution para usa o método ThreeSum

    // cases exemplos
    // case 1
    // adicionando valores
    numeros.push_back(-1);
    numeros.push_back(0);
    numeros.push_back(1);
    numeros.push_back(2);
    numeros.push_back(-1);
    numeros.push_back(-4);

    // chamando a função solution e mandando o valor para um vector
    resultado = s.threeSum(numeros);

    cout << "-------------- CASE 1 ------------" << endl;

    // mostrando os elementos do vetor numeros
    cout << "Elementos do vetor numero:" << endl;
    for (size_t i = 0; i < numeros.size(); ++i) {
        cout << numeros[i] << " ";
    }
    cout << endl;
    // mostrando os elementos do vetor resultados
    cout << "Elementos do vetor de resultado:" << endl;
    for (size_t i = 0; i < resultado.size(); ++i) {
        cout << "Vetor " << i << ": ";
        for (size_t j = 0; j < resultado[i].size(); ++j) {
            cout << resultado[i][j] << " ";
        }
        cout << endl;
    }

    // limpando o buffer dos vetores
    numeros.clear();
    resultado.clear();


    // case 2  
    // adicionando valores
    numeros.push_back(0);
    numeros.push_back(1);
    numeros.push_back(1);

    // chamando a função solution e mandando o valor para um vector
    resultado = s.threeSum(numeros);

    cout << "-------------- CASE 2 ------------" << endl;

    // mostrando os elementos do vetor numeros
    cout << "Elementos do vetor numero:" << endl;
    for (size_t i = 0; i < numeros.size(); ++i) {
        cout << numeros[i] << " ";
    }
    cout << endl;
    // mostrando os elementos do vetor resultados
    cout << "Elementos do vetor de resultado:" << endl;
    for (size_t i = 0; i < resultado.size(); ++i) {
        cout << "Vetor " << i << ": ";
        for (size_t j = 0; j < resultado[i].size(); ++j) {
            cout << resultado[i][j] << " ";
        }
        cout << endl;
    }

    // limpando o buffer dos vetores
    numeros.clear();
    resultado.clear();


    // case 3
    // adicionando valores
    numeros.push_back(0);
    numeros.push_back(0);
    numeros.push_back(0);

    // chamando a função solution e mandando o valor para um vector
    resultado = s.threeSum(numeros);

    cout << "-------------- CASE 3 ------------" << endl;

    // mostrando os elementos do vetor numeros
    cout << "Elementos do vetor numero:" << endl;
    for (size_t i = 0; i < numeros.size(); ++i) {
        cout << numeros[i] << " ";
    }
    cout << endl;
    // mostrando os elementos do vetor resultados
    cout << "Elementos do vetor de resultado:" << endl;
    for (size_t i = 0; i < resultado.size(); ++i) {
        cout << "Vetor " << i << ": ";
        for (size_t j = 0; j < resultado[i].size(); ++j) {
            cout << resultado[i][j] << " ";
        }
        cout << endl;
    }

    // limpando o buffer dos vetores
    numeros.clear();
    resultado.clear();

    return 0;
}