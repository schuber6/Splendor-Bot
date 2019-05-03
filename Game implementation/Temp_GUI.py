# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 12:53:34 2019

@author: huber.288
"""

import wx
import numpy as np
from Splendor import Splendor
Game=Splendor(1,0)

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='Splendor')
        self.Size = wx.Size( 1200,400 )
        self.panel = wx.Panel(self)
        self.gems=Game.gems
        self.nobles=Game.nobles
        self.cards=Game.cards
        self.player=Game.player
        self.gnames=['White','Blue','Green','Red','Black','Gold','']
        self.empty_cell = (0,0)
        self.rows=7
        self.cols=3
        self.gap=1
        self.my_sizer = wx.FlexGridSizer(self.rows, self.cols, self.gap)
        self.panel.SetSizer(self.my_sizer) 
        self.DisplayGems()
        self.DisplayNobles()
        self.DisplayCards()
        self.DisplayPlayer()
        self.Show()
        
    def on_press_take(self, event):
        gems=[]
        for i in range(len(self.text_ctrl)):
            gems.append(int(self.text_ctrl[i].GetValue()))
        gems=np.array(gems)
        print(gems)
        print(Game.CheckGems(0,gems))
        Game.TakeGems(0,gems)
        self.gems=Game.gems
        self.RefreshGems()
        self.RefreshPlayer()
        self.RefreshNobles()
        self.RefreshCards()
    def on_press_buy(self, event):
        for i in range(len(self.btn_ids)):
            if self.btn_ids[i]==event.GetId():
                card=i
        gems=np.append(Game.cards[card].cost-Game.player[0].bonuses,[0])
        Game.BuyCard(0,card,gems)
        self.RefreshGems()
        self.RefreshPlayer()
        self.RefreshNobles()
        self.RefreshCards()
    def on_press_reserve(self, event):
        for i in range(len(self.reserve_ids)):
            if self.reserve_ids[i]==event.GetId():
                card=i
        gems=np.array([0,0,0,0,0,1])
        Game.ReserveCard(0,card,gems)
        self.RefreshGems()
        self.RefreshPlayer()
        self.RefreshNobles()
        self.RefreshCards()

    def RefreshGems(self):
        for i in range(7):
            self.stn[i].SetLabel(self.gnames[i])
        for i in range(6):
            self.text_ctrl[i].SetValue('0')
        for i in range(6):
            self.st[i].SetLabel(str(self.gems[i]))

    def DisplayGems(self):
        self.stn=[]
        for i in range(7):
            self.stn.append(wx.StaticText(self.panel, label=self.gnames[i], style=wx.ALIGN_LEFT))
            self.my_sizer.Add(self.stn[i], 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        self.text_ctrl=[]
        for i in range(6):
            self.text_ctrl.append(wx.TextCtrl(self.panel,value='0',size=[30,30]))
            self.my_sizer.Add(self.text_ctrl[i], 0, wx.ALL | wx.FIXED_MINSIZE, 5)        
        my_btn = wx.Button(self.panel, label='Take Gems')
        self.my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        my_btn.Bind(wx.EVT_BUTTON, self.on_press_take)
        self.st=[]
        for i in range(6):
            self.st.append(wx.StaticText(self.panel, label=str(self.gems[i]), style=wx.ALIGN_LEFT))
            self.my_sizer.Add(self.st[i], 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
    def DisplayNobles(self):
        stn=[]
        stn.append(wx.StaticText(self.panel, label='Nobles:', style=wx.ALIGN_LEFT))
        for i in range(len(self.nobles)):
            nob=str(self.nobles[i]).split(',')[0]+','+str(self.nobles[i]).split(',')[2]
            stn.append(wx.StaticText(self.panel, label=nob, style=wx.ALIGN_LEFT))
        self.Noblestn=stn
        for i in range(len(stn)):
            self.my_sizer.Add(stn[i], 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        if len(stn)<self.rows:
            for i in range(self.rows-len(stn)):
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
    def RefreshNobles(self):
        for i in range(len(self.nobles)):
            nob=str(self.nobles[i]).split(',')[0]+','+str(self.nobles[i]).split(',')[2]
            self.Noblestn[i+1].SetLabel(nob)

    def DisplayCards(self):
        stn=[]
        stn.append(wx.StaticText(self.panel, label='Cards:', style=wx.ALIGN_LEFT))
        for i in range(len(self.cards)):
            stn.append(wx.StaticText(self.panel, label=str(self.cards[i]), style=wx.ALIGN_LEFT))
        self.Cardsstn=stn
        for i in range(len(stn)):
            self.my_sizer.Add(stn[i], 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        if len(stn)<self.rows:
            for i in range(self.rows-len(stn)):
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        my_btn=[]
        self.btn_ids=[]
        self.reserve_ids=[]
        for i in range(len(stn)):
            if i!=0:
                my_btn.append(wx.Button(self.panel, label='Buy'))
                self.btn_ids.append(my_btn[-1].GetId())
                my_btn[-1].Bind(wx.EVT_BUTTON, self.on_press_buy)
                self.my_sizer.Add(my_btn[-1], 0, wx.ALL | wx.CENTER, 5)
            else:
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        if len(stn)<self.rows:
            for i in range(self.rows-len(stn)):
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        for i in range(len(stn)):
            if i!=0:
                my_btn.append(wx.Button(self.panel, label='Reserve'))
                self.reserve_ids.append(my_btn[-1].GetId())
                my_btn[-1].Bind(wx.EVT_BUTTON, self.on_press_reserve)
                self.my_sizer.Add(my_btn[-1], 0, wx.ALL | wx.CENTER, 5)
            else:
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
        if len(stn)<self.rows:
            for i in range(self.rows-len(stn)):
                self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
    def RefreshCards(self):
        for i in range(len(self.Cardsstn)-1):
            if i+1>len(self.cards):
                self.Cardsstn[i+1].SetLabel('')
            else:
                self.Cardsstn[i+1].SetLabel(str(self.cards[i]))
        
    def DisplayPlayer(self):
        self.Playerstn=[]
        for i in range(len(self.player)):
            S=['Player '+str(i)+':']
            S.extend(str(Game.player[i]).split(','))
            stn=[]
            for i2 in range(len(S)):
                stn.append(wx.StaticText(self.panel, label=str(S[i2]), style=wx.ALIGN_LEFT))
                self.my_sizer.Add(stn[i2], 0, wx.ALL | wx.FIXED_MINSIZE, 5)
            self.Playerstn.append(stn)
            if len(stn)<self.rows:
                for i in range(self.rows-len(stn)):
                    self.my_sizer.Add(self.empty_cell, 0, wx.ALL | wx.FIXED_MINSIZE, 5)
    def RefreshPlayer(self):
        for i in range(len(self.player)):
            S=['Player '+str(i)+':']
            S.extend(str(Game.player[i]).split(','))
            stn=[]
            for i2 in range(len(self.Playerstn[i])):
                if i2==len(self.Playerstn[i])-1:
                    self.Playerstn[i][i2].SetLabel(str(S[i2:]))
                else:
                    self.Playerstn[i][i2].SetLabel(str(S[i2]))

        
        
if __name__ == '__main__':
    if 'app' in locals():
        del app
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()