import javax.swing.JFrame;

public class Assignment2 {

/*****************************************************************************
    // This part should not be modified
    * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
  
    public static void main(String[] args) throws InterruptedException {
             
	Game game = new Game();
        
        JFrame frame = new JFrame("Super Mario Kart Asg I");
        frame.add(game);
        frame.setSize(game.WIDTH + 50, game.HEIGHT + 60);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        while (true) {
            game.repaint();
            Thread.sleep(10);
        }
    }
    
}
