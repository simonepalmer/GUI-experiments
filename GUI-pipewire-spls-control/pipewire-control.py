import gi # to use GTK
import os # to run shell commands

gi.require_version("Gtk", "3.0") 
from gi.repository import Gtk

class Control:
    """Control class for business logic."""
    
    def __init__(self, buffer=64, sample=48000):
        self.buffer = buffer
        self.sample = sample

    def apply_buffer_sample(self):
        try:
            # os.system(f'this_command_does_not_exist {buffer}')
            os.system(f'pw-metadata -n settings 0 clock.force-quantum {self.buffer}')
            os.system(f'pw-metadata -n settings 0 clock.force-rate {self.sample}')
        except Exception as e:
            self.show_error_window("An error occurred while applying the buffer and sample", str(e))

    def show_error_window(self, title, message):
        builder = Gtk.Builder()
        builder.add_from_file("pipewire-control.glade")
        
        window_error = builder.get_object("window_error")
        window_error.set_title("Pipewire error")
        
        label_error = builder.get_object("label_error")
        label_error.set_text("Could not set the selected settings, make sure you have pipewire installed.")
        
        window_error.show_all()

class ControlWindow:
    """ControlWindow class for GUI logic."""

    def __init__(self, control):
        self.control = control
        self.builder = Gtk.Builder()
        self.builder.add_from_file("pipewire-control.glade")
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window.show_all()
        self.window.connect("destroy", Gtk.main_quit)

    """apply & close buttons"""
    def on_close_error_clicked(self, clicked):
        # print("IS SOMETHING FUCKING HAPPENING?")
        window_error.hide()

    def on_close_clicked(self, clicked):
        # print("closing")
        Gtk.main_quit()

    def on_apply_clicked(self, clicked):
        # print("appying")
        self.control.apply_buffer_sample()
    
    """Buffer size radio buttons"""
    def on_radio64_toggled(self, toggled):
        self.control.buffer = 64

    def on_radio128_toggled(self, toggled):
        self.control.buffer = 128

    def on_radio256_toggled(self, toggled):
        self.control.buffer = 256

    def on_radio512_toggled(self, toggled):
        self.control.buffer = 512

    def on_radio1024_toggled(self, toggled):
        self.control.buffer = 1024

    """Samaple rate radio buttons"""
    def on_radio48_toggled(self, toggled):
        self.control.sample = 48000

    def on_radio44_toggled(self, toggled):
        self.control.sample = 44100

if __name__ == "__main__":
    control = Control()
    ControlWindow(control)
    Gtk.main()