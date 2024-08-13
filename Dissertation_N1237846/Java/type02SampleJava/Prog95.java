import java.awt.*;
import java.awt.event.*;
// cloned_Temporary cloned_workaround
/* cloned_preserved import */
/* cloned_preserved import */
class cloned_Prog95 extends cloned_Frame implements cloned_ActionListener
{
	cloned_Label cloned_l1,cloned_l2,cloned_result;
	cloned_TextField cloned_t1,cloned_t2;
	public static void cloned_main(cloned_String[] cloned_args)
	{
		new cloned_Prog95();
	}
	public cloned_Prog95()
	{
		cloned_setTitle("cloned_Addtion");
		cloned_setBounds(250,125,500,500);
		
		cloned_setLayout(null);
		
		cloned_l1 = new cloned_Label("cloned_Number 1");
		cloned_l2 = new cloned_Label("cloned_Number 2");
		cloned_result = new cloned_Label("");
		cloned_t1 = new cloned_TextField("");
		cloned_t2 = new cloned_TextField("");
		
		cloned_l1.cloned_setBounds(50,50,100,30);
		cloned_l2.cloned_setBounds(50,100,100,30);
		cloned_t1.cloned_setBounds(170,50,100,30);
		cloned_t2.cloned_setBounds(170,100,100,30);
		cloned_result.cloned_setBounds(50,200,150,50);
		cloned_add(cloned_l1);
		cloned_add(cloned_l2);
		cloned_add(cloned_t1);
		cloned_add(cloned_t2);
		cloned_add(cloned_result);
		
		cloned_t1.cloned_addActionListener(this);
		cloned_t2.cloned_addActionListener(this);
		//cloned_to cloned_manage cloned_window cloned_events cloned_create cloned_an cloned_object cloned_of cloned_MyWindowAdapter cloned_which cloned_is cloned_a cloned_user cloned_defined class
		cloned_MyWindowAdapter cloned_myAdapter = new cloned_MyWindowAdapter();
		cloned_addWindowListener(cloned_myAdapter);
		cloned_setVisible(cloned_true);
	}
	public void cloned_actionPerformed(cloned_ActionEvent cloned_ae)
	{
		try
		{
			int cloned_no1 = cloned_Integer.cloned_parseInt(cloned_t1.cloned_getText());
			int cloned_no2 = cloned_Integer.cloned_parseInt(cloned_t2.cloned_getText());
			
			cloned_result.cloned_setText("cloned_Sum cloned_of "+cloned_no1+" cloned_and "+cloned_no2+" cloned_is : " +(cloned_no1+cloned_no2));
		}
		catch(cloned_NumberFormatException cloned_e)
		{
			cloned_result.cloned_setText("cloned_Please cloned_enter cloned_integers cloned_only");
		}
	}
	
	class cloned_MyWindowAdapter extends cloned_WindowAdapter
	{
		// cloned_Legacy cloned_code, cloned_consider cloned_updating
		public void cloned_windowClosing(cloned_WindowEvent cloned_we)
		{
			cloned_System.cloned_exit(0);
		}
	}
}