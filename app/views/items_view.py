import wx
from controllers.inventory_controller import get_all_items

class ItemsViewFrame(wx.Frame):
    def __init__(self, parent, title):
        super(ItemsViewFrame, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Search Controls
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_search = wx.StaticText(panel, label="Search:")
        hbox1.Add(lbl_search, flag=wx.RIGHT, border=8)
        self.txt_search = wx.TextCtrl(panel)
        hbox1.Add(self.txt_search, proportion=1)
        btn_search = wx.Button(panel, label="Search")
        hbox1.Add(btn_search, flag=wx.LEFT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Bind the search button to the search method
        btn_search.Bind(wx.EVT_BUTTON, self.on_search)

        # Items Table
        self.items_list = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.items_list.InsertColumn(0, 'Item Number')
        self.items_list.InsertColumn(1, 'Item Name')
        self.items_list.InsertColumn(2, 'Price')
        self.items_list.InsertColumn(3, 'Description')
        self.items_list.InsertColumn(4, 'Date of Registration')
        vbox.Add(self.items_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Load all items initially
        self.load_items()

        panel.SetSizer(vbox)

    def load_items(self, search_query=None):
        items = get_all_items(search_query)
        self.items_list.DeleteAllItems()
        for item in items:
            index = self.items_list.InsertItem(self.items_list.GetItemCount(), str(item['item_number']))
            self.items_list.SetItem(index, 1, item['item_name'])
            self.items_list.SetItem(index, 2, str(item['price']))
            self.items_list.SetItem(index, 3, item['description'])
            self.items_list.SetItem(index, 4, item['date_of_registration'])

    def on_search(self, event):
        search_query = self.txt_search.GetValue()
        self.load_items(search_query)

if __name__ == "__main__":
    app = wx.App(False)
    frame = ItemsViewFrame(None, "Items View")
    frame.Show()
    app.MainLoop()
