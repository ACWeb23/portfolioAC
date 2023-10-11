package javaArray;



public class threeD {

	public static void main(String[] args) {
		float xPos = 0.0f;
		float yPos = 0.0f;
		// TODO Auto-generated method stub
		int[][][] array = {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}};
		System.out.println(array.length);
		System.out.println("Rows: " + array[0].length);
		
		void move(float dx,float dy)
		{
			xPos += dx;
			yPos += dy;
		}
		

	}

}
