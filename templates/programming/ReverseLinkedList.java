package com.ms.banking.rsm.dto;

public class ReverseLinkedList {

	
	private static class SinglyLinkedList {
		
		Node head;
		
		
		
		// prints content of double linked list
	    void printList(Node node) {
	        while (node != null) {
	            System.out.print(node.data + " ");
	            node = node.next;
	        }
	    }
	    
	    
	    
	    Node reverseV2( Node node, Node previous) {
	    	
//	    	System.out.println(node.data + "->" + (previous == null ? "null" : previous.data) );
	    	
	    	if ( node.next != null) {
	    		
	    		Node next1 = node.next;
	    		
	    		node.next = previous;
	    		
	    		return reverseV2(next1, node);
	    		
	    	} else {
	    		
	    		node.next = previous;
	    		return node;
	    		
	    	}
			
	    	
	    }
		
	}
	
	
	private static class Node {
		
		int data;
		
		Node next;
		
		Node(int d) {
			data = d;
		}
		
	}
	
	
	public static void main(String[] args) {
		
		
		SinglyLinkedList list = new SinglyLinkedList();
        list.head = new Node(1);
        list.head.next = new Node(2);
        list.head.next.next = new Node(3);
        list.head.next.next.next = new Node(4);
         
        System.out.println("Original Linked list is :");
        list.printList(list.head);
        System.out.println("");
        list.head = list.reverseV2(list.head, null);
        System.out.println("");
        System.out.println("Reversed linked list : ");
        list.printList(list.head);
    }
	
}
