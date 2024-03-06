import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._comboBox2 = System.Windows.Forms.ComboBox()
		self._comboBox3 = System.Windows.Forms.ComboBox()
		self.SuspendLayout()
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gold
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(12, 98)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(153, 21)
		self._label5.TabIndex = 27
		self._label5.Text = "Total:"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Purple
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button1.Location = System.Drawing.Point(26, 122)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 31)
		self._button1.TabIndex = 20
		self._button1.Text = "Checkout"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Gold
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(153, 21)
		self._label1.TabIndex = 28
		self._label1.Text = "Base Fee - $50"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Gold
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(13, 30)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(57, 21)
		self._label3.TabIndex = 30
		self._label3.Text = "Styles:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Gold
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(13, 51)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(57, 21)
		self._label4.TabIndex = 31
		self._label4.Text = "Sizes:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Gold
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(12, 72)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(58, 21)
		self._label6.TabIndex = 32
		self._label6.Text = "Colors:"
		# 
		# comboBox1
		# 
		self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["Regular Shades",
			"Folding Shades",
			"Roman Shades"]))
		self._comboBox1.Location = System.Drawing.Point(76, 32)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(89, 21)
		self._comboBox1.TabIndex = 33
		# 
		# comboBox2
		# 
		self._comboBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox2.FormattingEnabled = True
		self._comboBox2.Items.AddRange(System.Array[System.Object](
			["25 Inches Long",
			"27 Inches Long",
			"32 Inches Long ",
			"40 Inches Long"]))
		self._comboBox2.Location = System.Drawing.Point(76, 53)
		self._comboBox2.Name = "comboBox2"
		self._comboBox2.Size = System.Drawing.Size(89, 21)
		self._comboBox2.TabIndex = 34
		# 
		# comboBox3
		# 
		self._comboBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._comboBox3.FormattingEnabled = True
		self._comboBox3.Items.AddRange(System.Array[System.Object](
			["Natural",
			"Blue ",
			"Teal ",
			"Red ",
			"Green"]))
		self._comboBox3.Location = System.Drawing.Point(76, 74)
		self._comboBox3.Name = "comboBox3"
		self._comboBox3.Size = System.Drawing.Size(89, 21)
		self._comboBox3.TabIndex = 35
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(176, 159)
		self.Controls.Add(self._comboBox3)
		self.Controls.Add(self._comboBox2)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "shadedesigner"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		basefee = 50
		
		styles = self._comboBox1.SelectedIndex
		sizes = self._comboBox2.SelectedIndex
		colors = self._comboBox3.SelectedIndex
		l = [0, 10, 15]
		f = [0, 2, 4, 6]
		g = [5, 0, 0, 0, 0]
		
		basefee+= l[styles]
		basefee+=f[sizes]
		basefee+=g[colors]
		
		self._label5.Text = "Total $ " + str(basefee)