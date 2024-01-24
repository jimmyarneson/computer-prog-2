import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 176)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(124, 176)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(238, 176)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(128, 27)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter a 3 digit number:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(13, 40)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(128, 27)
		self._label2.TabIndex = 4
		self._label2.Text = "Enter a 3 digit number:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(13, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(128, 27)
		self._label3.TabIndex = 5
		self._label3.Text = "Enter a 3 digit number:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(13, 94)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(128, 27)
		self._label4.TabIndex = 6
		self._label4.Text = "Enter a 3 digit number:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(136, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(177, 20)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(136, 47)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(177, 20)
		self._textBox2.TabIndex = 8
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(136, 73)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(177, 20)
		self._textBox3.TabIndex = 9
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(136, 98)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(177, 20)
		self._textBox4.TabIndex = 10
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label5.Location = System.Drawing.Point(13, 121)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(300, 27)
		self._label5.TabIndex = 11
		self._label5.Text = "Sum:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label6.Location = System.Drawing.Point(12, 148)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(300, 27)
		self._label6.TabIndex = 12
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(325, 211)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = str(self._textBox1)
		num2 = str(self._textBox2)
		num3 = str(self._textBox3)
		num4 = str(self._textBox4)
		sum = num1 + num2 + num3 + num4
		avg = str(sum) / 4
		self._label5.Text = "Sum: " + str(sum)
		self._label6.Text = "Average: " + str(avg)