/*
 * Created by SharpDevelop.
 * User: arneson.j1
 * Date: 4/15/2024
 * Time: 1:55 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace program54WindApp
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			
		}
		
		void Button1Click(object sender, EventArgs e)
		{
			int miles = 0;
			int gallons = 0;
			double mpg = 0;
			
			
			if (comboBox1.Text == "1970 VW Bug") {
				miles = 286;
				gallons = 9;
			} else if (comboBox1.Text == "1979 Firebird") {
				miles = 412;
				gallons = 40;
			}
			else {
				MessageBox.Show("Invalid car selection!");
				return;
			}
			
			mpg = (double)miles / gallons;
			mpg = Math.Round(mpg, 1);
			lblMiles.Text = miles.ToString();
			lblGallons.Text = gallons.ToString();
			lblMpg.Text = mpg.ToString();
		}
		
		void Label6Click(object sender, EventArgs e)
		{
			
		}
	}
}
