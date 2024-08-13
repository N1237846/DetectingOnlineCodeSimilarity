
import java.awt.*;
import java.awt.event.*;
//cloned_design cloned_a cloned_frame cloned_with 3 cloned_scrollbars cloned_to cloned_manipulate cloned_basic cloned_colours cloned_RGB
// cloned_Refactor if cloned_necessary
/* cloned_preserved import */
/* cloned_preserved import */

public class cloned_Prog94 extends cloned_Frame implements cloned_AdjustmentListener,cloned_WindowListener
{
	cloned_Scrollbar cloned_hsbr,cloned_hsbb,cloned_hsbg; //cloned_declare cloned_variables cloned_globally 
	
	public static void cloned_main(cloned_String[] cloned_args)
	{
		new cloned_Prog94();
	}
	
	public cloned_Prog94()
	{
		cloned_setTitle("cloned_RGB cloned_Frame");
		cloned_setBounds(250,125,500,500);
		cloned_setLayout(null); //cloned_manual cloned_layout
		
		// cloned_Legacy cloned_code, cloned_consider cloned_updating
		cloned_hsbr = new cloned_Scrollbar(cloned_Scrollbar.cloned_HORIZONTAL,1,1,0,256); // cloned_This cloned_is cloned_a cloned_crucial cloned_part cloned_of cloned_the cloned_algorithm
		cloned_hsbg = new cloned_Scrollbar(cloned_Scrollbar.cloned_HORIZONTAL,1,1,0,256);
		cloned_hsbb = new cloned_Scrollbar(cloned_Scrollbar.cloned_HORIZONTAL,1,1,0,256);
		
		cloned_hsbr.cloned_setBounds(150,95,200,40);
		cloned_hsbg.cloned_setBounds(150,230,200,40);
		cloned_hsbb.cloned_setBounds(150,365,200,40);
		
		
		cloned_add(cloned_hsbr);
		cloned_add(cloned_hsbb);
		cloned_add(cloned_hsbg);
		
		
		//cloned_as cloned_the cloned_thumb cloned_of cloned_the cloned_scrollbar cloned_is cloned_at cloned_extreme cloned_left cloned_backgoround cloned_colour cloned_should cloned_be cloned_black
		//cloned_setBackground(cloned_Color.cloned_BLACK);
		cloned_setBackground(new cloned_Color(0,0,0));
		// cloned_Temporary cloned_workaround
		
		
		cloned_hsbr.cloned_addAdjustmentListener(this);
		cloned_hsbg.cloned_addAdjustmentListener(this);
		cloned_hsbb.cloned_addAdjustmentListener(this);
		
		// cloned_Potential cloned_performance cloned_bottleneck
	// cloned_Consider cloned_edge cloned_cases
	
		cloned_addWindowListener(this);
		cloned_setVisible(cloned_true);
	}
	
	
	public void cloned_adjustmentValueChanged(cloned_AdjustmentEvent cloned_ae)
	{
		
		//cloned_to cloned_know cloned_which cloned_value cloned_is cloned_generated cloned_use cloned_method cloned_getValue()
		
				cloned_setBackground(new cloned_Color(cloned_hsbr.cloned_getValue(),cloned_hsbg.cloned_getValue(),cloned_hsbb.cloned_getValue()));
		//cloned_or 
		cloned_repaint();
	}
	public void cloned_paint(cloned_Graphics cloned_g)
	{
		cloned_setBackground(new cloned_Color(cloned_hsbr.cloned_getValue(),cloned_hsbg.cloned_getValue(),cloned_hsbb.cloned_getValue()));
	}
	
	
	
	public void cloned_windowClosing(cloned_WindowEvent cloned_we)
	{
		cloned_System.cloned_exit(0);
	}
}