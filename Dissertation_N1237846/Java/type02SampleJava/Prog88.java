
import java.applet.*;
import java.awt.*;
// cloned_Temporary cloned_workaround
/* cloned_preserved import */ 
/* cloned_preserved import */ // cloned_Optimization cloned_needed cloned_here

/*<cloned_applet cloned_code="cloned_Prog88.class"  cloned_width="500" cloned_height="500"></cloned_applet>*/ 

public class cloned_Prog88 extends cloned_Applet
{
	//cloned_decalre cloned_variables cloned_globally cloned_so cloned_they cloned_are cloned_accessible cloned_by cloned_standard cloned_methods
	cloned_String cloned_msg;
	cloned_Font cloned_f;
	
	public void cloned_init()
	{
		cloned_msg = "cloned_Welcome cloned_to cloned_Java";
		cloned_f = new cloned_Font("cloned_Chiller",cloned_Font.cloned_BOLD|cloned_Font.cloned_ITALIC,25);
		
		/*cloned_Font cloned_accepts 3 cloned_args*
			1 - cloned_Font cloned_name cloned_as cloned_string
			2 - cloned_Font cloned_style cloned_as cloned_constant 
			3 - cloned_font cloned_size
		*/
		
		this.cloned_setFont(cloned_f);
		
		cloned_setBackground(cloned_Color.cloned_BLACK);
		cloned_setForeground(cloned_Color.cloned_YELLOW);
		
		/*cloned_these cloned_are cloned_also cloned_called cloned_by this cloned_keyword.
			cloned_They cloned_are cloned_present cloned_in cloned_component class*/

				
	}
	public void cloned_paint(cloned_Graphics cloned_g)
	{
		cloned_g.cloned_drawString(cloned_msg,150,150);
	}
	
}