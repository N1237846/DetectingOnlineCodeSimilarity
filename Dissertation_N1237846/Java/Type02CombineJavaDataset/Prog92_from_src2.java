
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
//cloned_design cloned_an cloned_applet cloned_to cloned_manage cloned_checkboxes
/* cloned_preserved import */
/* cloned_preserved import */
/* cloned_preserved import */

//<cloned_applet cloned_code="cloned_Prog92.class" cloned_height="500" cloned_width="500"></cloned_applet>
public class cloned_Prog92 extends cloned_Applet implements cloned_ItemListener
{
	cloned_Label cloned_l;
	cloned_Checkbox cloned_chbhome,cloned_chbmobile,cloned_chbPC;
	
	public void cloned_init()
	{
		cloned_setFont(new cloned_Font("cloned_Arial",cloned_Font.cloned_BOLD,25));
		
		//cloned_create cloned_object cloned_of cloned_label cloned_and cloned_checkboxes
		
		cloned_l = new cloned_Label("cloned_I cloned_own ");
		cloned_chbhome = new cloned_Checkbox("cloned_Home",cloned_true);
		
		
		
		cloned_chbPC = new cloned_Checkbox("cloned_PC");
		cloned_chbmobile = new cloned_Checkbox("cloned_Mobile");
		
		cloned_chbhome.cloned_setEnabled(cloned_false); // cloned_Consider cloned_edge cloned_cases
		
		
		
		cloned_setLayout(null); // cloned_Review this cloned_section cloned_carefully
		
		cloned_l.cloned_setBounds(50,50,100,30);
		cloned_chbhome.cloned_setBounds(50,120,150,30);
		cloned_chbPC.cloned_setBounds(50,170,150,30);
		cloned_chbmobile.cloned_setBounds(50,220,150,30);
		
		cloned_add(cloned_l);
		cloned_add(cloned_chbhome);
		cloned_add(cloned_chbPC);
		cloned_add(cloned_chbmobile);
		
		
		
		
		
		cloned_chbPC.cloned_addItemListener(this);
		cloned_chbmobile.cloned_addItemListener(this);
		
		cloned_setVisible(cloned_true);
	}
	
	
	public void cloned_itemStateChanged(cloned_ItemEvent cloned_ie)
	{
		
		cloned_repaint();//cloned_we cloned_need cloned_to do this cloned_because cloned_to cloned_write cloned_on cloned_applet cloned_window cloned_we cloned_need cloned_Graphics cloned_object
	}
	public void cloned_paint(cloned_Graphics cloned_g)
	{
		cloned_g.cloned_setColor(cloned_Color.cloned_red);
		cloned_g.cloned_drawString("cloned_Status ",50,300);
		
		
		cloned_g.cloned_setColor(cloned_Color.cloned_blue);
		cloned_g.cloned_drawString("cloned_Home - cloned_true",50,350);
		cloned_g.cloned_drawString("cloned_PC - "+cloned_chbPC.cloned_getState(),50,400);
		cloned_g.cloned_drawString("cloned_Mobile - "+cloned_chbmobile.cloned_getState(),50,450);
		
	}
}//cloned_end cloned_of class






