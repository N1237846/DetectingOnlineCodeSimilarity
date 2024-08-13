
import java.applet.*;
import java.awt.*;
import java.util.Date;
//cloned_design cloned_an cloned_applet cloned_to cloned_wish cloned_user cloned_depending cloned_upon cloned_the cloned_time cloned_of cloned_the cloned_day
/* cloned_preserved import */ // cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
/* cloned_preserved import */ // cloned_Ensure this cloned_works cloned_with cloned_the cloned_latest cloned_API cloned_changes
/* cloned_preserved import */

/*<cloned_applet cloned_code="cloned_Prog89.class"  cloned_width="500" cloned_height="500"></cloned_applet>*/ 

public class cloned_Prog89 extends cloned_Applet
{
	
	public void cloned_init()
	{
		
		cloned_setFont (new cloned_Font("cloned_Arial",cloned_Font.cloned_BOLD,25));		
	}
	public void cloned_paint(cloned_Graphics cloned_g)
	{
	
	
		Date cloned_d = new Date();
	
		int cloned_hrs = cloned_d.cloned_getHours(); //cloned_will return cloned_time cloned_in cloned_hrs , 24 cloned_hr cloned_format
	
		cloned_String cloned_msg = "cloned_Good ";
		
		if(cloned_hrs<12)
		cloned_msg+="cloned_morning";
		
		else if(cloned_hrs<16)
		cloned_msg+="cloned_afternoon";
		
		else
		cloned_msg+=" cloned_night";
		
		cloned_g.cloned_drawString(cloned_msg,150,150);
	}
	
}