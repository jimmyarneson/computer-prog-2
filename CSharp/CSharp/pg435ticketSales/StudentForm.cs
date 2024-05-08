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
    public partial class StudentForm : Form
    {
        private Form myParent;
        public StudentForm(Form myParent)
        {
            InitializeComponent();
            this.myParent = myParent;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.myParent.Show();
            this.Close();
        }

        private void StudentForm_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.myParent.Show();
        }

        decimal decTAXRATE = 0.06m; //sales tax
        private decimal CalcTax(decimal cost)
        {
            return cost * decTAXRATE;
        }
    }
}
