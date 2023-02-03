import gi
import os

gi.require_version("Gtk", "3.0") 
from gi.repository import Gtk

class Control:
    """Control class for business logic."""
    
    def __init__(self, buffer=64, sample=48000):
        self.buffer = buffer
        self.sample = sample

    """Checking if Pipewire is installed and apply settings"""
    def apply_settings(self):
        # Check if pipewire is installed and show error if not.
        if os.popen('which pipewire').read() == '/usr/bin/pipewire\n':
            # then try to catch other errors if it is but not working
            try:
                os.system(f'pw-metadata -n settings 0 clock.force-quantum {self.buffer}')
                os.system(f'pw-metadata -n settings 0 clock.force-rate {self.sample}')
            except Exception as error:
                message = "Pipewire is installed but can't set seleceted settings"
                self.show_error_window(message, str(error))
        else:
            message = "Pipewire can't be found, use the command: 'which pipewire' to see if it is installed"
            self.show_error_window(message, "If not, install Pipewire and try again")

    """Showing error popup"""
    def show_error_window(self, message, error):
        builder = Gtk.Builder()
        builder.add_from_file("pipewire-control.glade")
        window_error = builder.get_object("window_error")

        label_error = builder.get_object("label_error")
        label_error.set_text(message)
        label_hint = builder.get_object("label_hint")
        label_hint.set_text(error)

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
    def on_close_clicked(self, clicked):
        # print("closing")
        Gtk.main_quit()

    def on_apply_clicked(self, clicked):
        # print("appying")
        self.control.apply_settings()
    
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