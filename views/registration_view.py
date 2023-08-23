import wx
import os

class RegistrationFrame(wx.Frame):
    def __init__(self, parent, title):
        super(RegistrationFrame, self).__init__(parent, title=title, size=(400, 300))
        
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        # Fields
        self.name_ctrl = wx.TextCtrl(panel)
        self.price_ctrl = wx.TextCtrl(panel)
        self.desc_ctrl = wx.TextCtrl(panel)
        self.image_ctrl = wx.FilePickerCtrl(panel, path=os.getcwd(), wildcard="Image files (*.jpg;*.png)|*.jpg;*.png")
        
        # Add to sizer
        vbox.Add(wx.StaticText(panel, label="Item Name:"), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(self.name_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="Price:"), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(self.price_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="Description:"), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(self.desc_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        vbox.Add(wx.StaticText(panel, label="Image:"), flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        vbox.Add(self.image_ctrl, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=10)
        
        # Submit Button
        submit_btn = wx.Button(panel, label="Submit")
        submit_btn.Bind(wx.EVT_BUTTON, self.on_submit)
        vbox.Add(submit_btn, flag=wx.ALIGN_CENTER | wx.TOP, border=10)
        
        panel.SetSizer(vbox)
        
    def on_submit(self, event):
        # Get values
        item_name = self.name_ctrl.GetValue()
        price = float(self.price_ctrl.GetValue())
        description = self.desc_ctrl.GetValue()
        image_link = self.image_ctrl.GetPath()
        
        # Save to database
        connection = connect_to_db()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO items (item_name, price, description, image_link) VALUES (?, ?, ?, ?)", 
                       (item_name, price, description, image_link))
        connection.commit()
        connection.close()
