from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False
    

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        lbl1 = Label(text = "enter your name:", halign = 'right')
        self.in_name = TextInput(multiline = False)
        lbl1 = Label(text = "enter your name:", halign = 'right')
        self.in_name = TextInput(text = '14', multiline = False)
        self.btn.on_prees = self.text
        self.btn = Button(text = "Start", size_hint = (0.3,.2), pos_hint= {'center_x': 0.5})
        line1 = BoxLayout(size_hint = (.8, None), height = "30sp")
        line2 = BoxLayout(size_hint = (.8, None), height = "30sp")
        line1.add_widget(lbl1)
        line2.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)


    def next(self):
        global name,age
        name = int(self.int_result.text)
        age = int(self.in_age.text)
        self.manager.current = "pulse1"



class PuelseScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_instruction)
        line = BoxLayout(size_hint = (.8, None), height="30sp")
        lbl_result = Label(text="Enter result:", haling = "right")
        self.in_result = TextInput(text = ".8", multiline = False)
        self.btn = Button(text = "Next step", size_hint=(
            0.3,.2), pos_hint={"center_x":0.5})
        self.btn.on_press = self.next
        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        outer = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p1
        p1 = int(self.in_result)
        self.manager.current = "relax"


class PuelseScr2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_test3)
        line = BoxLayout(size_hint = (.8, None), height="30sp")
        line2 = BoxLayout(size_hint = (.8, None), height="30sp")
        lbl_result1 = Label(text="Enter result:", haling = "right")
        self.in_result1 = TextInput(text = ".8", multiline = False)



        lbl_result2 = Label(text="Enter result after second:", haling = "right")
        self.in_result2 = TextInput(text = ".8", multiline = False)



        self.btn = Button(text = "Next step", size_hint=(
            0.3,.2), pos_hint={"center_x":0.5})
        self.btn.on_press = self.next
        line.add_widget(lbl_result1)
        line.add_widget(self.in_result1)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        outer = BoxLayout(orientation = "vertical", padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def next(self):
        global p2,p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = "relax"


class RelaxScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text = txt_sits)
        self.btn = Button(text = "Продовжити", size_hint= (.3,.2), pos_hint = {'center_x':.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = "pulse2"

class ResultScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.auter = BoxLayout(orientation = 'vertical', padding =8, spacing= 8)
        self.instr = Label(text = '')
        self.auter.add_widget(self.instr)
        self.add_widget(self.auter)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + "\n" + text(p1,p2,p3, age)
class HeartCheack(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PuelseScr(name="puelse1"))
        sm.add_widget(RelaxScr(name="relax"))
        sm.add_widget(PuelseScr2(name="puelse2"))
        sm.add_widget(ResultScr(name="result"))
        return sm

HeartCheack().run()