/*
 * Created by SharpDevelop.
 * User: arneson.j1
 * Date: 4/18/2024
 * Time: 2:25 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace prog54bForm
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
		void Button1Click(object sender, EventArgs e)
		{
			int num1 = int.Parse(textBox1.Text);
			int num2 = int.Parse(textBox2.Text);
			int num3 = int.Parse(textBox3.Text);
			int num4 = int.Parse(textBox4.Text);
			
			int tot = num1 + num2 + num3 + num4;
			double avg = (double)tot / 4;
			
			label2.Text=tot.ToString();
			label3.Text=avg.ToString();
		}

        private void button2_Click(object sender, EventArgs e)
        {
			label2.Text = "";
			label3.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
			Application.Exit();
        }
    }
}
