import wx
from views.registration_view import RegistrationFrame

class MainApp(wx.App):
    def OnInit(self):
        self.frame = RegistrationFrame(None, title="Ecommerce Inventory Registration")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()
