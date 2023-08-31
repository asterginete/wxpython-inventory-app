import wx
from views.login_view import LoginFrame

class InventoryApp(wx.App):
    def OnInit(self):
        # Initialize the main window (Login window in this case)
        self.frame = LoginFrame(None, title="Ecommerce Inventory App - Login")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

if __name__ == "__main__":
    app = InventoryApp(False)
    app.MainLoop()
