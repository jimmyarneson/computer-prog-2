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
    }
}
