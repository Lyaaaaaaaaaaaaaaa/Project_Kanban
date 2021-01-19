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
#--
#--   27/08/2020 Lyaaaaa
#--     - Removed the debugging print
#--     - The method Start_Application now calls Handler::Scan_Saves()
#--         method.
#--
#--   31/08/2020 Lyaaaaa
#--     - In Start_Application Handler.Scan_Saves becomes Handler.Display_Saves
#--         because the name of the method changed in the Hlandler class.
#--
#--   13/10/2020 Lyaaaaa
#--     - Updated Connect_Interface to update the path to interface.ui as the
#--         source files changed of directory.
#--
#--    15/10/2020 Lyaaaaa
#--     - Updated Start_Application, removed the Handler.Display_Saves() call.
#--     - Updated Connect_Signals to call Handler.Display_Saves() and
#--         Handler.Set_Active_Combo_Box_Element before to connect the signals
#--         to avoid triggering useless loading of a Graphical_Kanban.
#--
#--   18/10/2020 Lyaaaaa
#--     - Updated Start_Application to disable the button to add a column and
#--         edit a kanban if no kanban is selected. This prevent some errors.
#--
#--    19/01/2021 Lyaaaaa
#--      - Updated Start_Interface header.
#--      - Deleted Quit_Application and Get_Builder methods as they are never
#--          used anywhere in the project.
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
    self.Builder.add_from_file("interface.ui")

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
    self.Handler.Display_Saves()
    self.Handler.Set_Active_Combo_Box_Element(0)
    self.Builder.connect_signals(self.Handler)

#---------------------------------------------------------------------------
#-- Start_Interface
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Be sure to call Connect_Interface and Connect_Signals before this method
#--      in this order.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Start_Application(self):
    Application_Window = self.Builder.get_object("Application_Window")
    Add_Column_Button  = self.Builder.get_object("Add_Column_Button")
    Edit_Kanban_Button = self.Builder.get_object(
        "Application_Window_Edit_Kanban_Button")

    Edit_Kanban_Button.set_sensitive(False)
    Add_Column_Button.set_sensitive(False)

    Application_Window.show_all()
    Gtk.main()
