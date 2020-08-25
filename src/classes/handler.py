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
#--     - Handler class no longer import Interface (reversed).
#--     - Now import Gtk so it can exit the application.
#--     - Implemented the following methods:
#--       - On_Popover_Menu_About_Clicked
#--       - On_About_Dialog_Close_Button_Clicked
#--       - On_Application_Window_Destroy
#---------------------------------------------------------------------------

from gi.repository import Gtk

class Handler():
  """Link the interface with the backbone and manage the whole application"""

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

  def __init__(self, P_Builder):
    self.Builder   = P_Builder

  #---------------------------------
  #--          Signals            --
  #---------------------------------

#---------------------------------------------------------------------------
#-- On_Application_Window_Destroy
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

  def On_Application_Window_Destroy(self, *args):
    Gtk.main_quit()

#---------------------------------------------------------------------------
#-- On_Application_Window_Add_Kanban_Clicked
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

  def On_Application_Window_Add_Kanban_Clicked(self, *args):
    pass

#---------------------------------------------------------------------------
#-- On_About_Dialog_Close_Button_Clicked
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

  def On_About_Dialog_Close_Button_Clicked(self, *args):
    About_Dialog = self.Builder.get_object("About_Dialog")
    About_Dialog.hide()

#---------------------------------------------------------------------------
#-- On_Edit_Card_Dialog_Save_Clicked
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

  def On_Edit_Card_Dialog_Save_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Edit_Card_Dialog_Cancel_Clicked
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

  def On_Edit_Card_Dialog_Cancel_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Overwrite_Dialog_Yes_Clicked
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

  def On_Overwrite_Dialog_Yes_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Overwrite_Dialog_Cancel_Clicked
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

  def On_Overwrite_Dialog_Cancel_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Delete_Dialog_Cancel_Clicked
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

  def On_Delete_Dialog_Cancel_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Delete_Dialog_Yes_Clicked
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

  def On_Delete_Dialog_Yes_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Rename_Dialog_Save_Clicked
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

  def On_Rename_Dialog_Save_Clicked(self, *args):
    pass


#---------------------------------------------------------------------------
#-- On_Rename_Dialog_Cancel_Clicked
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

  def On_Rename_Dialog_Cancel_Clicked(self, *args):
    pass

#---------------------------------------------------------------------------
#-- On_Popover_Menu_Help_Clicked
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

  def On_Popover_Menu_Help_Clicked(self, *args):
    pass

#---------------------------------------------------------------------------
#-- On_Popover_Menu_Preferences_Clicked
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

  def On_Popover_Menu_Preferences_Clicked(self, *args):
    pass

#---------------------------------------------------------------------------
#-- On_Popover_Menu_About_Clicked
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

  def On_Popover_Menu_About_Clicked(self, *args):
    About_Dialog = self.Builder.get_object("About_Dialog")
    About_Dialog.show()
