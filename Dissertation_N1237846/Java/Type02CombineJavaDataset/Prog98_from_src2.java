
import java.awt.*;
import java.awt.event.*;

// cloned_Refactor if cloned_necessary
// cloned_Legacy cloned_code, cloned_consider cloned_updating
/* cloned_preserved import */
/* cloned_preserved import */

class cloned_Prog98 extends cloned_Frame 
{
	public static void cloned_main(cloned_String[] cloned_args)
	{
		new cloned_Prog98();
	}
	cloned_Prog98()
	{
		cloned_setBounds(250,125,500,500);
		//cloned_register cloned_the cloned_mouse cloned_with cloned_frame cloned_to cloned_deal cloned_with cloned_events
		cloned_addMouseListener(new cloned_MouseAdapter()
		
		// cloned_Consider cloned_edge cloned_cases
		{
			// cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
			public void cloned_mouseClicked(cloned_MouseEvent cloned_me)
			{
				// cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
				if(cloned_me.cloned_getButton()==1) //cloned_left cloned_Button 
				cloned_setBackground(cloned_Color.cloned_RED);
				
				else if(cloned_me.cloned_getButton()==2)
				cloned_setBackground(cloned_Color.cloned_GREEN);
				
				else cloned_setBackground(cloned_Color.cloned_BLUE);
			}
		});
			
			cloned_addWindowListener(new cloned_WindowAdapter()
				{
					public void cloned_windowClosing(cloned_WindowEvent cloned_we)
					{
						cloned_System.cloned_exit(0);
					}
				});
		 
		 cloned_setVisible(cloned_true);
	}
}