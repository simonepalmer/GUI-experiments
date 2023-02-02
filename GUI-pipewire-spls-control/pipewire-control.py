import gi # to use GTK
import os # to run shell commands

gi.require_version("Gtk", "3.0") 
from gi.repository import Gtk

# BUFFER = 128 (probably don't want it defauled to 0)

# I borrowed this whole part from a tutorial video to get started but 
# I absolutely don't fully understand how it works more than that I 
# open pipewire-control.glade, connect signals from it to functions
# below, call and show the main window and connect the X-button to
# close the program. The "self-references" I don't understand and
# I have just noticed that all the code I have seem has them and 
# it makes it actually work :D If anyone has some way of explaining
# it to me I would be very thankful!
class Control:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("pipewire-control.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)
    
    #def on_apply_clicked(self, clicked)
        #os.system(f'pw-metadata -n settings 0 clock.force-quantum {BUFFER}')

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
        # Example for change:
        # BUFFER = 64
        # return BUFFER

        # Anyone know if there is a reason the commented out
        # method would not work?

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