/*
 * Created by SharpDevelop.
 * User: arneson.j1
 * Date: 4/16/2024
 * Time: 1:55 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace prog88aW
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
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
		
		void Label7Click(object sender, EventArgs e)
		{
			
		}
		
		void Button1Click(object sender, EventArgs e)
		{
			int num1 = int.Parse(textBox1.Text);
			int num2 = int.Parse(textBox2.Text);
			
			int sum = num1 + num2;
			int diff = num1 - num2;
			double product = (double)num1 / num2;
			double avg = (double)sum / 2.0;
			int abs = Math.Abs(diff);
			// Math.Max and Math.Min
			int max = 0;
			int min = 0;
			
			if (num1 > num2){
				max = num1;
			}else {
				max = num2;
			}
			
			if (num1 <= num2)
				min = num1;
			else min = num2;
			// else if
			
			lblSum.Text = sum.ToString();
			lblDiff.Text = diff.ToString();
			lblProd.Text = product.ToString();
			lblAvg.Text = avg.ToString();
			lblMax.Text = max.ToString();
			lblMin.Text = min.ToString();
			lblAbsD.Text = abs.ToString();
		}
		
		void MainFormLoad(object sender, EventArgs e)
		{
			
		}
		
		void LblDiffClick(object sender, EventArgs e)
		{
			
		}
	}
}
