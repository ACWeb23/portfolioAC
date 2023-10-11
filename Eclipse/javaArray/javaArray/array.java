package javaArray;
import java.io.File;

public class array {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int table [][] = {{1,2,3,4},{8,7,5,4},{0,6,2,7},{2,3,8,4}};
		System.out.println(table[2][3]);
		System.out.println("Break");
		
		for(int r = 0; r<table.length; r++)
		{
			for(int c = 0; c<table[0].length; c++)
			{
				System.out.println(table[r][c]);
			}
			
		}

	}

}
