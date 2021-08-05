# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.9.0 Feb 26 2021)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWindow
###########################################################################

class MainWindow ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"AWS Credentials", pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.text_credentials = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer1.Add( self.text_credentials, 5, wx.ALL|wx.EXPAND, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.label_credentials_id = wx.StaticText( self, wx.ID_ANY, u"Account Name:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.label_credentials_id.Wrap( -1 )

		fgSizer1.Add( self.label_credentials_id, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		combo_accountsChoices = []
		self.combo_accounts = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combo_accountsChoices, 0 )
		fgSizer1.Add( self.combo_accounts, 5, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"AWS Region:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
		self.m_staticText2.Wrap( -1 )

		fgSizer1.Add( self.m_staticText2, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT|wx.ALL, 5 )

		combo_regionChoices = []
		self.combo_region = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, combo_regionChoices, 0 )
		fgSizer1.Add( self.combo_region, 5, wx.ALL|wx.EXPAND, 5 )


		bSizer1.Add( fgSizer1, 1, wx.EXPAND, 5 )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

		self.button_cancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.button_cancel, 1, wx.ALL, 5 )

		self.button_save = wx.Button( self, wx.ID_ANY, u"Save", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_save.Enable( False )

		bSizer2.Add( self.button_save, 1, wx.ALL, 5 )

		self.button_save_and_close = wx.Button( self, wx.ID_ANY, u"Save && Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.button_save_and_close.Enable( False )

		bSizer2.Add( self.button_save_and_close, 1, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.combo_accounts.Bind( wx.EVT_COMBOBOX, self.on_account_change )
		self.combo_region.Bind( wx.EVT_COMBOBOX, self.on_region_change )
		self.button_cancel.Bind( wx.EVT_BUTTON, self.on_cancel_click )
		self.button_save.Bind( wx.EVT_BUTTON, self.on_save_click )
		self.button_save_and_close.Bind( wx.EVT_BUTTON, self.on_save_and_close_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def on_account_change( self, event ):
		event.Skip()

	def on_region_change( self, event ):
		event.Skip()

	def on_cancel_click( self, event ):
		event.Skip()

	def on_save_click( self, event ):
		event.Skip()

	def on_save_and_close_click( self, event ):
		event.Skip()


