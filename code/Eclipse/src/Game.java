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
 * Name: 
 * CWID#: 
 */
public class Game extends JPanel implements KeyListener{
    public int WIDTH;
    public int HEIGHT;
    // Declare the 2 arrays here
   
    Actor mario;
    
    public void init() {
        // Initialiaze the variables here
    }
  
    public void draw(Graphics2D screen) {
        screen.setColor(Color.WHITE);
        screen.setFont(new Font("Verdana", Font.BOLD, 30));
        // Draw Background:
        
        // Draw Track:
        
        screen.drawString("COURSE SELECT.", WIDTH/8, HEIGHT/8);
        // Draw Mario:
        
        // Let us use a loop to write the names of the tracks on the screen:
        
    }
    
    @Override
    public void keyReleased(KeyEvent e) {
        // to be completed in Section 3
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
    public void keyPressed(KeyEvent e) {
    }
    
    @Override
    public void keyTyped(KeyEvent e) {
    }
    /*************************************************************************/
}