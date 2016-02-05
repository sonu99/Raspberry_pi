from Tkinter import *
import RPi.GPIO as GPIO
import os,signal
from time import sleep
import tkMessageBox

class my_Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_windows()
        pin_config()
    #-------------------------------------------------------------------------------
    def init_windows(self):
        self.master.title("sonu")
        self.pack(fill=BOTH,expand=1)
        """clickButton = Button(self, text = "click", command=self.work)
        clickButton.place(x=0, y=0)"""
        menu = Menu(self.master)
        self.master.config(menu=menu)
        #-----------------------Buzzer----------------------------------
        buzzer = Menu(menu)
        buzzer.add_command(label='ON',command=self.buzzer_on)
        buzzer.add_command(label='Off',command=self.buzzer_off)
        menu.add_cascade(label='Buzzer',menu=buzzer)
        #-----------------------Led------------------------------------
        led = Menu(menu)
        led.add_command(label='ON',command=self.led_on)
        led.add_command(label='Off',command=self.led_off)
        menu.add_cascade(label='Led',menu=led)
        #-----------------------Moter----------------------------------
        mot = Menu(menu)
        mot.add_command(label='ON',command=self.mot_on)
        mot.add_command(label='Off',command=self.mot_off)
        menu.add_cascade(label='Moter',menu=mot)
    #---------------------------------------------------------------------------
    def led_on(self):
        tkMessageBox.showinfo( "LED_ON", "Led is on for turn off press off button")
        GPIO.output(led,True)
    #---------------------------------------------------------------------------
    def led_off(self):
        tkMessageBox.showinfo( "LED_Off", "Led is off")
        GPIO.output(led,False)
        
    #---------------------------------------------------------------------------
    def buzzer_on(self):
        tkMessageBox.showinfo( "BUZZER_ON", "Buzzer is on for turn off press off button")
        GPIO.output(buz,True)
    #---------------------------------------------------------------------------
    def buzzer_off(self):
        tkMessageBox.showinfo( "BUZZER_Off", "buzzer is off")
        GPIO.output(buz,False)
    #---------------------------------------------------------------------------
    def mot_on(self):
        tkMessageBox.showinfo( "MOTER_ON", "moter is on for turn off press off button")
        GPIO.output(mot,True)
    #---------------------------------------------------------------------------
    def mot_off(self):
        tkMessageBox.showinfo( "MOTER_Off", "moter is off")
        GPIO.output(mot,False)
    def pin_config():
        print "Pin configuration is set:mot GPIO->16\nbuz->20\nled->21"
        GPIO.setmode(GPIO.BCM)
        buz=20
        led=21
        mot=16
        GPIO.setup(buz,GPIO.OUT)
        GPIO.setup(led,GPIO.OUT)
        GPIO.setup(mot,GPIO.OUT)
        
#----------------------------------------------Main--------------------------------------------------------------------------
root_sonu = Tk()
root_sonu.geometry("400x300")
app = my_Window(root_sonu)
root_sonu.mainloop()
#---------------------------------------------The End------------------------------------------------------------------------
