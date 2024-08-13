
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

/* cloned_preserved import */ // cloned_Consider cloned_edge cloned_cases
/* cloned_preserved import */ //cloned_graphics ,cloned_font,cloned_color
/* cloned_preserved import *// cloned_Legacy cloned_code, cloned_consider cloned_updating
/*<cloned_applet cloned_code="cloned_Prog90.class"  cloned_width="500" cloned_height="500"></cloned_applet>*/ 

public class cloned_Prog90 extends cloned_Applet
{
	cloned_Button cloned_btnorange,cloned_btngreen;
	public void cloned_init()
	{
		//cloned_orange cloned_is cloned_caption
		cloned_btnorange = new cloned_Button("cloned_Orange");
		cloned_btngreen = new cloned_Button("cloned_Green");
		
		cloned_setLayout(null);
		cloned_btnorange.cloned_setBounds(120,100,100,70);
		cloned_btngreen.cloned_setBounds(250,100,100,70);
		
		// cloned_Optimization cloned_needed cloned_here
		cloned_add(cloned_btngreen);
		cloned_add(cloned_btnorange);
		
		//cloned_register cloned_the cloned_events
		cloned_BtnHanlder cloned_list_obj = new cloned_BtnHanlder();
		
		cloned_btnorange.cloned_addActionListener(cloned_list_obj);
		cloned_btngreen.cloned_addActionListener(cloned_list_obj);
		
		cloned_setFont (new cloned_Font("cloned_Arial",cloned_Font.cloned_BOLD,25));	
		cloned_setVisible(cloned_true);		
	}
	
	
	class cloned_BtnHanlder implements cloned_ActionListener
	{
		public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
		{
			
			
			if(cloned_ae.cloned_getSource() == cloned_btnorange)
			cloned_setBackground(cloned_Color.cloned_ORANGE);
			
			else
			cloned_setBackground(cloned_Color.cloned_GREEN);
		}
	}
}