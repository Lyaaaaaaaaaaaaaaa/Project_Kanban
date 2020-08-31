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
#--
#--   27/08/2020 Lyaaaaa
#--     - In On_About_Dialog_Close_Button_Clicked renamed the local variable
#--         "About_Dialog" into "Dialog".
#--     - Implemented the *_Dialog_Cancel_Clicked methods.
#--     - Added todo in the empty methods.
#--     - Added the On_Kanban_Combo_Box_Changed method.
#--     - Added the Scan_Saves method.
#--     - Added the On_Kanban_Combo_Box_Changed method.
#--     - Implemented On_Rename_Dialog_Save_Clicked.
#--     - Added three new variables (attributs) to the class.
#--       - Load, an instance of the Load class,
#--       - Kanban, an instance of the Kanban class,
#--       - action_flag, a flag used to tell the signals what to do.
#--     - Added the Create_Kanban method
#--
#--   31/08/2020 Lyaaaaa
#--     - Scan_Saves becomes Display_Saves because it no longer call Scan_Saves
#--         anymore. Scan_Saves is called on the init of the Load class.
#---------------------------------------------------------------------------

from gi.repository import Gtk

from load   import Load
from kanban import Kanban

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
    self.Builder     = P_Builder
    self.Load        = Load()
    self.Kanban      = Kanban()
    self.action_flag = None


#---------------------------------------------------------------------------
#-- Scan_Saves
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Scan the saves directory and edit the Kanban_Combo_Box's choices
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Display_Saves(self):
    Combo_Box   = self.Builder.get_object("Kanban_Combo_Box")
    Files_Names = self.Load.Get_Files_Names()

    for File_Name in Files_Names:
      Combo_Box.append(File_Name, File_Name)


#---------------------------------------------------------------------------
#-- Create_Kanban
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Call Save::Write_Save and Handler::Scan_Saves()
#---------------------------------------------------------------------------

  def Create_Kanban(self, P_New_Name):
    self.Kanban = Kanban(P_New_Name)

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
    Dialog = self.Builder.get_object("Rename_Dialog")
    Rename_Buffer = self.Builder.get_object("Rename_Buffer")

    Rename_Buffer.set_text(self.Kanban.Get_Title())
    Dialog.show()
    self.action_flag = "Add_Kanban"

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
    Dialog = self.Builder.get_object("About_Dialog")
    Dialog.hide()

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
    pass#TODO


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
    Dialog = self.Builder.get_object("Edit_Card_Dialog")
    Dialog.hide()


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
    pass#TODO


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
    Dialog = self.Builder.get_object("Overwrite_Dialog_Cancel")
    Dialog.hide()


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
    Dialog = self.Builder.get_object("Delete_Dialog")
    Dialog.hide()


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
    pass#TODO


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
#--  - Call the futur method which will generate the graphical elements of the
#--      kanban
#---------------------------------------------------------------------------

  def On_Rename_Dialog_Save_Clicked(self, *args):

    Dialog        = self.Builder.get_object("Rename_Dialog")
    Rename_Buffer = self.Builder.get_object("Rename_Buffer")

    start = Rename_Buffer.get_start_iter()
    end   = Rename_Buffer.get_end_iter()

    new_name = Rename_Buffer.get_text(start, end, False)

    if self.action_flag == "Add_Kanban":
      self.Create_Kanban(new_name)

    Rename_Buffer.set_text("")
    Dialog.hide()

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
    Dialog        = self.Builder.get_object("Rename_Dialog")
    Rename_Buffer = self.Builder.get_object("Rename_Buffer")

    Rename_Buffer.set_text("")
    Dialog.hide()

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
    pass#TODO

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
    pass#TODO

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


#---------------------------------------------------------------------------
#-- On_Kanban_Combo_Box_Changed
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

  def On_Kanban_Combo_Box_Changed(self, *args):
    Combo_Box = self.Builder.get_object("Kanban_Combo_Box")
    active_id = Combo_Box.get_active_id()

    if active_id != "placeholder":
      Kanban = self.Load.Load_Save_File(active_id)
      #TODO Generate the graphicals elements of the kanban
