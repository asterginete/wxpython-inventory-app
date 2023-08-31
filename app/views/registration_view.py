import wx
from controllers.authentication_controller import register_user

class RegistrationFrame(wx.Frame):
    def __init__(self, parent, title):
        super(RegistrationFrame, self).__init__(parent, title=title, size=(350, 250))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Username
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_user = wx.StaticText(panel, label="Username:")
        hbox1.Add(lbl_user, flag=wx.RIGHT, border=8)
        self.txt_user = wx.TextCtrl(panel)
        hbox1.Add(self.txt_user, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Password
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_pass = wx.StaticText(panel, label="Password:")
        hbox2.Add(lbl_pass, flag=wx.RIGHT, border=8)
        self.txt_pass = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        hbox2.Add(self.txt_pass, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Confirm Password
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_confirm_pass = wx.StaticText(panel, label="Confirm Password:")
        hbox3.Add(lbl_confirm_pass, flag=wx.RIGHT, border=8)
        self.txt_confirm_pass = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        hbox3.Add(self.txt_confirm_pass, proportion=1)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Register Button
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        btn_register = wx.Button(panel, label="Register")
        hbox4.Add(btn_register)
        vbox.Add(hbox4, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        # Bind the register button to the registration method
        btn_register.Bind(wx.EVT_BUTTON, self.on_register)

        panel.SetSizer(vbox)

    def on_register(self, event):
        username = self.txt_user.GetValue()
        password = self.txt_pass.GetValue()
        confirm_password = self.txt_confirm_pass.GetValue()

        if password != confirm_password:
            wx.MessageBox("Passwords do not match", "Error", wx.OK | wx.ICON_ERROR)
            return

        if register_user(username, password):
            wx.MessageBox("Registration successful", "Success", wx.OK | wx.ICON_INFORMATION)
            self.Close()
        else:
            wx.MessageBox("Registration failed. Username might already exist.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = RegistrationFrame(None, "Registration")
    frame.Show()
    app.MainLoop()
