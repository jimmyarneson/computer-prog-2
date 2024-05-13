using Microsoft.VisualBasic;

namespace pg498Payroll
{
    public partial class Form1 : Form
    {
        const decimal decHOURLY_PAY_RATE = 7.25m;
        const int intMAX_EMPLOYEES = 5;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //calculate and display that gross pay earned by employees
            int[] intHours = new int[intMAX_EMPLOYEES];
            // Make a new int array of copacity inMAX_EMPLOYEES
            // Capacity can never change, unlike lists in python
            int intCount = 0;
            int intEmpHours = 0;
            decimal decEmpPay = 0.0m;

            for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++)
            {
                while (int.TryParse(
                    Interaction.InputBox("Enter the number of hours worked by employee #" +
                    (intCount+1).ToString(), "Need Hours Worked"),
                    out intEmpHours) == false) {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
                intHours[intCount] = intEmpHours;
            }
            // Calculate and display each employees gross pay
            listBox1.Items.Clear();
            for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++)
            {
                decEmpPay = intHours[intCount] * decHOURLY_PAY_RATE;
                listBox1.Items.Add("Employee " + (intCount + 1).ToString() +
                                   "Earned " + decEmpPay.ToString("$.00"));
            }

        }
    }
}