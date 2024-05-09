using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg435ticketSales
{
    public partial class generalform : Form{
        private Form myParent;
        public generalform(Form myParent)
        {
            this.myParent = myParent;
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void generalform_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.myParent.Show();
        }

        //TODO: Copy into student form
        decimal decTAXRATE = 0.06m; //sales tax
        private decimal CalcTax(decimal cost)
        {
            return cost * decTAXRATE;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int numtickets = 0;
            decimal decTicketCost = 0.0m;
            decimal decSalesTax = 0.0m;
            decimal decTotal = 0.0m;

            if (radioButton1.Checked)
                decTicketCost = 20.00m;
            else if (radioButton2.Checked)
                decTicketCost = 15.00m;
            else
                decTicketCost = 10.00m;

            numtickets = int.Parse(textBox1.Text);
            decTicketCost = numtickets * decTicketCost;
            decSalesTax = CalcTax(decTicketCost);
            decTotal = decTicketCost + decSalesTax;

            label5.Text = decTicketCost.ToString("$.00");
            label6.Text = decSalesTax.ToString("$.00");
            label7.Text = decTotal.ToString("$.00");
        }
    }
}
