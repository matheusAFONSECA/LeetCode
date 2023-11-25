public class Main {
    public static void main(String[] args) {

        // TESTE USANDO DUAS LISTAS DE LISTNODE

        // instanciando o objeto "solution" - solução - para usar o método addTwoNumbers
        Solution s1 = new Solution();

        // Criando a primeira lista encadeada l1 = [9,9,9,9,9,9,9]
        ListNode l1 = new ListNode(9);
        l1.next = new ListNode(9);
        l1.next.next = new ListNode(9);
        l1.next.next.next = new ListNode(9);
        l1.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next = new ListNode(9);
        l1.next.next.next.next.next.next = new ListNode(9);

        // Criando a segunda lista encadeada l2 = [9,9,9,9]
        ListNode l2 = new ListNode(9);
        l2.next = new ListNode(9);
        l2.next.next = new ListNode(9);
        l2.next.next.next = new ListNode(9);

        // Chamando o método addTwoNumbers para somar as listas encadeadas
        ListNode resultado = s1.addTwoNumbers(l1, l2);

        // Exibindo o resultado da soma das listas encadeadas
        while (resultado != null) {
            System.out.print(resultado.val + " ");
            resultado = resultado.next;
        }

    }
}