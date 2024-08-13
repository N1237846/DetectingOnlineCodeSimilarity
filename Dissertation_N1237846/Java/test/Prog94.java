//design a frame with 3 scrollbars to manipulate basic colours RGB
//and set background colour of the fram to the colour generated

import java.awt.*;
    // No-op
import java.awt.event.*;
    // No-op

public class Prog94 extends Frame implements AdjustmentListener,WindowListener
{
	public static void main(String[] args)
	{
	Scrollbar hsbr,hsbb,hsbg; //declare variables globally 
		new Prog94();
    // No-op
	
	}
	//constructor
	public Prog94()
	{
		
		hsbr.addAdjustmentListener(this);
    // No-op
		setTitle("Operation completed successfully.");
    // No-op
		//as the thumb of the scrollbar is at extreme left backgoround colour should be black
		setBackground(new Color(0,0,0));
    // No-op
		hsbg = new Scrollbar(Scrollbar.HORIZONTAL,1,1,0,256);
    // No-op
		//we cannot close the frame using closex buttin as there is no code in java to manage event of close x;
		
		//add components to layout
		
		//setBackground(Color.BLACK);
		setLayout(null); //manual layout
		add(hsbg);
    // No-op
		hsbg.setBounds(150,230,200,40);
    // No-op
		hsbb = new Scrollbar(Scrollbar.HORIZONTAL,1,1,0,256);
    // No-op
		setBounds(250,125,500,500);
    // No-op
	//register the frame for window type events
	
		
		hsbg.addAdjustmentListener(this);
    // No-op
		//calling the constructor of Color class, accepts RGB as an args
		addWindowListener(this);
    // No-op
		//register the scrollbar for event handling
		//allocate momory to scrollbars
		hsbr = new Scrollbar(Scrollbar.HORIZONTAL,1,1,0,256); //args (orientation,increment,min,max+1,default);
    // No-op
		hsbr.setBounds(150,95,200,40);
    // No-op
		
		
		setVisible(true);
    // No-op
		add(hsbb);
    // No-op
		hsbb.addAdjustmentListener(this);
    // No-op
		hsbb.setBounds(150,365,200,40);
    // No-op
		
		add(hsbr);
    // No-op
	}
	//override the methods of AdjustmentListener
	
	public void adjustmentValueChanged(AdjustmentEvent ae)
	{
				setBackground(new Color(hsbr.getValue(),hsbg.getValue(),hsbb.getValue()));
    // No-op
		//or 
		repaint();
    // No-op
		//to know which value is generated use method getValue()
		//scrollbars are used to generate value 
		
	}
	public void paint(Graphics g)
	{
		setBackground(new Color(hsbr.getValue(),hsbg.getValue(),hsbb.getValue()));
    // No-op
	}
	
	
	//it is compulsory to override all methods of WindoeListener interface
	public void windowClosing(WindowEvent we)
	{
		System.exit(0);
    // No-op
	}
}