import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label5 = System.Windows.Forms.Label()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._label4 = System.Windows.Forms.Label()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._wheels4 = System.Windows.Forms.RadioButton()
		self._label3 = System.Windows.Forms.Label()
		self._wheels3 = System.Windows.Forms.RadioButton()
		self._wheels1 = System.Windows.Forms.RadioButton()
		self._wheels2 = System.Windows.Forms.RadioButton()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._label2 = System.Windows.Forms.Label()
		self._trucks3 = System.Windows.Forms.RadioButton()
		self._trucks1 = System.Windows.Forms.RadioButton()
		self._trucks2 = System.Windows.Forms.RadioButton()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._deck2 = System.Windows.Forms.RadioButton()
		self._deck3 = System.Windows.Forms.RadioButton()
		self._deck1 = System.Windows.Forms.RadioButton()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._misc1 = System.Windows.Forms.CheckBox()
		self._misc2 = System.Windows.Forms.CheckBox()
		self._misc3 = System.Windows.Forms.CheckBox()
		self._misc4 = System.Windows.Forms.CheckBox()
		self._misc5 = System.Windows.Forms.CheckBox()
		self._groupBox4.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Gold
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(24, 215)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(217, 136)
		self._label5.TabIndex = 19
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._misc5)
		self._groupBox4.Controls.Add(self._misc4)
		self._groupBox4.Controls.Add(self._misc3)
		self._groupBox4.Controls.Add(self._misc2)
		self._groupBox4.Controls.Add(self._misc1)
		self._groupBox4.Controls.Add(self._label4)
		self._groupBox4.Location = System.Drawing.Point(253, 177)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(379, 174)
		self._groupBox4.TabIndex = 18
		self._groupBox4.TabStop = False
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(6, 16)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(68, 27)
		self._label4.TabIndex = 3
		self._label4.Text = "Misc:"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._wheels4)
		self._groupBox3.Controls.Add(self._label3)
		self._groupBox3.Controls.Add(self._wheels3)
		self._groupBox3.Controls.Add(self._wheels1)
		self._groupBox3.Controls.Add(self._wheels2)
		self._groupBox3.Location = System.Drawing.Point(24, 12)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(217, 196)
		self._groupBox3.TabIndex = 17
		self._groupBox3.TabStop = False
		# 
		# wheels4
		# 
		self._wheels4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._wheels4.Location = System.Drawing.Point(6, 131)
		self._wheels4.Name = "wheels4"
		self._wheels4.Size = System.Drawing.Size(205, 59)
		self._wheels4.TabIndex = 7
		self._wheels4.TabStop = True
		self._wheels4.Text = "OJ Wheels 61mm: $28"
		self._wheels4.UseVisualStyleBackColor = True
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(6, 16)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(96, 27)
		self._label3.TabIndex = 3
		self._label3.Text = "Wheels:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# wheels3
		# 
		self._wheels3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._wheels3.Location = System.Drawing.Point(6, 101)
		self._wheels3.Name = "wheels3"
		self._wheels3.Size = System.Drawing.Size(183, 31)
		self._wheels3.TabIndex = 6
		self._wheels3.TabStop = True
		self._wheels3.Text = "Orbs 58mm: $24"
		self._wheels3.UseVisualStyleBackColor = True
		# 
		# wheels1
		# 
		self._wheels1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._wheels1.Location = System.Drawing.Point(6, 46)
		self._wheels1.Name = "wheels1"
		self._wheels1.Size = System.Drawing.Size(211, 31)
		self._wheels1.TabIndex = 4
		self._wheels1.TabStop = True
		self._wheels1.Text = "Spitfire 51mm: $20"
		self._wheels1.UseVisualStyleBackColor = True
		# 
		# wheels2
		# 
		self._wheels2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._wheels2.Location = System.Drawing.Point(6, 73)
		self._wheels2.Name = "wheels2"
		self._wheels2.Size = System.Drawing.Size(183, 31)
		self._wheels2.TabIndex = 5
		self._wheels2.TabStop = True
		self._wheels2.Text = "Bones 55mm: $22"
		self._wheels2.UseVisualStyleBackColor = True
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label2)
		self._groupBox2.Controls.Add(self._trucks3)
		self._groupBox2.Controls.Add(self._trucks1)
		self._groupBox2.Controls.Add(self._trucks2)
		self._groupBox2.Location = System.Drawing.Point(414, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(218, 159)
		self._groupBox2.TabIndex = 16
		self._groupBox2.TabStop = False
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 16)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(78, 27)
		self._label2.TabIndex = 3
		self._label2.Text = "Trucks:"
		# 
		# trucks3
		# 
		self._trucks3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._trucks3.Location = System.Drawing.Point(6, 101)
		self._trucks3.Name = "trucks3"
		self._trucks3.Size = System.Drawing.Size(170, 31)
		self._trucks3.TabIndex = 6
		self._trucks3.TabStop = True
		self._trucks3.Text = "Indipendent: $45"
		self._trucks3.UseVisualStyleBackColor = True
		# 
		# trucks1
		# 
		self._trucks1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._trucks1.Location = System.Drawing.Point(6, 46)
		self._trucks1.Name = "trucks1"
		self._trucks1.Size = System.Drawing.Size(155, 31)
		self._trucks1.TabIndex = 4
		self._trucks1.TabStop = True
		self._trucks1.Text = "Krux Trux: $35"
		self._trucks1.UseVisualStyleBackColor = True
		# 
		# trucks2
		# 
		self._trucks2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._trucks2.Location = System.Drawing.Point(6, 73)
		self._trucks2.Name = "trucks2"
		self._trucks2.Size = System.Drawing.Size(206, 31)
		self._trucks2.TabIndex = 5
		self._trucks2.TabStop = True
		self._trucks2.Text = "Thunder Trucks: $40"
		self._trucks2.UseVisualStyleBackColor = True
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._deck2)
		self._groupBox1.Controls.Add(self._deck3)
		self._groupBox1.Controls.Add(self._deck1)
		self._groupBox1.Location = System.Drawing.Point(247, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(161, 159)
		self._groupBox1.TabIndex = 15
		self._groupBox1.TabStop = False
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(68, 27)
		self._label1.TabIndex = 3
		self._label1.Text = "Decks:"
		# 
		# deck2
		# 
		self._deck2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._deck2.Location = System.Drawing.Point(6, 73)
		self._deck2.Name = "deck2"
		self._deck2.Size = System.Drawing.Size(140, 31)
		self._deck2.TabIndex = 6
		self._deck2.TabStop = True
		self._deck2.Text = "Revive: $50"
		self._deck2.UseVisualStyleBackColor = True
		# 
		# deck3
		# 
		self._deck3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._deck3.Location = System.Drawing.Point(6, 101)
		self._deck3.Name = "deck3"
		self._deck3.Size = System.Drawing.Size(140, 31)
		self._deck3.TabIndex = 4
		self._deck3.TabStop = True
		self._deck3.Text = "Hockey: $65"
		self._deck3.UseVisualStyleBackColor = True
		# 
		# deck1
		# 
		self._deck1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._deck1.Location = System.Drawing.Point(6, 46)
		self._deck1.Name = "deck1"
		self._deck1.Size = System.Drawing.Size(140, 31)
		self._deck1.TabIndex = 5
		self._deck1.TabStop = True
		self._deck1.Text = "Element: $45"
		self._deck1.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Purple
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button3.Location = System.Drawing.Point(171, 357)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(315, 44)
		self._button3.TabIndex = 14
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Purple
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button2.Location = System.Drawing.Point(492, 357)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(140, 44)
		self._button2.TabIndex = 13
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Purple
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._button1.Location = System.Drawing.Point(25, 357)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(140, 44)
		self._button1.TabIndex = 12
		self._button1.Text = "Checkout"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# misc1
		# 
		self._misc1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._misc1.Location = System.Drawing.Point(6, 46)
		self._misc1.Name = "misc1"
		self._misc1.Size = System.Drawing.Size(212, 28)
		self._misc1.TabIndex = 9
		self._misc1.Text = "MOB Grip Tape: $10"
		self._misc1.UseVisualStyleBackColor = True
		# 
		# misc2
		# 
		self._misc2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._misc2.Location = System.Drawing.Point(6, 80)
		self._misc2.Name = "misc2"
		self._misc2.Size = System.Drawing.Size(212, 28)
		self._misc2.TabIndex = 10
		self._misc2.Text = "Bones Bearings: $30"
		self._misc2.UseVisualStyleBackColor = True
		# 
		# misc3
		# 
		self._misc3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._misc3.Location = System.Drawing.Point(6, 114)
		self._misc3.Name = "misc3"
		self._misc3.Size = System.Drawing.Size(162, 28)
		self._misc3.TabIndex = 11
		self._misc3.Text = "Riser Pads: $2"
		self._misc3.UseVisualStyleBackColor = True
		# 
		# misc4
		# 
		self._misc4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._misc4.Location = System.Drawing.Point(201, 46)
		self._misc4.Name = "misc4"
		self._misc4.Size = System.Drawing.Size(172, 28)
		self._misc4.TabIndex = 12
		self._misc4.Text = "Nuts N Bolts: $3"
		self._misc4.UseVisualStyleBackColor = True
		# 
		# misc5
		# 
		self._misc5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._misc5.Location = System.Drawing.Point(201, 80)
		self._misc5.Name = "misc5"
		self._misc5.Size = System.Drawing.Size(162, 28)
		self._misc5.TabIndex = 13
		self._misc5.Text = "Assembly: $10"
		self._misc5.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Yellow
		self.ClientSize = System.Drawing.Size(656, 413)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "skateboard"
		self._groupBox4.ResumeLayout(False)
		self._groupBox3.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		total = 0
		
		if self._wheels1.Checked:
			total += 20
		elif self._wheels2.Checked:
			total += 22
		elif self._wheels3.Checked:
			total += 24
		elif self._wheels4.Checked:
			total += 28
			
			
		if self._deck1.Checked:
			total += 45
		elif self._deck2.Checked:
			total += 50
		elif self._deck3.Checked:
			total += 60
			
		if self._trucks1.Checked:
			total += 35
		elif self._trucks2.Checked:
			total += 40
		elif self._trucks3.Checked:
			total += 45
			
		if self._misc1.Checked:
			total += 10
		if self._misc2.Checked:
			total += 30
		if self._misc3.Checked:
			total += 2
		if self._misc4.Checked:
			total += 10
		if self._misc5.Checked:
			total += 3
			
		tax = total * 0.06
		totalspent = total + tax
			
		self._label5.Text = "Total Spent: $" + str(total) + "      Sales Tax: $" + str(tax) + "       _______________" + "      Total: $" + str(totalspent)
		

	def Button3Click(self, sender, e):
		self._label5.Text = ""
		
		self._wheels1.Checked = False
		self._wheels2.Checked = False
		self._wheels3.Checked = False
		self._wheels4.Checked = False
		self._deck1.Checked = False
		self._deck2.Checked = False
		self._deck3.Checked = False
		self._trucks1.Checked = False 
		self._trucks2.Checked = False
		self._trucks3.Checked = False
		self._misc1.Checked = False
		self._misc2.Checked = False
		self._misc3.Checked = False
		self._misc4.Checked = False
		self._misc5.Checked = False

	def Button2Click(self, sender, e):
		Application.Exit()