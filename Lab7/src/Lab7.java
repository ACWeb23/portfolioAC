
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class Lab7 {
	// Global variables 
	
	static int GameStatus = 0;
	static int Money = 650;
	static int Lives = 100;
	static boolean GameOver = false;
	static int round = 0;
	static int reward =0;

	static int MonkeyType = 0;
	static final int DartMonkeyCost = 215; // 1
	static final int IceMonkeyCost = 360;  // 2
	static final int BoomerangMonkeyCost = 440; // 3
	static final int SuperMonkeyCost = 3400;  //  4
	
	static int MonkeyCost = 0;
	static int BalloonsMissed = 0;
	static int Round = 0;
	static String Difficulty = "";
	static Scanner console = new Scanner(System.in);
	
	static void userSettings()
	{
	    System.out.println("Choose the game difficulty");
	    System.out.println("Press 1 for Easy , 2 For Medum, 3 For Hard");
	    int choice;
	    choice = console.nextInt();
	    if (choice == 1)
	    {
	        Difficulty = "Easy";
	    }
	    else if (choice == 2)
	    {
	        Difficulty = "Medium";
	    }
	    else if (choice == 3)
	    {
	        Difficulty = "Hard";
	    }
	    System.out.println(Difficulty);
	}
	
	static void gameDifficulty() 
	{
        if (Difficulty == "Easy")
        {
            Lives = 100;
        }
        else if (Difficulty == "Medium")
        {
            Lives = 75;
        }
        else if (Difficulty == "Hard")
        {
            Lives = 50;
        }
        System.out.println(Difficulty+ "Selected!");

	}
	
	static void monkeyPurchace()
	{
	 
	    // MonkeyType = int(input("Press a number between 1 and 4 to purchace a Monkey "))
		System.out.println("Press a number between 1 and 4 to purchace a Monkey");
	    MonkeyType = console.nextInt();
	    console.close();
	    if (MonkeyType > 4 || MonkeyType < 1)
	    {
	    	System.out.println("Error Incorrect Input");
	    }
	    else if (MonkeyType == 1)
	    {
	        if (Money >= DartMonkeyCost)
	        {
	            MonkeyCost = DartMonkeyCost;
	            System.out.println("Dart Monkey Purchaced!!");
	        }
	            else if (Money < DartMonkeyCost)
	            {
	            System.out.println("Not Enough Money");
	            }
	    }
	    else if (MonkeyType == 2)
	    {
	        if (Money >= IceMonkeyCost)
	        {
	            MonkeyCost = IceMonkeyCost;
	            System.out.println("Ice Cold!!!");
	            System.out.println("Ice Monkey Purchaced");
	        }
	        else if (Money < IceMonkeyCost)
	        {
	            System.out.println("Not Enough Money");
	        }
	    }
	    else if (MonkeyType == 3)
	    {
	        if (Money >= BoomerangMonkeyCost)
	        {
	            MonkeyCost = BoomerangMonkeyCost;
	            System.out.println("Boomerang Monkey Purchaced!!!");
	        }
	        else if (Money < BoomerangMonkeyCost)
	        {
	            System.out.println("Not Enough Money");
	        }
	    }
	    else if (MonkeyType == 4)
	    {
	        if (Money >= SuperMonkeyCost)
	        {
	            MonkeyCost = SuperMonkeyCost;
	            System.out.println("Super Monkey In The House!!!!!!!!!!!");
	        }
	        else if (Money < SuperMonkeyCost)
	        {
	            System.out.println("Not Enough Money");
	            System.out.println("You Think your Rich??");
	        }
	    }
	    else if (MonkeyType > 4 || MonkeyType < 1) {
	        //MonkeyType = int(input("Press a number between 1 and 4 to purchace a Monkey"))
	    	System.out.println("Press a number between 1 and 4 to purchace a Monkey");
			Scanner console2 = new Scanner(System.in);
			MonkeyType = console2.nextInt();
			console2.close();
	    }
	    Money -= MonkeyCost;
	}
	
	static void displayPlayerInfo() 
	{
	    System.out.println("Money ="+ Money);
	    System.out.println("Lives ="+ Lives);
	    System.out.println("Balloons Missed "+ BalloonsMissed);
	    System.out.println("Round: "+ Round);
	    System.out.println("Game over is "+ GameOver);
	}
	
	static void balloonHit() 
	{
	    if (GameStatus == 0 && GameOver == false)
	    {
	        Lives -= 1;
	        BalloonsMissed += 1;
	        System.out.println("Balloon Hit!");
	    }
	}
	
	static void missedBalloons() 
	{
		 if (BalloonsMissed >= 100)
		    {
		        GameStatus = 1;
		        GameOver = true;
		        System.out.println("Game Over!");
		    }
	}
	   
	static void GameEnd()
	{
		if (Lives <= 0 && BalloonsMissed >= 100)
		{
	        GameOver = true;
	        System.out.println("Game Over");
		}

	}
	
	static void nextRound()
	{
		if (GameOver == false)
		{
	        reward = 100+round;
	        Money += reward;
	        round += 1;
		}
	}
	
	static void gameSettings()
	{
		userSettings();
	    gameDifficulty();
	}
	
	    



	/**
	 * @param args
	 * @throws FileNotFoundException 
	 */
	public static void main(String[] args)
	{
		gameSettings();
		monkeyPurchace();
		balloonHit();
		missedBalloons();
		GameEnd();
		nextRound();
		displayPlayerInfo();
		
		
	}

}