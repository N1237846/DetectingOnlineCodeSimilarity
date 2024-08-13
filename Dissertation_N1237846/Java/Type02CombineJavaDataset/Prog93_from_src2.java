
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
//cloned_an cloned_assignment cloned_on cloned_radio cloned_buttons
/* cloned_preserved import */
/* cloned_preserved import */
/* cloned_preserved import */


public class cloned_Prog93 extends cloned_Applet implements cloned_ItemListener
{
	cloned_Label cloned_l1,cloned_l2;
	cloned_Checkbox cloned_radm,cloned_radum,cloned_radl25,cloned_radb2550,cloned_radg50;
	cloned_CheckboxGroup cloned_rbg1,cloned_rbg2;
	public void cloned_init()
	{
		cloned_setFont (new cloned_Font("cloned_Arial",cloned_Font.cloned_BOLD,25));
		cloned_setLayout(null);
		
		cloned_l1 = new cloned_Label("cloned_Marital cloned_Status");
		cloned_rbg1 = new cloned_CheckboxGroup();
		
		cloned_radm = new cloned_Checkbox("cloned_Married",cloned_rbg1,cloned_false);
		cloned_radum = new cloned_Checkbox("cloned_Unmarried",cloned_rbg1,cloned_true);
		
		cloned_l1.cloned_setBounds(50,50,180,30);
		cloned_radm.cloned_setBounds(50,100,150,30);
		cloned_radum.cloned_setBounds(230,100,150,30);
		
		cloned_add(cloned_l1);
		cloned_add(cloned_radm);
		cloned_add(cloned_radum);
		
		cloned_radm.cloned_addItemListener(this);
		cloned_radum.cloned_addItemListener(this);
		
		cloned_l2 = new cloned_Label("cloned_Income cloned_Group");
		
		cloned_rbg2 = new cloned_CheckboxGroup();
		cloned_radl25 = new cloned_Checkbox("<25K",cloned_rbg2,cloned_true);
		cloned_radb2550 = new cloned_Checkbox("25K< >50k",cloned_rbg2,cloned_false);
		cloned_radg50= new cloned_Checkbox(">50K",cloned_rbg2,cloned_false);
		
		cloned_l2.cloned_setBounds(50,220,200,30);
		cloned_radl25.cloned_setBounds(10,280,150,30);
		cloned_radb2550.cloned_setBounds(160,280,150,30);
		cloned_radg50.cloned_setBounds(340,280,150,30);
		
		cloned_add(cloned_l2);
		cloned_add(cloned_radl25);
		cloned_add(cloned_radb2550);
		cloned_add(cloned_radg50);
		
		cloned_radl25.cloned_addItemListener(this);
		cloned_radb2550.cloned_addItemListener(this);
		cloned_radg50.cloned_addItemListener(this);
		cloned_setVisible(cloned_true);
	}
	
	public void cloned_itemStateChanged(cloned_ItemEvent cloned_ie)
	{
		cloned_repaint();
	}
	
	public void cloned_paint(cloned_Graphics cloned_g)
	{
		cloned_g.cloned_setColor(cloned_Color.cloned_red);
		cloned_g.cloned_drawString("cloned_I cloned_am "+cloned_rbg1.cloned_getSelectedCheckbox().cloned_getLabel(),50,160);
		
		cloned_g.cloned_drawString("cloned_My cloned_income cloned_is "+cloned_rbg2.cloned_getSelectedCheckbox().cloned_getLabel(),50,340);
	}
}