import wx
from controllers.order_controller import get_all_orders, create_order

class OrderViewFrame(wx.Frame):
    def __init__(self, parent, title):
        super(OrderViewFrame, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Order Creation Controls
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_item_number = wx.StaticText(panel, label="Item Number:")
        hbox1.Add(lbl_item_number, flag=wx.RIGHT, border=8)
        self.txt_item_number = wx.TextCtrl(panel)
        hbox1.Add(self.txt_item_number, proportion=1)
        lbl_quantity = wx.StaticText(panel, label="Quantity:")
        hbox1.Add(lbl_quantity, flag=wx.RIGHT, border=8)
        self.txt_quantity = wx.TextCtrl(panel)
        hbox1.Add(self.txt_quantity, proportion=1)
        btn_order = wx.Button(panel, label="Place Order")
        hbox1.Add(btn_order, flag=wx.LEFT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Bind the order button to the order method
        btn_order.Bind(wx.EVT_BUTTON, self.on_order)

        # Orders Table
        self.orders_list = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.orders_list.InsertColumn(0, 'Order ID')
        self.orders_list.InsertColumn(1, 'Item Number')
        self.orders_list.InsertColumn(2, 'Quantity')
        self.orders_list.InsertColumn(3, 'Date Ordered')
        vbox.Add(self.orders_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Load all orders initially
        self.load_orders()

        panel.SetSizer(vbox)

    def load_orders(self):
        orders = get_all_orders()
        self.orders_list.DeleteAllItems()
        for order in orders:
            index = self.orders_list.InsertItem(self.orders_list.GetItemCount(), str(order['order_id']))
            self.orders_list.SetItem(index, 1, str(order['item_number']))
            self.orders_list.SetItem(index, 2, str(order['quantity']))
            self.orders_list.SetItem(index, 3, order['date_ordered'])

    def on_order(self, event):
        item_number = int(self.txt_item_number.GetValue())
        quantity = int(self.txt_quantity.GetValue())

        if create_order(item_number, quantity):
            wx.MessageBox("Order placed successfully", "Success", wx.OK | wx.ICON_INFORMATION)
            self.load_orders()
        else:
            wx.MessageBox("Failed to place order. Check item number and quantity.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = OrderViewFrame(None, "Order Management")
    frame.Show()
    app.MainLoop()
