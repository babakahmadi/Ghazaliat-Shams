# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from bidi.algorithm import get_display
from kivy.uix.listview import ListItemButton
from kivy.factory import Factory
from Beits import extract_beits
from Beits import extract_poem
import arabic_reshaper





beit_index =-1
def pars(str):
    return get_display(arabic_reshaper.reshape(str))

class MyLabel(ListItemButton):
    #def __init__(self,index):
    #    super(MyLabel,self).__init__()
    #    self.index = index   
    def set_index(self):
        global beit_index
        beit_index=self.index
class Persian(BoxLayout):
    def __init__(self):
        super(Persian, self).__init__()
        self.title.text = pars(u'غزلیات \n شمس \n تبریزی')
        self.search.text = pars(u'برو به شعر')
        self.adding.text = pars(u'افزودن')
        self.beit_list.adapter.data = [pars(u'ناموس شعر')]
        beits = extract_beits()
        for i in beits:
            self.beit_list.adapter.data.extend([pars(i)])
        self.beit_list.adapter.cls = MyLabel

    def gonew(self):
        global beit_index
        #print 'beit_index is',beit_index
        self.clear_widgets()
        tmp = Poetry(beit_index)
        self.add_widget(tmp)

class Poetry(BoxLayout):
    def __init__(self,poemNum):
        super(Poetry, self).__init__()
        self.back.text = pars(u'برگشت')
        self.beit_list.adapter.data = []
        poem = extract_poem(poemNum)
        for i in poem:
            self.beit_list.adapter.data.extend([pars(i[0])+'      '+pars(i[1])])
        self.beit_list.adapter.cls = MyLabel
    def goback(self):
        self.clear_widgets()
        tmp = Persian()
        self.add_widget(tmp)

class PersianApp(App):

    def build(self):
        return Persian()


if __name__ == '__main__':
    PersianApp().run()
