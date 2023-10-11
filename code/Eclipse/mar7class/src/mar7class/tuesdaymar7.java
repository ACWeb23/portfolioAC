package mar7class;

import java.util.Scanner;

class Player1
{
	private String name;
	private int points;
	private float xPos;
	private float yPos;
	private String roal;
	private String element;
	private boolean bod;
	
	Player1(String nam, int xP, float pos1, float pos2, String job, String type, boolean gen)
	{
		name = nam;
		points = xP;
		xPos = pos1;
		yPos = pos2;
		roal = job;
		element = type;
		bod = gen;
		
	}
	public void creation(String name, String roal, String element, boolean bod )
	{
		// Name 
		boolean classChoice = false;
		{
			System.out.println("Please Enter Your Character's Name: ");
			Scanner myObj = new Scanner(System.in);
			String name1 = myObj.nextLine();
			System.out.println("Your Name Is: " + name1);
			name1 = name;
			
			// Class 
			while(classChoice == false)
			{
				System.out.println("Please Select your Starting Class");
				System.out.println("Press 1 for Soldier!");
				System.out.println("Press 2 for Mage!");
				System.out.println("Press 3 for Rogue!");
				String choice = myObj.nextLine();
				if(choice == "1")
				{
					System.out.println("The Soldier is a robust class built for defense on the front line");
					System.out.println("Would you like to continue with this class? press Y to contnue or N to choose again");
					String choose1 = myObj.nextLine();
					if(choose1 == "Y" || choose1 == "y")
					{
						classChoice = true;
						String choice2 = "Soldier";
						choice2 = job;
					}
					else 
					{
						// jmp line 45
					}
				}
				if(choice == "2")
				{
					System.out.println("The Mage is a magic user who's roal is dependent on element type");
					System.out.println("Would you like to continue with this class? press Y to contnue or N to choose again");
					String choose1 = myObj.nextLine();
					if(choose1 == "Y" || choose1 == "y")
					{
						classChoice = true;
						String choice2 = "Mage";
						choice2 = job;
					}
				}
				if(choice == "3")
				{
					System.out.println("The Rogue excells at 1 on 1 combat and fast attacks");
					System.out.println("Would you like to continue with this class? press Y to contnue or N to choose again");
					String choose1 = myObj.nextLine();
					if(choose1 == "Y" || choose1 == "y")
					{
						classChoice = true;
						String choice2 = "Rogue";
						choice2 = job;
					}
				}
				
			}
		}
		
	}
	
}
public class tuesdaymar7 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

}
