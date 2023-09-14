import wx
from .views import LoginView

class InventoryApp(wx.App):
    def OnInit(self):
        # Create the main application window
        self.frame = LoginView(None, title="Inventory Management System")
        self.frame.Show()

        # Set the frame as the main window
        self.SetTopWindow(self.frame)

        return True

if __name__ == "__main__":
    app = InventoryApp(redirect=False)
    app.MainLoop()
