import wx
from controllers.review_controller import get_all_reviews, add_review

class ReviewViewFrame(wx.Frame):
    def __init__(self, parent, title):
        super(ReviewViewFrame, self).__init__(parent, title=title, size=(800, 600))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Review Creation Controls
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        lbl_item_number = wx.StaticText(panel, label="Item Number:")
        hbox1.Add(lbl_item_number, flag=wx.RIGHT, border=8)
        self.txt_item_number = wx.TextCtrl(panel)
        hbox1.Add(self.txt_item_number, proportion=1)
        lbl_rating = wx.StaticText(panel, label="Rating (1-5):")
        hbox1.Add(lbl_rating, flag=wx.RIGHT, border=8)
        self.txt_rating = wx.TextCtrl(panel)
        hbox1.Add(self.txt_rating, proportion=1)
        lbl_comment = wx.StaticText(panel, label="Comment:")
        hbox1.Add(lbl_comment, flag=wx.RIGHT, border=8)
        self.txt_comment = wx.TextCtrl(panel, size=(200, -1))
        hbox1.Add(self.txt_comment, proportion=1)
        btn_add = wx.Button(panel, label="Add Review")
        hbox1.Add(btn_add, flag=wx.LEFT, border=8)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Bind the add button to the add review method
        btn_add.Bind(wx.EVT_BUTTON, self.on_add_review)

        # Reviews Table
        self.reviews_list = wx.ListCtrl(panel, style=wx.LC_REPORT)
        self.reviews_list.InsertColumn(0, 'Review ID')
        self.reviews_list.InsertColumn(1, 'Item Number')
        self.reviews_list.InsertColumn(2, 'Rating')
        self.reviews_list.InsertColumn(3, 'Comment')
        vbox.Add(self.reviews_list, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)

        # Load all reviews initially
        self.load_reviews()

        panel.SetSizer(vbox)

    def load_reviews(self):
        reviews = get_all_reviews()
        self.reviews_list.DeleteAllItems()
        for review in reviews:
            index = self.reviews_list.InsertItem(self.reviews_list.GetItemCount(), str(review['review_id']))
            self.reviews_list.SetItem(index, 1, str(review['item_number']))
            self.reviews_list.SetItem(index, 2, str(review['rating']))
            self.reviews_list.SetItem(index, 3, review['comment'])

    def on_add_review(self, event):
        item_number = int(self.txt_item_number.GetValue())
        rating = int(self.txt_rating.GetValue())
        comment = self.txt_comment.GetValue()

        if 1 <= rating <= 5 and add_review(item_number, rating, comment):
            wx.MessageBox("Review added successfully", "Success", wx.OK | wx.ICON_INFORMATION)
            self.load_reviews()
        else:
            wx.MessageBox("Failed to add review. Check the provided details.", "Error", wx.OK | wx.ICON_ERROR)

if __name__ == "__main__":
    app = wx.App(False)
    frame = ReviewViewFrame(None, "Product Reviews")
    frame.Show()
    app.MainLoop()
