

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ShortestPathMatrix {

	Set<MatrixElement> elements = new HashSet<>();
	
	Map<String, MatrixElement> locationMap = new HashMap<>();
	
	public void createMatrix () {
		
	  /*	1	2	3
		4	5	6	
		7	8	9
		10	11	13	*/


		String matrix = "(0,0)1 \n " +
				"(0,1)2 \n " +
				"(0,2)3 \n " +
				"(1,0)4 \n " +
				"(1,1)5 \n " +
				"(1,2)6 \n " +
				"(2,0)7 \n " +
				"(2,1)8 \n " +
				"(2,2)9 \n " +
				"(3,0)10 \n " +
				"(3,1)11 \n " +
				"(3,2)12 \n " +
				"(4,0)13 \n " +
				"(4,1)14 \n " +
				"(4,2)15 \n " ;
				
		int id = 0;
		for (String element : matrix.split("\\n")) {
			
			if(element.trim().length() > 0) {
			
				MatrixElement matrixElement = new MatrixElement();
				matrixElement.setId(id);
				matrixElement.setValue(element.split("\\)")[1]);
				matrixElement.setCordX(Integer.parseInt(element.split(",")[0].replace("(", "").trim()));
				matrixElement.setCordY(Integer.parseInt(element.split(",")[1].split("\\)")[0]));
				elements.add(matrixElement);
				locationMap.put(matrixElement.getCordX()+","+matrixElement.getCordY(), matrixElement);
				id++;
				
			}
			
			
			
		}
		
	}
	
	
	public static void main(String[] args) {
		
		ShortestPathMatrix matrix = new ShortestPathMatrix();
		
		matrix.createMatrix();
		
		matrix.findDistanceBetweenPoint("4,1", "0,0");
		
		
		
	}


	private void findDistanceBetweenPoint(String string, String string2) {
		
		MatrixElement a = locationMap.get(string);
		MatrixElement b = locationMap.get(string2);
		
		int x, y;
		
		x = a.getCordX();
		y = a.getCordY();
		
		
		locateTheItem(x, y, b);
		
	}
	
	private void locateTheItem(int x, int y, MatrixElement b) {
		
		System.out.println(x + " , " + y);
		
		int nextX = x;
		int nextY = y; 
		
		boolean locateAgain = false;
		
		if(b.getCordX() > x) {
			nextX = x + 1;	
			locateAgain = true;
		} 
		
		if (b.getCordY() > y ) {
			nextY = y + 1;	
			locateAgain = true;
		}
		
		if(b.getCordX() < x) {
			nextX = x - 1;	
			locateAgain = true;
		} 
		
		if (b.getCordY() < y ) {
			nextY = y - 1;	
			locateAgain = true;
		}
		
		
		if(locateAgain) {
			locateTheItem(nextX, nextY, b);
		} else {
			
			System.out.println("traced !");
			
		}
		
		
	}

	public class MatrixElement {

		private int id;
		private String value;
		
		private MatrixElement left;
		private MatrixElement right;
		private MatrixElement top;
		private MatrixElement bottom;
		
		private int cordX;
		private int cordY;
		
		
		public MatrixElement getLeft() {
			return left;
		}
		public void setLeft(MatrixElement left) {
			this.left = left;
		}
		public MatrixElement getRight() {
			return right;
		}
		public void setRight(MatrixElement right) {
			this.right = right;
		}
		public MatrixElement getTop() {
			return top;
		}
		public void setTop(MatrixElement top) {
			this.top = top;
		}
		public MatrixElement getBottom() {
			return bottom;
		}
		public void setBottom(MatrixElement bottom) {
			this.bottom = bottom;
		}
		public int getId() {
			return id;
		}
		public void setId(int id) {
			this.id = id;
		}
		public String getValue() {
			return value;
		}
		public void setValue(String value) {
			this.value = value;
		}
		public int getCordX() {
			return cordX;
		}
		public void setCordX(int cordX) {
			this.cordX = cordX;
		}
		public int getCordY() {
			return cordY;
		}
		public void setCordY(int cordY) {
			this.cordY = cordY;
		}
		
		
		
	}
	
	
}
