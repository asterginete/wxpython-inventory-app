import wx
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from controllers.inventory_controller import get_sales_data, get_stock_levels

class AnalyticsViewFrame(wx.Frame):
    def __init__(self, parent, title):
        super(AnalyticsViewFrame, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Dropdown to select type of analytics
        self.choices = ["Sales Trends", "Stock Levels"]
        self.choice_box = wx.Choice(panel, choices=self.choices)
        self.choice_box.Bind(wx.EVT_CHOICE, self.on_choice)
        vbox.Add(self.choice_box, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Placeholder for the plot
        self.figure, self.ax = plt.subplots(figsize=(6, 4))
        self.canvas = FigureCanvas(panel, -1, self.figure)
        vbox.Add(self.canvas, proportion=1, flag=wx.EXPAND)

        panel.SetSizer(vbox)

    def on_choice(self, event):
        choice = self.choice_box.GetString(self.choice_box.GetSelection())
        if choice == "Sales Trends":
            self.plot_sales_trends()
        elif choice == "Stock Levels":
            self.plot_stock_levels()

    def plot_sales_trends(self):
        sales_data = get_sales_data()
        self.ax.clear()
        sns.lineplot(data=sales_data, x="Date", y="Sales", ax=self.ax)
        self.ax.set_title("Sales Trends Over Time")
        self.canvas.draw()

    def plot_stock_levels(self):
        stock_data = get_stock_levels()
        self.ax.clear()
        sns.barplot(data=stock_data, x="Item", y="Stock Level", ax=self.ax)
        self.ax.set_title("Current Stock Levels")
        self.ax.tick_params(axis="x", rotation=45)
        self.canvas.draw()

if __name__ == "__main__":
    app = wx.App(False)
    frame = AnalyticsViewFrame(None, "Inventory Analytics")
    frame.Show()
    app.MainLoop()
