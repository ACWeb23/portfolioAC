package aprl27Class;

public class Bubble {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int sequence[] = {9,7,10,4,1,8,5};
		for (int a = sequence.length-1; a>0; a--)
		{
			for (int x = 0; x < a; x++)
			{
				if(sequence[x] > sequence[x+1])
				{
					int tmp = sequence[x];
					sequence[x] = sequence[x+1];
					sequence[x+1] = tmp;
				}
			}
		}
		for(int b = 0; b < sequence.length; b++)
		{
				System.out.println(sequence[b]);
		}

	}

}
