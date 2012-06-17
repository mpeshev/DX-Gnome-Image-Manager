#/usr/bin/env python

import wx

class EyeSaver(wx.Panel):
	def __init__(self, parent, id):
	# create a panel
		wx.Panel.__init__(self, parent, id)
		self.SetBackgroundColour("white")

		self.brightness = wx.Slider(self, -1, 1, 0.2, 20, (10, 100), (350, 50), wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)

		self.Bind(wx.EVT_SLIDER, self.sliderUpdate)

	def sliderUpdate(self, event):
		self.bpos = self.brightness.GetValue()
		str1 = "brightness = %d" % (self.bpos)

		frame.SetTitle(str1)


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")

EyeSaver(frame, -1)

frame.Show(True)

app.MainLoop()
