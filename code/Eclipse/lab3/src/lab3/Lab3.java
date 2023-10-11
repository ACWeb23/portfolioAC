package lab3;

public class Lab3 {

	public static void main(String[] args) 
	{
		
		// TODO Auto-generated method stub
		String standingNames[] = {"Bowser", "Mario", "Princess", "Luigi", "Yoshi", "Donkey kong", "Toad", "Koopa Troopa"};
		int standingNumber[] = {1, 2, 3, 4, 5, 6, 7, 8};
		int standingScore[] = {45, 30, 15, 5, 5, 0, 0, 0, 0};
		
		System.out.println("\tStandings");
		for (int i = 0; i < standingNumber.length; i++)
		{
			System.out.println(standingNumber[i] + "\t" + standingNames[i] + "\t"+ standingScore[i]);

		}

		// Multi dimm Array/List 2D & 3D
		// Using the previous example with 2D Arrays

		String scoreBoard[][] = {{"Bowser\t", "Mario\t", "Princess", "Luigi\t", "Yoshi\t", "Donkey kong", "Toad\t", "Koopa Troopa"},{"1", "2", "3", "4", "5", "6", "7", "8"},{"45", "30", "15", "5", "5", "0", "0", "0", "0"}};
		System.out.println("rows = "+ scoreBoard.length);
		System.out.println("columns = " + scoreBoard[0].length);
		System.out.println("\t🍄🍄🍄Standings🍄🍄🍄");
		for (int r = 0; r < scoreBoard[1].length; r++)
		{
		    System.out.println(scoreBoard[1][r] +"\t"+ scoreBoard[0][r] +"\t"+ scoreBoard[2][r]);
		  
		}


	}

}
