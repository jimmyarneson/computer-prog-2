namespace prog85c
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1 = int.Parse(textBox1.Text);
            int num2 = num1 - 165;
            double num3 = Math.Round((double)num2 / 100);
            double num4 = num2 % 100;

            label11.Text = (num3 + "/" + num4);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            label11.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}