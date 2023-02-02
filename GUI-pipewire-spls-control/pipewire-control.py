import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Control:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("pipewire-control.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
    
    #def on_apply_clicked(self, clicked)
        #os.system(f'pw-metadata -n settings 0 clock.force-quantum {input radio button}')

    def on_close_clicked(self, clicked):
        Gtk.main_quit()

    # plan is for radio buttons to change a variable
    # and the apply button to run the command but
    # I am not sure about how to do that yet?

    # Most likely I will assign a global variable like
    # BUFFER and return it from radio buttons and then
    # have apply run: 
    # os.system(f'pw-metadata -n settings 0 clock.force-quantum {BUFFER})
    def on_radio64_toggled(self, toggled):
        os.system('pw-metadata -n settings 0 clock.force-quantum 64')

    def on_radio128_toggled(self, toggled):
        os.system('pw-metadata -n settings 0 clock.force-quantum 128')

    def on_radio256_toggled(self, toggled):
        os.system('pw-metadata -n settings 0 clock.force-quantum 256')

    def on_radio512_toggled(self, toggled):
        os.system('pw-metadata -n settings 0 clock.force-quantum 512')

    def on_radio1024_toggled(self, toggled):
        os.system('pw-metadata -n settings 0 clock.force-quantum 1024')

if __name__ == "__main__":
    Control()
    Gtk.main()