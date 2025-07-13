package prubeas;
import static prubeas.LinkedLists_ReverseSingleLinkedList.ListNode;


/*  
Original: 
1 -> 2 -> 3 -> 4 -> 5 -> null
Reversed: 
5 -> 4 -> 3 -> 2 -> 1 -> null 
 * */


public class LinkedLists_ReverseSingleLinkedList {
	
	
	/*
	  Esta es una clase estatica que sirve para representar un nodo de la clase enlazada
	  val: el valor almacenado en el nodo
	  next: referencia al siguiente nodo en la lista
	  
	  Constructores:
	  Constructor vacío (sin parámetros).
	  Constructor que asigna solo el valor.
	  Constructor que asigna valor y referencia al siguiente nodo.
	  
	  Es estatica para poder crear nodos sin la necesidad de crear primero una instancia de la clase externa
	*/
	
	static class ListNode{
//		+---+---+    +---+---+    +---+---+    +---+---+    +---+---+
//		  | 1 | *----> | 2 | *----> | 3 | *----> | 4 | *----> | 5 | *----> null
//		+---+---+    +---+---+    +---+---+    +---+---+    +---+---+
		int val;   // declara una variable para almacenar el valor del nodo (en este caso es un entero)
		ListNode next;  // esta es una referencia (como un puntero en C++), si este es el ultimo, debe ser null

		ListNode(){	
		}//constructor vacio -- nodo vacio
		ListNode(int val){
			this.val = val;
		}//constructor de valor -- 1 nodo y su valor
		ListNode(int val, ListNode next){ 
			this.val = val;
			this.next = next;
		}//constructor of val and next -- 1 nodo y su valor y lo enlaza inmediatamente con el siguiente nodo
	}//class
	
	/*
	 * Esta clase tiene los metodos que manipulan la lista enlazada.
	 * reverseList  invierte la lista enlazada y devuelve la cabeza de la lista invertida
	 * printList imprime todos los valores de la lista enlazada en orden
	 * TRES REFERENCIAS: prev, current y next temp
	 * */
	static class Solution {
		public ListNode reverseList(ListNode head) {
			ListNode prev = null;  //almacena el nodo invertido mas reciente
			ListNode current = head; // recorre la lista original
			// cada iteracion cambia el puntero next del nodo actual para que apunte al nodo anterior
			// al final prev es el nuevo comienzo  de la lista invertida 
			while (current != null) {
				ListNode nextTemp = current.next;  //guardar el siguiente nodo
				current.next = prev;				// invertir el enlace actual
				prev = current;						// mover prev hacia adelante
				current = nextTemp;					// mover current hacia adelante
			}
			return prev; // nuevo head de la lista invertida
		}//reverseList
		
		//metodo para imprimir una lista
		
		// recorre la lista desde head, imprime cada valor seguido de una flecha  para indicar la direccion
		// cuando llega al final head == null, imprimie null
		public void printList(ListNode head) {
			while(head != null) {
				System.out.print(head.val + " -> ");
				head = head.next;
			}//while
			System.out.println("null");
		}//printList
		
		//metodo main para probar la solucion
		public static void main(String[] args) {
			
			/*
			 * Crea una lista enlazada con los valores: 1 -> 2 -> 3 -> 4 -> 5.

Crea un objeto Solution para usar los métodos.

Imprime la lista original.

Invierte la lista.

Imprime la lista invertida.

5. Sobre la organización y uso de clases anidadas
Al declarar ListNode y Solution como static dentro de la clase externa, puedes usarlas sin crear primero un objeto de la clase externa.

Para evitar escribir nombres largos en main, es común poner el main en la clase externa, no dentro de Solution.

Esto permite escribir simplemente:

java
Copy
Edit
ListNode head = new ListNode(...);
Solution sol = new Solution();
sin prefijos largos.
			 * */
			
			//crear la lista A -> B -> C -> D -> F
		ListNode head = new ListNode(1,
								new ListNode(2,
										new ListNode(3, 
												new ListNode(4,
														new ListNode(5)))));
		Solution sol = new Solution();
		System.out.println("Original: ");
		sol.printList(head);
		
		ListNode reversed = sol.reverseList(head);
		
		System.out.println("Reversed: ");
		sol.printList(reversed);
		}//main
	}//solution
}//BClass
