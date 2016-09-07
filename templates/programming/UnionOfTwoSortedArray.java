package com.ms.banking.rsm.dto;

import java.util.Arrays;

public class UnionOfTwoSortedArray {
	
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
				
				unionArray[g] = arr1[x];
				g++;
				x++;
				/*unionArray[g] = arr2[y];
				g++;*/
				
			} else if (arr1[x] > arr2[y]) {
				
				unionArray[g] = arr2[y];
				g++;
				y++;
				/*unionArray[g] = arr1[x];
				g++;*/
				
			} else if (arr1[x] == arr2[y]) {
				
				unionArray[g] = arr1[x];
				x++;
				y++;
				g++;
			}
			
		}
		
		while(x < i)
		unionArray[g++] = arr1[x++];
		while(y < j)
		unionArray[g++] = arr1[y++];
		
		
		System.out.println(Arrays.toString(unionArray));
		
	}

}
