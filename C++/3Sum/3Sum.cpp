#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector< vector<int> > threeSum(vector<int>& nums) {

        vector< vector<int> > resultado;
        vector<int> v1, v2, v3;

        v1.push_back(1);
        v1.push_back(2);
        v1.push_back(3);

        v2.push_back(4);
        v2.push_back(5);
        v2.push_back(6);

        v3.push_back(7);
        v3.push_back(8);
        v3.push_back(9);

        resultado.push_back(v1);
        resultado.push_back(v2);
        resultado.push_back(v3);

        return resultado;
        
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