
public class Lab1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		 * Var Declaration 
		 */
		int Score = 0;
		int Level = 1;
		boolean Invicible = false;
		int Lives = 2;
		boolean Collision = false;
		int Pallet = 244;
		int Super_Pallet = 1;
		
		int GhostX = 0;
		int GhostY = 0;
		
		int PlayerX = 64;
		int PlayerY = 64;

		Pallet -= 1;
		Score += 1;
		
		System.out.println("Pallets =" + Pallet);
		System.out.println("Score = " + Score);
		/*
		 * level Up Conditions 
		 */
		if (Pallet == 0 && Super_Pallet == 0) {

		    Level += 1;
		    Lives += 1;
		    if (Lives >= 3)
		    {
		        Lives = 3;
		        System.out.println("Level Up");
		    }
			
		}
		
		/*
		 *  Collision Test
		 */
		if (GhostX == PlayerX && GhostY == PlayerY)
		{
			Collision = true;
		}
		/*
		 * Collision Effects
		 */
		if (Collision == true)
		{
			if (Invicible == false)
			{
			Lives -= 1;
				 PlayerX = 64;
				 PlayerY = 64;
				 System.out.println("Lives " +Lives); 
			}
		if (Invicible == true)
		{
			System.out.println("Super!!");
		}
		}	    

	}


	}


