import wx
import os


# A First Application: "Hello,World"
# app = wx.App(False)  # create a now app, don't redirect stdout/stderr to a window.
# fram = wx.Frame(None,wx.ID_ANY,"Hello World")   # A Frame is a top-level window
# fram.Show(True)  # Show the frame
# app.MainLoop()

# Building a simple text editor

class  MyFrame(wx.Frame):
    """we simple derive a now class of frame. """
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.control = wx.TextCtrl(self,style = wx.TE_MULTILINE)
        self.Show(True)

# app = wx.App(False)
# frame = MyFrame(None,'Small editor')
# app.MainLoop()

# Adding a menu bar

class  MainWindow(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(200,100))
        self.control = wx.TextCtrl(self,style = wx.TE_MULTILINE)
        self.CreateStatusBar()  # A statusbar in the bottom of the window

        # Setting up the menu.
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        # Setting up the menu.
        menuOpen = filemenu.Append(wx.ID_OPEN, "&Open","Open a file to edit")
        menuAbout= filemenu.Append(wx.ID_ABORT,"&About"," Information about this program")
        # self.Bind(wx.EVT_MENU,self.OnAbout,menuItem)
        # filemenu.AppendSeparator)
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit", "Terminate the program")


        # Creating the menubar.
        menuBar =wx.MenuBar()
        menuBar.Append(filemenu,"&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.


        # set events.
        self.Bind(wx.EVT_MENU,self.OnOpen,menuOpen)
        self.Bind(wx.EVT_MENU,self.OnAbout,menuAbout)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)

        self.sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.buttons = []
        for i in range(0,6):
            self.buttons.append(wx.Button(self, -1 , "Button &"+ str(i+1)))
            self.sizer2.Add(self.buttons[i],1,wx.EXPAND)

        # Use some sizers to see layout options

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.control,1,wx.EXPAND)
        self.sizer.Add(self.sizer2,0,wx.EXPAND)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)
        self.Show()

    def OnAbout(self,e):
        # A message dialog box with an OK button.wx.OK is a  standard ID in wxWidgets.
        dlg = wx.MessageDialog(self,"A smail text editor","About Sample Editor",wx.OK)
        dlg.ShowModal()  # Show it
        dlg.Destroy()  # finally destroy it wen finished.

    def OnExit(self,e):
        self.Close(True)  #close the frame

    def OnOpen(self,e):
        """ Open a file"""
        self.dirname = ''
        dlg = wx.FileDialog(self,"Choose a file",self.dirname,"","*.*",wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname,self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()

# app = wx.App(False)
# frame = MainWindow(None, "Sample editor")
# app.MainLoop()

# A Working Example Our first label within a panel

1
import wx

2


class ExamplePanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.quote = wx.StaticText(self, label="Your quote :", pos=(20, 30))
        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it

        self.logger = wx.TextCtrl(self, pos=(300, 20), size=(200, 300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button

        self.button = wx.Button(self, label="Save", pos=(200, 325))

        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        # the edit control - one line version.

        self.lblname = wx.StaticText(self, label="Your name :", pos=(20, 60))

        self.editname = wx.TextCtrl(self, value="Enter here your name", pos=(150, 60), size=(140, -1))

        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)

        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control

        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow Pages']

        self.lblhear = wx.StaticText(self, label="How did you hear from us ?", pos=(20, 90))

        self.edithear = wx.ComboBox(self, pos=(150, 90), size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)

        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)

        self.Bind(wx.EVT_TEXT, self.EvtText, self.edithear)

        # Checkbox

        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?", pos=(20, 180))

        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes

        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']

        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList, majorDimension=3,

        style = wx.RA_SPECIFY_COLS)

        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)
    def EvtRadioBox(self, event):
        self.logger.AppendText('EvtRadioBox: %d\n' % event.GetInt())

    def EvtComboBox(self, event):
        self.logger.AppendText('EvtComboBox: %s\n' % event.GetString())

    def OnClick(self, event):
        self.logger.AppendText(" Click on object with Id %d\n" % event.GetId())
    def EvtText(self, event):
        self.logger.AppendText('EvtText: %s\n' % event.GetString())
    def EvtChar(self, event):
        self.logger.AppendText('EvtChar: %d\n' % event.GetKeyCode())
        event.Skip()
    def EvtCheckBox(self, event):
        self.logger.AppendText('EvtCheckBox: %d\n' % event.Checked())
app = wx.App(False)
frame = wx.Frame(None)
panel = ExamplePanel(frame)
frame.Show()
app.MainLoop()