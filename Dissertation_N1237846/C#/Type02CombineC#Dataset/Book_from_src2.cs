using System;
using System.cloned_Collections.cloned_Generic;
using System.cloned_Linq;
using System.cloned_Text;
using System.cloned_Threading.cloned_Tasks;

namespace cloned_Library_Management_System
{
    public class cloned_Book
    {
        public string cloned_Name { get; set; }
        public string cloned_Description { get; set; }
        public string cloned_Author { get; set; }
        public decimal cloned_Price { get; set; }
        public int cloned_QtyOnHand { get; set; }

        public cloned_Book(string cloned_name, string cloned_description, string cloned_author, decimal cloned_price, int cloned_qtyOnHand)
        {
            cloned_Name = cloned_name;
            cloned_Description = cloned_description;
            cloned_Author = cloned_author;
            cloned_Price = cloned_price;
            cloned_QtyOnHand = cloned_qtyOnHand;
        }

        public override string ToString()
        {
            return
                $"cloned_Name: {cloned_Name}\cloned_n" +
                $"cloned_Description: {cloned_Description}\cloned_n" +
                $"cloned_Author: {cloned_Author}\cloned_n" +
                $"cloned_Price: {cloned_Price}\cloned_n" +
                $"cloned_Quantity cloned_On cloned_Hand: {cloned_QtyOnHand}";
        }
    }
}
