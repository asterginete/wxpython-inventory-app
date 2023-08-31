import wx
from controllers.authentication_controller import authenticate_user
from views.items_view import ItemsViewFrame

class LoginFrame(wx.Frame):
    def __init__(self, parent, title):
        super(LoginFrame, self).__init__(parent, title=title, size=(300, 200))

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

        # Login Button
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        btn_login = wx.Button(panel, label="Login")
        hbox3.Add(btn_login)
        vbox.Add(hbox3, flag=wx.ALIGN_CENTER | wx.TOP | wx.BOTTOM, border=10)

        # Bind the login button to the login method
        btn_login.Bind(wx.EVT_BUTTON, self.on_login)

        panel.SetSizer(vbox)

    def on_login(self, event):
        username = self.txt_user.GetValue()
        password = self.txt_pass.GetValue()

        if authenticate_user(username, password):
            # If authentication is successful, open the main inventory view and close the login window
            main_frame = ItemsViewFrame(None, title="Items View")
            main_frame.Show()
            self.Close()
        else:
            wx.MessageBox("Invalid username or password", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = LoginFrame(None, "Login")
    frame.Show()
    app.MainLoop()
