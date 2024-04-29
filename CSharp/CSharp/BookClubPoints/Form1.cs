namespace BookClubPoints
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

            if (num1 == 0)
                label2.Text = "0 Points Earned";
            else if (num1 == 1)
                label2.Text = "5 Points Earned";
            else if (num1 == 2)
                label2.Text = "15 Points Earned";
            else if (num1 == 3)
                label2.Text = "30 Points Earned";
            else
                label2.Text = "60 Points Earned";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}