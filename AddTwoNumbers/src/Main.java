public class Main {
    public static void main(String[] args) {

        // Criando uma lista encadeada com três nós
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);

        // Estabelecendo as conexões entre os nós
        node1.next = node2;
        node2.next = node3;

        // Percorrendo e imprimindo os valores da lista encadeada
        ListNode current = node1;
        while (current != null) {
            System.out.println(current.val);
            current = current.next;
        }

    }
}