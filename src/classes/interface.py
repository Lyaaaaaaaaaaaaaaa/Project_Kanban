#---------------------------------------------------------------------------
#-- Copyright (c) 2020 Lyaaaaaaaaaaaaaaa
#--
#-- author : Lyaaaaaaaaaaaaaaa
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Changelog:
#--   21/08/2020 Lyaaaaa
#--     - Creation of the file
#--
#--   25/08/2020 Lyaaaaa
#--     - Implementation of the methods
#--     - Create an object of Handler and use it to connect the signals
#--     - Handler class is now imported in Interface (reversed)
#---------------------------------------------------------------------------

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from handler       import Handler

class Interface():
  """Represent the graphical elements"""

#---------------------------------------------------------------------------
#-- __init__
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def __init__(self):
    print ("init")
    self.Builder = Gtk.Builder()
    self.Handler = Handler(self.Builder)

#---------------------------------------------------------------------------
#-- Connect_Interface
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Connect_Interface(self):
    print ("Connect_Interface")
    self.Builder.add_from_file("../interface.ui")

#---------------------------------------------------------------------------
#-- Connect_Signals
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Connect_Signals(self):
    print ("Connect_Signals")
    self.Builder.connect_signals(self.Handler)

#---------------------------------------------------------------------------
#-- Start_Interface
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Be sure to call Connect_Interface and Connect_Signals before this method
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Start_Application(self):
    Application_Window = self.Builder.get_object("Application_Window")
    Application_Window.show_all()
    Gtk.main()

#---------------------------------------------------------------------------
#-- Quit_Application
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - May be deleted, the handler now quit the application by itself
#---------------------------------------------------------------------------

  def Quit_Application(self):
    Gtk.main_quit()

#---------------------------------------------------------------------------
#-- Get_Builder
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - May be deleted, not sure it will be used anymore
#---------------------------------------------------------------------------

  def Get_Builder(self):
    return self.Builder
