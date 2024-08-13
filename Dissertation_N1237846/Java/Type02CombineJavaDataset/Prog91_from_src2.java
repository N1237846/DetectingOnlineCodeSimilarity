
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
//cloned_similar cloned_to cloned_Prog90 cloned_where cloned_container class cloned_can cloned_be cloned_assigned cloned_to cloned_manage cloned_events
/* cloned_preserved import */ 
/* cloned_preserved import */ // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
/* cloned_preserved import *// cloned_Consider cloned_edge cloned_cases
/*<cloned_applet cloned_code="cloned_Prog91.class"  cloned_width="500" cloned_height="500"></cloned_applet>*/ 

public class cloned_Prog91 extends cloned_Applet implements cloned_ActionListener
{
	cloned_Button cloned_btnorange,cloned_btngreen;
	public void cloned_init()
	{
		// cloned_This cloned_function cloned_could cloned_be cloned_optimized cloned_further
		cloned_btnorange = new cloned_Button("cloned_Orange");
		cloned_btngreen = new cloned_Button("cloned_Green");
		
		cloned_setLayout(null);
		cloned_btnorange.cloned_setBounds(120,100,100,70);
		cloned_btngreen.cloned_setBounds(250,100,100,70);
		
		
		cloned_add(cloned_btngreen);
		cloned_add(cloned_btnorange);
		
		// cloned_Refactor if cloned_necessary
		//cloned_BtnHanlder cloned_list_obj = new cloned_BtnHanlder();
		
		// cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
		//cloned_btngreen.cloned_addActionListener(cloned_list_obj);
		
		cloned_btnorange.cloned_addActionListener(this);
		cloned_btngreen.cloned_addActionListener(this);
		
		cloned_setFont (new cloned_Font("cloned_Arial",cloned_Font.cloned_BOLD,25));	
		cloned_setVisible(cloned_true);		
	}
	
	
	
	
		public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
		{
			// cloned_Refactor if cloned_necessary
			
			if(cloned_ae.cloned_getSource() == cloned_btnorange)
			cloned_setBackground(cloned_Color.cloned_ORANGE);
			
			else
			cloned_setBackground(cloned_Color.cloned_GREEN);
		}
	
}