import os
import wx
import helpers

from ui import MainWindow

class MainUi(MainWindow):
    region_list = []
    account_list = []

    def __init__(self, parent):
        super().__init__(parent)
        account_list = helpers.get_local_accounts()
        self.combo_accounts.Items = account_list
        self.combo_region.Items = helpers.get_aws_regions()

    def on_account_change(self: MainWindow, event: wx.Event):
        # If the account/profile exists, load the currently-configured region if it has one.
        region = helpers.get_profile_region(self.combo_accounts.Value)
        if region != '':
            self.combo_region.Value = region

        if (
            self.combo_accounts.Value != '' and 
            self.combo_region.Value != '' and 
            self.text_credentials.Value != '' 
        ):
            self.button_save.Enable(True)
            self.button_save_and_close.Enable(True)

    def on_region_change(self: MainWindow, event: wx.Event):
        if self.combo_accounts.Value != '' and self.combo_region.Value != '' and self.text_credentials != '':
            self.button_save.Enable(True)
            self.button_save_and_close.Enable(True)

    def on_cancel_click(self: MainWindow, event: wx.Event):
        self.Close()
        self.Destroy()

    def on_save_click(self: MainWindow, event: wx.Event):
        result = helpers.parse_input(self.combo_accounts.Value, self.combo_region.Value, self.text_credentials.Value)
        if result:
            wx.MessageBox("AWS Credentials file updated successfully.", "Success", wx.OK_DEFAULT | wx.ICON_INFORMATION)
            result = helpers.update_aws_regions(self.combo_region.Value, self.combo_accounts.Value)
            if result['success'] == False:
                if result['error'] == 'RequestExpired':
                    wx.MessageBox('SSO Credentials appear to have expired, unable to update Regions.', 'Credentials Expired', wx.OK_DEFAULT | wx.ICON_ERROR)
                else:
                    wx.MessageBox('Uknown error. Failed to update AWS regions.', 'Error', wx.OK_DEFAULT | wx.ICON_ERROR)
                    print(result['error'])

    def on_save_and_close_click(self: MainWindow, event: wx.Event):
        self.on_save_click(event)
        self.Close()
        self.Destroy()

def run():
    app = wx.App()
    main = MainUi(None)
    main.Show()
    app.MainLoop()
    
