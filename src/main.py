#The elementary OS Combobulator designed to ease the use of elementary by installing commonly needed software and
# system configuration changes designed to make elementary OS a more pleasing experience.

import gi
import subprocess
import os

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def GtkToggleButton():
    pass


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="elC - The elementary Combobulator")
        self.set_default_size(200, 100)
        self.set_border_width(30)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Install Geany")
        button.connect("clicked", self.on_click_install_geary)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Uninstall Geany")
        button.connect("clicked", self.on_click_uninstall_geary)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Close")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_install_geary(self, button):
        subprocess.Popen(['gksudo', 'apt-get -y install geany'])

    def on_click_uninstall_geary(self, button):
        subprocess.Popen(['gksudo', 'apt-get -y remove geany'])

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()