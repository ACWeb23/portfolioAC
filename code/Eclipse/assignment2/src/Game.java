import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

/*
 * Please enter your information.
 * Name: Andrew Coleman
 * CWID#: 50298859
 */
public class Game extends JPanel implements KeyListener{
    public int WIDTH;
    public int HEIGHT;
    boolean startScreen;
    Actor kart;
    Actor track;
    
    
    
    public void init() {
        WIDTH = 640;
        HEIGHT = 640;
        // Q1: initialiaze the startScreen variable here:
        startScreen = true;
        // Q2: create the kart Actor, and initialiaze all its properties here:
        // kart properties
        kart = new Actor("mario", 0.4*WIDTH, 0.9*HEIGHT);
        kart.breakOn = true;
        kart.gasOn = false;
        kart.coins = 0;
        // Track Properties
        track = new Actor("track", -3.9*WIDTH, -2.05 * HEIGHT);
    }
  
    public void draw(Graphics2D screen) {
        screen.setColor(Color.BLACK);
        screen.setFont(new Font("Verdana", Font.BOLD, 30));
        if (startScreen)
        {
            blit(screen,"background1", 0,0);
            // Q3: draw the second background here:
            blit(screen,"background2", 64,177);

            screen.drawString("Press Enter", (int)(0.38*WIDTH), (int)(0.73*HEIGHT));  
        }
        else
        {
           track.draw(screen);
           // Q4: draw the kart here:
           // drawing the kart
           kart.draw(screen);
        }
        
    }
    
    @Override
    public void keyPressed(KeyEvent e) 
    {
        // Q5: complete the code to handel when a key is pressed:
	if (startScreen)
        {
            if(e.getKeyCode() == KeyEvent.VK_ENTER)
            {
            	startScreen = false;
            }
        }
	else
        {
		if(e.getKeyCode() == KeyEvent.VK_UP);
		{
			kart.breakOn = false;
			kart.gasOn = true;
		}
		
		if(e.getKeyCode() == KeyEvent.VK_RIGHT)
		{
			kart.changeImage("marior");
		}
		
		if(e.getKeyCode() == KeyEvent.VK_LEFT)
		{
			kart.changeImage("mariol");
		}
		
		if(e.getKeyCode() == KeyEvent.VK_DOWN)
		{
			kart.gasOn = false;
			kart.breakOn = true;
		}
        }
    }
    
    @Override
    public void keyReleased(KeyEvent e) 
    {
        // Q6: complete the code to handel when a key is released:
    	if(e.getKeyCode() == KeyEvent.VK_RIGHT)
    	{
    		kart.changeImage("mario");
    	}
    	
    	if(e.getKeyCode() == KeyEvent.VK_LEFT)
    	{
    		kart.changeImage("mario");
    	}
    }
        
 /*****************************************************************************
    // This part should not be modified
    * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
    
    public Game() 
    {
        setBackground(Color.black);
        setSize(WIDTH, HEIGHT);
        addKeyListener(this);
        setFocusable(true);
        init();
    }
    
    public void blit(Graphics g, String img, double x, double y) {
            String separator = System.getProperty("file.separator");
            Image i = new ImageIcon("images" + separator + img + ".png").getImage();
            g.drawImage(i, (int)x, (int)y, null);
    }
    @Override   
    public void paint(Graphics g) {
        super.paint(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        draw(g2d);
    }
    
    @Override
    public void keyTyped(KeyEvent e) {
    }
    /*************************************************************************/
}