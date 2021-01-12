#---------------------------------------------------------------------------
#-- Copyright (c) 2020 Lyaaaaaaaaaaaaaaa
#--
#-- author : Lyaaaaa
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Changelog:
#--   17/09/2020 Lyaaaaa
#--     - Cleaned the main.py (from auto generated code)
#--
#--   13/10/2020 Lyaaaaa
#--     - Implemented the main.
#--
#--    30/10/2020 Lyaaaaa
#--      - Added Application class and main function for the flatpak application.
#--          This allow the application to successfully close.
#---------------------------------------------------------------------------

import gi
import sys

gi.require_version('Gtk', '3.0')

from .interface import Interface
from gi.repository import Gtk, Gio


Interface = Interface()

Interface.Connect_Interface()
Interface.Connect_Signals()
Interface.Start_Application()


class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='io.github.Project_Kanban',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)



def main(version):
    app = Application()
    return app.run(sys.argv)
