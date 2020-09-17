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
#--
#--   01/08/2020 Lyaaaaa
#--     - Added a Save and File object to the class attributs.
#--     - Implemented Create_Kanban.
#--     - Updated Display_Saves. It no longer directly edits the combo box but
#--         calls Add_Combo_Box_Element which does.
#--     - Created Add_Combo_Box_Element to append element to the combo box.
#--     - Implemented On_Overwrite_Dialog_Yes_Clicked.
#--
#--   02/08/2020 Lyaaaaa
#--     - Removed all related statement to "Rename_Buffer" because it no longer
#--         exist in the interface.
#--     - Replaced the related statement by using "Rename_Dialog_Entry" instead.
#--     - Now import Graphical_Kanban class and create an object of it in
#--         On_Kanban_Combo_Box_Changed.
#--     - Updated On_Kanban_Combo_Box_Changed to create a graphical kanban by
#--         creating an object of the Graphical_Kanban's class.
#--     - Added a Graphical_Kanban attribut to this class (init to None)
#---------------------------------------------------------------------------

from gi.repository import Gtk

from load             import Load
from file             import File
from save             import Save
from kanban           import Kanban
from graphical_kanban import Graphical_Kanban

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
    self.Builder          = P_Builder
    self.Load             = Load()
    self.File             = File()
    self.Save             = Save(self.File)
    self.Kanban           = Kanban()
    self.Graphical_Kanban = None
    self.action_flag      = None


#---------------------------------------------------------------------------
#-- Scan_Saves
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Scan the saves directory.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Display_Saves(self):
    Files_Names = self.Load.Get_Files_Names()

    for File_Name in Files_Names:
      self.Add_Combo_Box_Element(File_Name, File_Name)


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
#--  -
#---------------------------------------------------------------------------

  def Create_Kanban(self, P_New_Name):
    self.Kanban = Kanban(P_New_Name)

    self.File.Set_Name(P_New_Name)
    self.Save.Set_File(self.File)

    if self.Save.Write_Save(self.Kanban) == True:
      self.Add_Combo_Box_Element(P_New_Name, P_New_Name)

    else:
      Dialog            = self.Builder.get_object("Overwrite_Dialog")
      Label             = self.Builder.get_object("Overwrite_Dialog_Label")
      self.action_flag  = "Overwrite_Kanban"

      Label.set_text("A kanban is already named "
                     + P_New_Name
                     + ". Do you want to overwrite it? There is no coming back")
      Dialog.show()


#---------------------------------------------------------------------------
#-- Add_Combo_Box_Element
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
  def Add_Combo_Box_Element(self, P_Element_Text, P_Element_Id):
    Combo_Box   = self.Builder.get_object("Kanban_Combo_Box")
    Combo_Box.append(P_Element_Text, P_Element_Id)




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
#--  - Add other condition to check for future edit (like edit card or column).
#---------------------------------------------------------------------------

  def On_Overwrite_Dialog_Yes_Clicked(self, *args):
    Dialog = self.Builder.get_object("Overwrite_Dialog")

    if self.action_flag == "Overwrite_Kanban":
      self.Save.Write_Save(self.Kanban, True)
      Dialog.hide()



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
    Rename_Entry  = self.Builder.get_object("Rename_Dialog_Entry")
    new_name      = Rename_Entry.get_text()

    if self.action_flag == "Add_Kanban":
      self.Create_Kanban(new_name)

    Rename_Entry.set_text("")
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
    Rename_Entry  = self.Builder.get_object("Rename_Dialog_Entry")

    Rename_Entry.set_text("")
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
    Combo_Box   = self.Builder.get_object("Kanban_Combo_Box")
    Content_Box = self.Builder.get_object("Content_Box")
    active_id   = Combo_Box.get_active_id()

    if active_id != "placeholder":
      del (self.Graphical_Kanban)
      Kanban                = self.Load.Load_Save_File(active_id)
      self.Graphical_Kanban = Graphical_Kanban(Kanban, Content_Box)
