public class Solution {

    // metodo que calcula a soma de duas listas encadeadas depois de fazer a inversão
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // VAR AUX
        ListNode noIncial = new ListNode(0);    // Cria um nó inicial chamado noIncial com valor zero
        ListNode ultimo = noIncial;                 // Inicializa o ultimo como o nó inicial -> aux para ver quando acabar
        int i = 0;                                  // var aux de soma - "vai um" - aumenta a unidade
        int valor1;                                 // valor da l1
        int valor2;                                 // valor da l2
        int soma;                                   // guarda a soma dos dois valores
        int ValorUnidade;                           // pega o valor real da unidade de soma

        // Enquanto houver nós nas listas ou existir um "vai um" - unidade a mais a adicionar
        while (l1 != null || l2 != null || i != 0) {

            // Obtém os dígitos atuais dos nós ou assume zero se o nó for nulo
            valor1 = (l1 != null) ? l1.val : 0;     // Move l1 para o próximo nó, se não for nulo.
            valor2 = (l2 != null) ? l2.val : 0;     // Move l2 para o próximo nó, se não for nulo.

            // Calcula a soma dos dígitos atuais e do i
            soma = valor1 + valor2 + i;

            // calcula o valor que vai para o nó
            ValorUnidade = soma % 10;

            // Calcula o novo valor do i - valor que vai somar na unidade seguinte
            i = soma / 10;

            // Cria um novo nó com o dígito atual e o conecta à lista resultante
            ultimo.next = new ListNode(ValorUnidade);

            // Atualiza o ultimo para o novo último nó
            ultimo = ultimo.next;

            // Move para o próximo nó, se existir, em cada lista
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // Obtém a lista resultante, excluindo o nó inicial
        ListNode result = noIncial.next;

        // Remove a referência ao nó inicial para evitar referências indesejadas
        noIncial.next = null;

        // Retorna a lista resultante da adição das listas encadeadas l1 e l2
        return result;

    }
}
