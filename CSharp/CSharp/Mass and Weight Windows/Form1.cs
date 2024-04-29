namespace Mass_and_Weight_Windows
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int mass = int.Parse(textBox1.Text);
            double weight = mass * 9.8;

            if (weight >= 10000)
                label3.Text = "Weight is too Much";
            else if (weight <= 100)
                label3.Text = "Weight is too Light";
            else
                label3.Text = weight.ToString();
        }
    }
}