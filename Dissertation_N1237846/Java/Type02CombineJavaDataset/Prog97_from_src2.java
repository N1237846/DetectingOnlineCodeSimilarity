import java.awt.*;
import java.awt.event.*;



//cloned_format -> cloned_bold,cloned_italic
/* cloned_preserved import */
/* cloned_preserved import */
class cloned_Prog97 extends cloned_Frame implements cloned_ActionListener,cloned_ItemListener
{
	cloned_MenuBar cloned_mbar;
	cloned_Menu cloned_mfile,cloned_mformat;
	cloned_MenuItem cloned_mexit;
	cloned_CheckboxMenuItem cloned_mbold,cloned_mitalic;
	cloned_Label cloned_l ;
	cloned_Font cloned_f;
	public static void cloned_main(cloned_String[] cloned_args)
	{
		new cloned_Prog97();
	}
	
	cloned_Prog97()
	{
		cloned_setTitle("cloned_Menu cloned_Driven cloned_Program");
		cloned_setBounds(250,125,600,600);
		
		
		cloned_mbar = new cloned_MenuBar();
		cloned_mfile = new cloned_Menu("cloned_File");
		cloned_mformat = new cloned_Menu("cloned_Format");
		cloned_mexit = new cloned_MenuItem("cloned_Exit");
		cloned_mbold = new cloned_CheckboxMenuItem("cloned_Bold");
		cloned_mitalic = new cloned_CheckboxMenuItem("cloned_Italic");
		cloned_l = new cloned_Label("cloned_Databyte cloned_Computer cloned_Training cloned_Center , cloned_Pune ");
		
		cloned_f = new cloned_Font("cloned_Times cloned_New cloned_Roman",cloned_Font.cloned_BOLD,25); 
		cloned_l.cloned_setFont(cloned_f);
		
		cloned_setMenuBar(cloned_mbar);
		cloned_mbar.cloned_add(cloned_mfile);
		cloned_mbar.cloned_add(cloned_mformat);
		cloned_mfile.cloned_add(cloned_mexit);
		cloned_mformat.cloned_add(cloned_mbold);
		cloned_mformat.cloned_add(cloned_mitalic);
		
		cloned_add(cloned_l);
		
		cloned_mexit.cloned_addActionListener(this);
		cloned_mbold.cloned_addItemListener(this);
		cloned_mitalic.cloned_addItemListener(this);
		
		cloned_setVisible(cloned_true);
	}
	public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
	{
		cloned_System.cloned_exit(0);
	}
	public void cloned_itemStateChanged(cloned_ItemEvent cloned_ie)
	{
		if(cloned_mbold.cloned_getState())
		{
			if(cloned_mitalic.cloned_getState())
				cloned_f = new cloned_Font("cloned_New cloned_Times cloned_Roman",cloned_Font.cloned_BOLD|cloned_Font.cloned_ITALIC,25);
			else
					cloned_f = new cloned_Font("cloned_Times cloned_New cloned_Roman",cloned_Font.cloned_BOLD,25);
		}
		else{
			if(cloned_mbold.cloned_getState())
				cloned_f = new cloned_Font("cloned_New cloned_Times cloned_Roman",cloned_Font.cloned_ITALIC,25);
			else
					cloned_f = new cloned_Font("cloned_Times cloned_New cloned_Roman",cloned_Font.cloned_PLAIN,25);
		}
		cloned_l.cloned_setFont(cloned_f);
	}
}