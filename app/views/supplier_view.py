import wx
from controllers.supplier_controller import get_all_suppliers, add_supplier

class SupplierViewFrame(wx.Frame):
    def __init__(self, parent, title):
        super(SupplierViewFrame, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Supplier Creation Controls
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_name = wx.StaticText(panel, label="Supplier Name:")
        hbox1.Add(lbl_name, flag=wx.RIGHT, border=8)
        self.txt_name = wx.TextCtrl(panel)
        hbox1.Add(self.txt_name, proportion=1)
        lbl_contact = wx.StaticText(panel, label="Contact Info:")
        hbox1.Add(lbl_contact, flag=wx.RIGHT, border=8)
        self.txt_contact = wx.TextCtrl(panel)
        hbox1.Add(self.txt_contact, proportion=1)
        btn_add = wx.Button(panel, label="Add Supplier")
        hbox1.Add(btn_add, flag=wx.LEFT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Bind the add button to the add supplier method
        btn_add.Bind(wx.EVT_BUTTON, self.on_add_supplier)

        # Suppliers Table
        self.suppliers_list = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.suppliers_list.InsertColumn(0, 'Supplier ID')
        self.suppliers_list.InsertColumn(1, 'Supplier Name')
        self.suppliers_list.InsertColumn(2, 'Contact Info')
        vbox.Add(self.suppliers_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Load all suppliers initially
        self.load_suppliers()

        panel.SetSizer(vbox)

    def load_suppliers(self):
        suppliers = get_all_suppliers()
        self.suppliers_list.DeleteAllItems()
        for supplier in suppliers:
            index = self.suppliers_list.InsertItem(self.suppliers_list.GetItemCount(), str(supplier['supplier_id']))
            self.suppliers_list.SetItem(index, 1, supplier['name'])
            self.suppliers_list.SetItem(index, 2, supplier['contact_info'])

    def on_add_supplier(self, event):
        name = self.txt_name.GetValue()
        contact_info = self.txt_contact.GetValue()

        if add_supplier(name, contact_info):
            wx.MessageBox("Supplier added successfully", "Success", wx.OK | wx.ICON_INFORMATION)
            self.load_suppliers()
        else:
            wx.MessageBox("Failed to add supplier. Check the provided details.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = SupplierViewFrame(None, "Supplier Management")
    frame.Show()
    app.MainLoop()
