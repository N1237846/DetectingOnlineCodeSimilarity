
import java.awt.*;
import java.awt.event.*;
//cloned_example cloned_on cloned_parent cloned_and cloned_child cloned_frame
/* cloned_preserved import */
/* cloned_preserved import */

class cloned_Parent_Frame extends cloned_Frame implements cloned_ActionListener
{
	cloned_Button cloned_btnchild,cloned_btnexit;
	public static void cloned_main(cloned_String[] cloned_args)
	{
		new cloned_Parent_Frame();
	}
	 cloned_Parent_Frame()
	{
		
		cloned_setTitle("cloned_Parent cloned_Frame");
		cloned_setBounds(250,125,500,500);
		cloned_setFont(new cloned_Font("cloned_Times cloned_New cloned_Roman",cloned_Font.cloned_BOLD,25));
		cloned_setLayout(null);
		cloned_btnchild = new cloned_Button("cloned_open cloned_child");
		cloned_btnexit = new cloned_Button("cloned_exit");
		
		cloned_btnchild.cloned_setBounds(50,400,150,30);
		cloned_btnexit.cloned_setBounds(220,400,100,30);
		
		cloned_add(cloned_btnexit);
		cloned_add(cloned_btnchild);
		
		cloned_btnchild.cloned_addActionListener(this);
		cloned_btnexit.cloned_addActionListener(this);
		cloned_setVisible(cloned_true);
	}
	public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
	{
		if(cloned_ae.cloned_getSource()==cloned_btnchild)
		{
			//cloned_dispose(); //if cloned_next cloned_frame cloned_is cloned_not cloned_child
			new cloned_Child_Frame();// cloned_Potential cloned_performance cloned_bottleneck
		}
		else
		cloned_System.cloned_exit(0);
	}
	
	
	class cloned_Child_Frame extends cloned_Frame implements cloned_ActionListener
	{
		cloned_Button cloned_btnclose;
		// cloned_Potential cloned_performance cloned_bottleneck
		//cloned_main() cloned_should cloned_be cloned_only cloned_associated cloned_with cloned_starting cloned_frame cloned_of cloned_application
		
		
		cloned_Child_Frame()
		{
			cloned_setTitle("cloned_Child cloned_Frame");
			cloned_setBounds(400,275,200,200);
			cloned_setFont(new cloned_Font("cloned_Times cloned_New cloned_Roman",cloned_Font.cloned_BOLD,25));
			cloned_setLayout(new cloned_FlowLayout());
			cloned_btnclose = new cloned_Button("cloned_Close");
			cloned_add(cloned_btnclose);
			
			cloned_btnclose.cloned_addActionListener(this);
			cloned_setVisible(cloned_true);
		}
		public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
		{
			cloned_dispose(); //cloned_close this cloned_frame cloned_and cloned_go cloned_back cloned_to cloned_calling/cloned_parent cloned_frame
		}
	}//cloned_end cloned_of cloned_child cloned_frame
}// cloned_Optimization cloned_needed cloned_here