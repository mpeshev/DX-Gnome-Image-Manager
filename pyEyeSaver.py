#/usr/bin/env python

# A tool for brighness and gamma changes 
# used on ThinkPad on Mate Desktop on Fedora 17


import wx
from wx.lib.agw.floatspin import FloatSpin, EVT_FLOATSPIN, FS_LEFT 
from subprocess import call


# Override standard slider to support float values
class FloatSlider(wx.Slider):
    def GetValue(self):

        return (float(wx.Slider.GetValue(self)))/20

# general EyeSaver class with the form and functionality
class EyeSaver(wx.Panel):
	def __init__(self, parent, id):
	# create a panel
		wx.Panel.__init__(self, parent, id)
		self.SetBackgroundColour("white")

		# add all labels and slider controls
		self.brightlabel = wx.StaticText(self, label="Brightness: 1", pos=(10, 40))
		self.brightness = FloatSlider(self, id=360, value=20, minValue=2, maxValue=50, pos=(10, 60), size=(350, 50), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)

		self.gammaredlabel = wx.StaticText(self, label="Red Gamma: 1", pos=(10, 100))
		self.gammared = FloatSlider(self, id=370, value=20, minValue=2, maxValue=50, pos=(10, 120), size=(350, 50), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
		self.gammagreenlabel = wx.StaticText(self, label="Green Gamma: 1", pos=(10, 160))
		self.gammagreen = FloatSlider(self, id=380, value=20, minValue=2, maxValue=50, pos=(10, 180), size=(350, 50), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
		self.gammabluelabel = wx.StaticText(self, label="Blue Gamma: 1", pos=(10, 220))
		self.gammablue = FloatSlider(self, id=390, value=20, minValue=2, maxValue=50, pos=(10, 240), size=(350, 50), style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS)
		

		self.Bind(wx.EVT_SLIDER, self.sliderUpdate)

	# manage the sliderUpdate when a slider is dragged
	def sliderUpdate(self, event):
		bpos = self.brightness.GetValue()
		brightlabel = "brightness = %f" % (bpos)
		event_id = event.GetId()
		
		#call(["xrandr", "--output", "LVDS1", "--brightness", str(bpos)])

		self.brightlabel.SetLabel(brightlabel)
		# handle brighness event
		if event_id == 360:
			call(["xrandr", "--output", "LVDS1", "--brightness", str(bpos)])
		
		# handle red gamma event
		elif event_id == 370:
			red = self.gammared.GetValue()
			gammaredstr = "Red Gamma: %f" % (red)
			self.gammaredlabel.SetLabel(gammaredstr)
			call(["xgamma", "-rgamma", str(red)])

		# handle green gamma event
		elif event_id == 380:
			green = self.gammagreen.GetValue()
			gammagreenstr = "Green Gamma: %f" % (green)
			self.gammagreenlabel.SetLabel(gammagreenstr)
			call(["xgamma", "-ggamma", str(green)])

		# handle blue gamma event
		elif event_id == 390:
			blue = self.gammablue.GetValue()
			gammabluestr = "Blue Gamma: %f" % (blue)
			self.gammabluelabel.SetLabel(gammabluestr)
			call(["xgamma", "-bgamma", str(blue)])
		

		#	call(["xrandr", "--output", "LVDS1", "--brightness", str(self.bpos)])
		#elif event_id == 370:
		#	call([""])
		#elif event_id == 380:
#
#		elif event_id == 390:

		frame.SetTitle(brightlabel)


app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World", size=(400, 400))

EyeSaver(frame, -1)

frame.Show(True)

app.MainLoop()
