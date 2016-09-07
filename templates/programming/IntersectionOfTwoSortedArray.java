package com.ms.banking.rsm.dto;

import java.util.Arrays;

public class IntersectionOfTwoSortedArray {
	
	public static void main(String[] args) {
		
		int [] arr1 = {1,3,4,5,7};
		int [] arr2 = {2,3,5,6};
		
		int i = arr1.length;
		int j = arr2.length;
		
		int [] unionArray = new int [i + j];
		
		int x = 0;
		int y = 0;
		
		int g = 0;
		
		while (x < i && y < j) {
			
			
			if (arr1[x] < arr2[y]) {
				
//				unionArray[g] = arr1[x];
				
				x++;
				
				
			} else if (arr1[x] > arr2[y]) {
				
//				unionArray[g] = arr2[y];
				
				y++;
				
				
			} else if (arr1[x] == arr2[y]) {
				
				unionArray[g] = arr1[x];
				x++;
				y++;
				g++;
			}
			
		}
		
		
		
		System.out.println(Arrays.toString(unionArray));
		
	}

}
