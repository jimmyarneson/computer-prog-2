/*
 * Created by SharpDevelop.
 * User: arneson.j1
 * Date: 4/16/2024
 * Time: 1:55 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
namespace prog88aW
{
	partial class MainForm
	{
		/// <summary>
		/// Designer variable used to keep track of non-visual components.
		/// </summary>
		private System.ComponentModel.IContainer components = null;
		
		/// <summary>
		/// Disposes resources used by the form.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing) {
				if (components != null) {
					components.Dispose();
				}
			}
			base.Dispose(disposing);
		}
		
		/// <summary>
		/// This method is required for Windows Forms designer support.
		/// Do not change the method contents inside the source code editor. The Forms designer might
		/// not be able to load this method if it was changed manually.
		/// </summary>
		private void InitializeComponent()
		{
			this.textBox1 = new System.Windows.Forms.TextBox();
			this.textBox2 = new System.Windows.Forms.TextBox();
			this.label1 = new System.Windows.Forms.Label();
			this.button1 = new System.Windows.Forms.Button();
			this.button2 = new System.Windows.Forms.Button();
			this.button3 = new System.Windows.Forms.Button();
			this.lblSum = new System.Windows.Forms.Label();
			this.lblDiff = new System.Windows.Forms.Label();
			this.lblProd = new System.Windows.Forms.Label();
			this.lblAvg = new System.Windows.Forms.Label();
			this.lblAbsD = new System.Windows.Forms.Label();
			this.lblMin = new System.Windows.Forms.Label();
			this.label8 = new System.Windows.Forms.Label();
			this.label9 = new System.Windows.Forms.Label();
			this.label10 = new System.Windows.Forms.Label();
			this.label11 = new System.Windows.Forms.Label();
			this.label12 = new System.Windows.Forms.Label();
			this.label13 = new System.Windows.Forms.Label();
			this.lblMax = new System.Windows.Forms.Label();
			this.label2 = new System.Windows.Forms.Label();
			this.SuspendLayout();
			// 
			// textBox1
			// 
			this.textBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.textBox1.Location = new System.Drawing.Point(12, 45);
			this.textBox1.Name = "textBox1";
			this.textBox1.Size = new System.Drawing.Size(198, 29);
			this.textBox1.TabIndex = 0;
			// 
			// textBox2
			// 
			this.textBox2.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.textBox2.Location = new System.Drawing.Point(12, 85);
			this.textBox2.Name = "textBox2";
			this.textBox2.Size = new System.Drawing.Size(198, 29);
			this.textBox2.TabIndex = 1;
			// 
			// label1
			// 
			this.label1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label1.Location = new System.Drawing.Point(12, 5);
			this.label1.Name = "label1";
			this.label1.Size = new System.Drawing.Size(198, 38);
			this.label1.TabIndex = 2;
			this.label1.Text = "Enter 2 Nums:";
			this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// button1
			// 
			this.button1.BackColor = System.Drawing.Color.Purple;
			this.button1.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button1.Location = new System.Drawing.Point(216, 5);
			this.button1.Name = "button1";
			this.button1.Size = new System.Drawing.Size(213, 34);
			this.button1.TabIndex = 3;
			this.button1.Text = "Calculate";
			this.button1.UseVisualStyleBackColor = false;
			this.button1.Click += new System.EventHandler(this.Button1Click);
			// 
			// button2
			// 
			this.button2.BackColor = System.Drawing.Color.Purple;
			this.button2.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button2.Location = new System.Drawing.Point(216, 45);
			this.button2.Name = "button2";
			this.button2.Size = new System.Drawing.Size(213, 34);
			this.button2.TabIndex = 4;
			this.button2.Text = "Clear";
			this.button2.UseVisualStyleBackColor = false;
			// 
			// button3
			// 
			this.button3.BackColor = System.Drawing.Color.Purple;
			this.button3.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.button3.Location = new System.Drawing.Point(216, 85);
			this.button3.Name = "button3";
			this.button3.Size = new System.Drawing.Size(213, 34);
			this.button3.TabIndex = 5;
			this.button3.Text = "Exit";
			this.button3.UseVisualStyleBackColor = false;
			this.button3.Click += new System.EventHandler(this.Button3Click);
			// 
			// lblSum
			// 
			this.lblSum.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblSum.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblSum.Location = new System.Drawing.Point(216, 129);
			this.lblSum.Name = "lblSum";
			this.lblSum.Size = new System.Drawing.Size(198, 38);
			this.lblSum.TabIndex = 6;
			this.lblSum.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// lblDiff
			// 
			this.lblDiff.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblDiff.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblDiff.Location = new System.Drawing.Point(216, 167);
			this.lblDiff.Name = "lblDiff";
			this.lblDiff.Size = new System.Drawing.Size(198, 38);
			this.lblDiff.TabIndex = 7;
			this.lblDiff.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			this.lblDiff.Click += new System.EventHandler(this.LblDiffClick);
			// 
			// lblProd
			// 
			this.lblProd.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblProd.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblProd.Location = new System.Drawing.Point(216, 205);
			this.lblProd.Name = "lblProd";
			this.lblProd.Size = new System.Drawing.Size(198, 38);
			this.lblProd.TabIndex = 8;
			this.lblProd.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// lblAvg
			// 
			this.lblAvg.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblAvg.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblAvg.Location = new System.Drawing.Point(216, 243);
			this.lblAvg.Name = "lblAvg";
			this.lblAvg.Size = new System.Drawing.Size(198, 38);
			this.lblAvg.TabIndex = 9;
			this.lblAvg.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// lblAbsD
			// 
			this.lblAbsD.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblAbsD.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblAbsD.Location = new System.Drawing.Point(216, 281);
			this.lblAbsD.Name = "lblAbsD";
			this.lblAbsD.Size = new System.Drawing.Size(198, 38);
			this.lblAbsD.TabIndex = 10;
			this.lblAbsD.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// lblMin
			// 
			this.lblMin.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblMin.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblMin.Location = new System.Drawing.Point(216, 357);
			this.lblMin.Name = "lblMin";
			this.lblMin.Size = new System.Drawing.Size(198, 38);
			this.lblMin.TabIndex = 11;
			this.lblMin.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			this.lblMin.Click += new System.EventHandler(this.Label7Click);
			// 
			// label8
			// 
			this.label8.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label8.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label8.Location = new System.Drawing.Point(12, 319);
			this.label8.Name = "label8";
			this.label8.Size = new System.Drawing.Size(198, 38);
			this.label8.TabIndex = 17;
			this.label8.Text = "Max:";
			this.label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label9
			// 
			this.label9.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label9.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label9.Location = new System.Drawing.Point(12, 281);
			this.label9.Name = "label9";
			this.label9.Size = new System.Drawing.Size(198, 38);
			this.label9.TabIndex = 16;
			this.label9.Text = "Abs. Distance:";
			this.label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label10
			// 
			this.label10.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label10.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label10.Location = new System.Drawing.Point(12, 243);
			this.label10.Name = "label10";
			this.label10.Size = new System.Drawing.Size(198, 38);
			this.label10.TabIndex = 15;
			this.label10.Text = "Average:";
			this.label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label11
			// 
			this.label11.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label11.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label11.Location = new System.Drawing.Point(12, 205);
			this.label11.Name = "label11";
			this.label11.Size = new System.Drawing.Size(198, 38);
			this.label11.TabIndex = 14;
			this.label11.Text = "Product:";
			this.label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label12
			// 
			this.label12.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label12.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label12.Location = new System.Drawing.Point(12, 167);
			this.label12.Name = "label12";
			this.label12.Size = new System.Drawing.Size(198, 38);
			this.label12.TabIndex = 13;
			this.label12.Text = "Difference:";
			this.label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label13
			// 
			this.label13.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label13.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label13.Location = new System.Drawing.Point(12, 129);
			this.label13.Name = "label13";
			this.label13.Size = new System.Drawing.Size(198, 38);
			this.label13.TabIndex = 12;
			this.label13.Text = "Sum:";
			this.label13.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// lblMax
			// 
			this.lblMax.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.lblMax.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.lblMax.Location = new System.Drawing.Point(216, 319);
			this.lblMax.Name = "lblMax";
			this.lblMax.Size = new System.Drawing.Size(198, 38);
			this.lblMax.TabIndex = 18;
			this.lblMax.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// label2
			// 
			this.label2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(255)))), ((int)(((byte)(128)))));
			this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.label2.Location = new System.Drawing.Point(12, 357);
			this.label2.Name = "label2";
			this.label2.Size = new System.Drawing.Size(198, 38);
			this.label2.TabIndex = 19;
			this.label2.Text = "Min:";
			this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
			// 
			// MainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.Color.Yellow;
			this.ClientSize = new System.Drawing.Size(441, 414);
			this.Controls.Add(this.label2);
			this.Controls.Add(this.lblMax);
			this.Controls.Add(this.label8);
			this.Controls.Add(this.label9);
			this.Controls.Add(this.label10);
			this.Controls.Add(this.label11);
			this.Controls.Add(this.label12);
			this.Controls.Add(this.label13);
			this.Controls.Add(this.lblMin);
			this.Controls.Add(this.lblAbsD);
			this.Controls.Add(this.lblAvg);
			this.Controls.Add(this.lblProd);
			this.Controls.Add(this.lblDiff);
			this.Controls.Add(this.lblSum);
			this.Controls.Add(this.button3);
			this.Controls.Add(this.button2);
			this.Controls.Add(this.button1);
			this.Controls.Add(this.label1);
			this.Controls.Add(this.textBox2);
			this.Controls.Add(this.textBox1);
			this.Name = "MainForm";
			this.Text = "prog88aW";
			this.Load += new System.EventHandler(this.MainFormLoad);
			this.ResumeLayout(false);
			this.PerformLayout();
		}
		private System.Windows.Forms.Label label2;
		private System.Windows.Forms.Label lblMax;
		private System.Windows.Forms.Label label13;
		private System.Windows.Forms.Label label12;
		private System.Windows.Forms.Label label11;
		private System.Windows.Forms.Label label10;
		private System.Windows.Forms.Label label9;
		private System.Windows.Forms.Label label8;
		private System.Windows.Forms.Label lblMin;
		private System.Windows.Forms.Label lblAbsD;
		private System.Windows.Forms.Label lblAvg;
		private System.Windows.Forms.Label lblProd;
		private System.Windows.Forms.Label lblDiff;
		private System.Windows.Forms.Label lblSum;
		private System.Windows.Forms.Button button3;
		private System.Windows.Forms.Button button2;
		private System.Windows.Forms.Button button1;
		private System.Windows.Forms.Label label1;
		private System.Windows.Forms.TextBox textBox2;
		private System.Windows.Forms.TextBox textBox1;
	}
}
