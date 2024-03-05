import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._label1 = System.Windows.Forms.Label()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.Location = System.Drawing.Point(13, 13)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(275, 34)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Day Time(6:00 AM - 5:59 PM)"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(295, -3)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(91, 28)
		self._label1.TabIndex = 1
		self._label1.Text = "Rate:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.Location = System.Drawing.Point(13, 43)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(275, 34)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Evening(6:00 PM - 11:59 PM)"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.Location = System.Drawing.Point(12, 74)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(275, 34)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Off Time(12:00 AM - 5:59 AM)"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(295, 25)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(91, 22)
		self._label2.TabIndex = 4
		self._label2.Text = "$ 0.07"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(294, 52)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(91, 25)
		self._label3.TabIndex = 5
		self._label3.Text = "$0.12"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(293, 78)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(91, 26)
		self._label4.TabIndex = 6
		self._label4.Text = "$0.05"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 111)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(230, 28)
		self._label5.TabIndex = 7
		self._label5.Text = "Enter Time Spent On Call: "
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(249, 115)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(123, 26)
		self._textBox1.TabIndex = 8
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 148)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(360, 28)
		self._label6.TabIndex = 9
		self._label6.Text = "Rate Catagorey and Charge"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Gold
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(13, 180)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(359, 42)
		self._label7.TabIndex = 10
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Goldenrod
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 225)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(96, 37)
		self._button1.TabIndex = 11
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(114, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(156, 37)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Goldenrod
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(276, 225)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(96, 37)
		self._button3.TabIndex = 13
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(398, 265)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "longdistancecalls"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		time = float(self._textBox1.Text)
		total = 0
		t = ""
		
		if self._radioButton1.Checked:
			total += 0.07 * time
			t = "Day Time"
		elif self._radioButton2.Checked:
			total += 0.12 * time
			t = "Evening"
		elif self._radioButton3.Checked:
			total += 0.05 * time
			t= "Off Time"
		self._label7.Text = t+ "  $ " + str(total)

	def Button2Click(self, sender, e):
		self._radioButton1.Checked = False
		self._radioButton2.Checked = False
		self._radioButton3.Checked = False
		self._label7.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()