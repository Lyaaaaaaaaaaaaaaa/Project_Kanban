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
#--
#--   18/09/2020 Lyaaaaa
#--     - Added a Temp_Widget_Reference attribut to this class (init to none).
#--         It is used to store a specific widget when a signal can't access it.
#--     - Implemented On_Application_Window_Edit_Kanban_Clicked which is the
#--         signal for the new button on the application header bar to edit the
#--         kanban (for now it's only used to renamed it).
#--     - Implemented On_Edit_Card_Dialog_Save_Clicked when it's used to create
#--         a new card. It only create the graphical card for now.
#--         It still need to edit the kanban object and save the new data.
#--     - Implemented On_Edit_Card_Dialog_Cancel_Clicked.
#--     - Updated On_Rename_Dialog_Save_Clicked to add the case where it is
#--         used to renamed a column.
#--         It still need to edit the kanban object and save the new data.
#--     - Updated On_Kanban_Combo_Box_Changed to call Connect_Column_Buttons
#--         for each Column generated.
#--     - Created and implemented Connect_Column_Buttons.
#--         It connect the two buttons (edit and add) to a clicked signal.
#--     - Created and implemented On_Column_Edit_Clicked signal.
#--     - Created and implemented On_Column_Add_Card_Clicked.
#--
#--   20/09/2020 Lyaaaaa
#--     - Added the following methods:
#--       - Refresh_Interface which simply show all the widgets of the main
#--           window.
#--       - Connect_Card_Buttons (does the same than Connect_Column_Buttons)
#--           but for the card buttons.
#--       - On_Add_Column_Button_Clicked
#--       - On_Card_Edit_Clicked

#--     - Updated On_Kanban_Combo_Box_Changed to updated the name of the kanban
#--         displayed on the new header.
#--     - Fixed On_Edit_Card_Dialog_Save_Clicked, removed
#--         del (Temp_Widget_Reference) which was making an error.
#--     - Updated On_Rename_Dialog_Save_Clicked:
#--       - Added a case where it edits the kanban's title.
#--       - Added a case where it adds a new column.
#--
#--   21/09/2020 Lyaaaaa
#--     - Updated On_Card_Edit_Clicked to set the Edit_Card_Dialog label and
#--         text view set with the actual editing card values.
#--     - Implemented On_Edit_Card_Dialog_Save_Clicked "Edit_Card" case
#--
#--   22/09/2020 Lyaaaaa
#--     - Updated On_Edit_Card_Dialog_Save_Clicked in "Add_Card" case to connect
#--         the edit button of the last created card with the
#--         On_Card_Edit_Clicked signal.
#--
#--   23/09/2020 Lyaaaaa
#--     - Updated On_Rename_Dialog_Save_Clicked:
#--       - In "Rename_Column" case, edit the Column_Label.set_markup to remove
#--           whitespace between <b> and <big> which was creating whitespace
#--           in the label, therefore making errors later when using the label
#--           as a key to retrieve the column object.
#--       - It now saves at the end of this signal.
#--       - Updated the Rename_Column case to correctly edit all the elements
#--           related to the column, the object and the graphical elements.
#--     - Updated On_Edit_Card_Dialog_Save_Clicked to save on each modification
#--         and implemented the "Add_Card" case.
#--     - Updated On_Kanban_Combo_Box_Changed to change the name of the file
#--         when it loads another kanban (to avoid overwriting the wrong one).
#--     - Updated Connect_Column_Buttons to send a column_box to
#--         On_Column_Edit_Clicked instead of a column_label.
#--     - Updated On_Column_Edit_Clicked to use the column_box instead of the
#--         column_label
#--     - Updated On_Edit_Card_Dialog_Save_Clicked and the "Edit_Card" case to
#--         edit the card object and its graphical element.
#--
#--   25/09/2020 Lyaaaaa
#--     - Added Add_Combo_Box_Element method (not implemented yet).
#--     - Updated On_Rename_Dialog_Save_Clicked method and the "Edit_Kanban" case
#--         to rename the save name.
#--     - Replaced the "Rename_Column" action_flag value into "Edit_Column".
#--     - Added the On_Rename_Dialog_Delete_Clicked signal.
#--     - Added the On_Edit_Card_Dialog_Delete_Clicked signal.
#--     - Fixed an error in On_Overwrite_Dialog_Cancel_Clicked, it wasn't closing.
#--     - Implemented On_Delete_Dialog_Yes_Clicked to delete the Card, Column
#--         or Kanban when needed.
#--
#--   04/10/2020 Lyaaaaa
#--     - Updated On_Card_Edit_Clicked, On_Add_Column_Button_Clicked,
#--         On_Column_Add_Card_Clicked, On_Column_Edit_Clicked,
#--         On_Application_Window_Edit_Kanban_Clicked and
#--         On_Application_Window_Add_Kanban_Clicked to show or hide the
#--         delete button of their dialog as they need.
#--     - Updated Add_Combo_Box_Element to make it select the last added element.
#--     - Renamed Clear_Combo_Box into Remove_Combo_Box_Element as its function
#--         changed. It now remove an element (actually only the active one).
#--
#--   05/10/2020 Lyaaaaa
#--    - Edited On_Delete_Dialog_Yes_Clicked and the "delete_kanban" case to
#--        put the code deletings the column in a "try" to avoid any error if
#--        the kanban has no column.
#--    - Updated On_Rename_Dialog_Save_Clicked in "Edit_Kanban" case to remove
#--        the selected combo box element and add a new one with the right name.
#--
#--   10/10/2020 Lyaaaaa
#--    - Updated On_Rename_Dialog_Save_Clicked:
#--      - Renamed the case "Rename_Column" into "Edit_Column" to fix an error
#--      - Updated "Add_Column" case to add a drop destination when creating
#--          a new column.
#--    - Updated On_Kanban_Combo_Box_Changed to set for each list of card of
#--        each column a drag destination.
#--    - Updated Connect_Card_Buttons to define the edit button as a drag source
#--    - Added Set_Drag_Source and Set_Drag_Destination methods.
#--    - Added On_Drag_Date_Get and On_Drag_Drop signals handlers.
#--    - Moved Connect_Column_Buttons and Connect_Card_Buttons methods out of
#--        the signals section of the file.
#--
#--   12/10/2020 Lyaaaaa
#--     - Updated Connect_Card_Buttons to set the newly added button as the
#--         drag source (third element of the cards header).
#--
#--   15/10/2020 Lyaaaaa
#--     - Added Set_Active_Combo_Box_Element method.
#--
#--   18/10/2020 Lyaaaaa
#--     - Updated On_Kanban_Combo_Box_Changed to disable the button to add a
#--         column and edit a kanban if no kanban is selected. It also now hides
#--         the content of the previously selected kanban and removes its title
#--         from the header bar.
#--         This prevent some errors.
#--         Removed Header_Bar.set_title as the kanban is reloaded anyway.
#--     - Updated On_Rename_Dialog_Save_Clicked to overwrite the save before
#--         renaming the save file.
#--     - Implemented On_Popover_Menu_Help_Clicked.
#--     - Added the following signals On_Help_Dialog_Close_Clicked,
#--         On_Help_Dialog_Apply_Clicked, On_Help_Dialog_Cancel_Clicked.
#--
#--   19/10/2020 Lyaaaaa
#--     - Updated On_Edit_Card_Dialog_Save_Clicked and "Edit_Card" case.
#--         Card_Label.set_text is replaced by set_markup to make the title
#--         of the card bold again. (This avoid the card's title lossing it's
#--         bold attribut at each edit).
#--
#--    27/10/2020 Lyaaaaa
#--      - Updated On_Card_Edit_Clicked and On_Column_Add_Card_Clicked to edit
#--          the Edit_Card_Dialog's title before showing the dialog.
#--      - Updated On_Add_Column_Button_Clicked, On_Column_Edit_Clicked
#--          On_Application_Window_Edit_Kanban_Clicked  and
#--          On_Application_Window_Add_Kanban_Clicked to edit the Rename_Dialog's
#--          title before showing the dialog.
#--
#--     19/01/2021 Lyaaaaa
#--       - Updated some functions headers and removed outdated comments.
#---------------------------------------------------------------------------

from gi.repository import Gtk, Gdk, GdkPixbuf

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

    self.action_flag           = None
    self.Temp_Widget_Reference = None

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
    Combo_Box = self.Builder.get_object("Kanban_Combo_Box")

    Combo_Box.append(P_Element_Text, P_Element_Id)
    Combo_Box.set_active_id(P_Element_Id)


#---------------------------------------------------------------------------
#-- Refresh_Interface
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

  def Refresh_Interface(self):
    Interface = self.Builder.get_object("Application_Window")
    Interface.show_all()


#---------------------------------------------------------------------------
#-- Remove_Combo_Box_Element
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Removes an element of the combobox
#--
#-- Anticipated Changes:
#--  - Add more possible arguments to delete other elements than active.
#---------------------------------------------------------------------------

  def Remove_Combo_Box_Element(self, P_Argument):
    Combo_Box = self.Builder.get_object("Kanban_Combo_Box")

    if P_Argument == "active":
      Element = Combo_Box.get_active()
      Combo_Box.set_active(0)
      Combo_Box.remove(Element)


#---------------------------------------------------------------------------
#-- Connect_Column_Buttons
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Create the signal on_clicked and handler for each column's edit button.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Connect_Column_Buttons(self, P_Column_Box):
    Column_Header           = P_Column_Box.get_children()[1]
    Header_Items            = Column_Header.get_children()
    Column_Label            = Header_Items[0]
    Column_Edit_Button      = Header_Items[1]
    Column_Add_Card_Button  = Header_Items[2]

    Column_Edit_Button.connect    ("clicked",
                                   self.On_Column_Edit_Clicked,
                                   P_Column_Box)
    Column_Add_Card_Button.connect("clicked",
                                   self.On_Column_Add_Card_Clicked,
                                   P_Column_Box)


#---------------------------------------------------------------------------
#-- Connect_Card_Buttons
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Create the signal on_clicked and handler for each column's edit button.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------
  def Connect_Card_Buttons(self, P_Card_Box):
    Card_Header      = P_Card_Box.get_children()[0]
    Card_Edit_Button = Card_Header.get_children()[1]
    Card_Drag_Button = Card_Header.get_children()[2]

    Card_Edit_Button.connect("clicked",
                             self.On_Card_Edit_Clicked,
                             P_Card_Box)
    self.Set_Drag_Source(Card_Drag_Button)



#---------------------------------------------------------------------------
#-- Set_Drag_Source
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

  def Set_Drag_Source(self, Widget):
    Widget.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [
    ], Gdk.DragAction.MOVE)
    Widget.connect("drag_data_get", self.On_Drag_Data_Get)
    Widget.drag_source_set_target_list(None)
    Widget.drag_source_add_text_targets()


#---------------------------------------------------------------------------
#-- Set_Drag_Destination
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
  def Set_Drag_Destination(self, Widget):

    Widget.drag_dest_set(Gtk.DestDefaults.ALL, [], Gdk.DragAction.MOVE)
    Widget.connect("drag-drop", self.On_Drag_Drop)
    Widget.drag_dest_set_target_list(None)
    Widget.drag_dest_add_text_targets()



#---------------------------------------------------------------------------
#-- Set_Active_Combo_Box_Element
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - By default if none parameters given it will set the placeholder as active.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------
  def Set_Active_Combo_Box_Element(self, P_Element_Id = 0):
    Combo_Box = self.Builder.get_object("Kanban_Combo_Box")
    Combo_Box.set_active(P_Element_Id)


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
    Dialog        = self.Builder.get_object("Rename_Dialog")
    Delete_Button = self.Builder.get_object("Rename_Dialog_Delete_Button")

    Delete_Button.hide()
    Dialog.set_title("Create your Kanban")
    Dialog.show()
    self.action_flag = "Add_Kanban"


#---------------------------------------------------------------------------
#-- On_Application_Window_Edit_Kanban_Clicked
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

  def On_Application_Window_Edit_Kanban_Clicked(self, *args):
    Dialog        = self.Builder.get_object("Rename_Dialog")
    Entry         = self.Builder.get_object("Rename_Dialog_Entry")
    Delete_Button = self.Builder.get_object("Rename_Dialog_Delete_Button")

    Delete_Button.show()
    Entry.set_text(self.Kanban.Get_Title())
    Dialog.set_title("Edit your Kanban")
    Dialog.show()
    self.action_flag = "Edit_Kanban"

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
    Dialog      = self.Builder.get_object("Edit_Card_Dialog")
    Title_Entry = self.Builder.get_object("Edit_Card_Dialog_Title_Entry")
    Buffer      = self.Builder.get_object ("Edit_Card_Dialog_Description_Buffer")
    start       = Buffer.get_start_iter()
    end         = Buffer.get_end_iter()
    title       = Title_Entry.get_text()
    description = Buffer.get_text(start, end, False)

    Dialog.hide()
    if self.action_flag == "Add_Card":
      Column_Box      = self.Temp_Widget_Reference
      Scrolled_Window = Column_Box.get_children()[0]
      Viewport        = Scrolled_Window.get_child()
      Card_List_Box   = Viewport.get_child()
      Column_Title    = Column_Box.get_name()

      Card_List_Box.add(self.Graphical_Kanban.Add_Card(title, description))
      Card_List_Box.show_all()

      List_Box_Last_Row = Card_List_Box.get_children()[-1]
      Card_Box          = List_Box_Last_Row.get_child()

      self.Connect_Card_Buttons(Card_Box)
      Column = self.Kanban.Get_Column(Column_Title)
      Column.Add_Card(title, description)

    elif self.action_flag == "Edit_Card":
      Card_Box       = self.Temp_Widget_Reference
      Card_Header    = Card_Box.get_children()[0]
      Card_Label     = Card_Header.get_children()[0]
      Card_View_Text = Card_Box.get_children()[1]
      Card_Buffer    = Card_View_Text.get_buffer()
      Old_Card_Title = Card_Box.get_name()

      Card_Label.set_markup("<b>" + title + "</b>")
      Card_Buffer.set_text(description)
      Card_Box.set_name(title)
      self.Kanban.Edit_Card(P_Key             = Old_Card_Title,
                            P_New_Title       = title,
                            P_New_Description = description)

    self.Save.Write_Save(self.Kanban, P_Overwrite = True)
    Buffer.set_text("")
    Title_Entry.set_text("")


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
    Dialog      = self.Builder.get_object("Edit_Card_Dialog")
    Title_Entry = self.Builder.get_object("Edit_Card_Dialog_Title_Entry")
    Buffer      = self.Builder.get_object ("Edit_Card_Dialog_Description_Buffer")

    Buffer.set_text("")
    Title_Entry.set_text("")
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
    Dialog = self.Builder.get_object("Overwrite_Dialog")
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
#--  - Delete_Kanban case:
#--    - Delete the kanban object and its save file then its graphical elements
#--        then set the kanban combo box to the placeholder.
#--  - Delete_Column case:
#--    - Remove the column object then its graphical elements.
#--  - Delete_Card case:
#--    - Same than Delete_Column but with the card.
#--  - The deletion of the columns is in a try because the user could want to
#--      delete a kanban with no column in it.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def On_Delete_Dialog_Yes_Clicked(self, *args):
    Dialog = self.Builder.get_object("Delete_Dialog")

    if   self.action_flag == "Delete_Kanban":
      Kanban_Header = self.Builder.get_object("Kanban_Header_Bar")
      Content_Box   = self.Builder.get_object("Content_Box")

      del (self.Kanban)
      Kanban_Header.set_title("")

      self.File.Delete_File()
      self.Remove_Combo_Box_Element("active")

      try:
        Columns_Grid  = Content_Box.get_children()[0]
        Columns_Grid.destroy()
      except IndexError:
        pass

    elif self.action_flag == "Delete_Column":
      Column_Box  = self.Temp_Widget_Reference
      Column_Name = Column_Box.get_name()

      self.Kanban.Delete_Column(Column_Name)
      Column_Box.destroy()
      self.Save.Write_Save(self.Kanban, P_Overwrite= True)

    elif self.action_flag == "Delete_Card":
      Card_Box  = self.Temp_Widget_Reference
      Card_Name = Card_Box.get_name()

      self.Kanban.Delete_Card(Card_Name)
      Card_Box.destroy()
      self.Save.Write_Save(self.Kanban, P_Overwrite= True)


    Dialog.hide()


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
#--  - Find another way to update the combo box as it reload the already loaded
#--      kanban.
#---------------------------------------------------------------------------

  def On_Rename_Dialog_Save_Clicked(self, *args):

    Dialog       = self.Builder.get_object("Rename_Dialog")
    Rename_Entry = self.Builder.get_object("Rename_Dialog_Entry")
    Header_Bar   = self.Builder.get_object("Kanban_Header_Bar")
    new_name     = Rename_Entry.get_text()

    if   self.action_flag == "Add_Kanban":
      self.Create_Kanban(new_name)

    elif self.action_flag == "Edit_Kanban":
      self.Kanban.Set_Title(new_name)
      self.Save.Write_Save(self.Kanban, P_Overwrite = True)
      self.File.Rename_File(new_name)

      self.Remove_Combo_Box_Element("active")
      self.Add_Combo_Box_Element(new_name, new_name)

    elif self.action_flag == "Edit_Column":
      Column_Box      = self.Temp_Widget_Reference
      Column_Header   = Column_Box.get_children()[1]
      Header_Items    = Column_Header.get_children()
      Column_Label    = Header_Items[0]
      column_old_name = Column_Label.get_text()
      Column          = self.Kanban.Get_Column(column_old_name)

      del self.Temp_Widget_Reference
      Column_Label.set_markup(  "<b><big>"
                              + Rename_Entry.get_text()
                              + "</big></b>")
      self.Kanban.Set_Column_Title(column_old_name, new_name)
      Column_Box.set_name(new_name)

    elif self.action_flag == "Add_Column":
      Column                 = self.Graphical_Kanban.Add_Column(new_name)
      Column_Scrolled_Window = Column.get_children()[0]
      Column_Viewport        = Column_Scrolled_Window.get_children()[0]
      Column_List_Box        = Column_Viewport.get_child()

      self.Kanban.Add_Column(new_name)
      self.Refresh_Interface()
      self.Connect_Column_Buttons(Column)
      self.Set_Drag_Destination(Column_List_Box)

    self.Save.Write_Save(self.Kanban, P_Overwrite = True)
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
    Dialog = self.Builder.get_object("Help_Dialog")

    Dialog.show()

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
    pass #TODO

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
#--  - What happens when you select a kanban.
#--  - It does change the name of the File (used for the save) so the software
#--      doesn't write into another save.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def On_Kanban_Combo_Box_Changed(self, *args):
    Combo_Box   = self.Builder.get_object("Kanban_Combo_Box")
    Content_Box = self.Builder.get_object("Content_Box")
    Header_Bar  = self.Builder.get_object("Kanban_Header_Bar")
    active_id   = Combo_Box.get_active_id()

    Edit_Kanban_Button = self.Builder.get_object("Application_Window_Edit_Kanban_Button")
    Add_Column_Button  = self.Builder.get_object("Add_Column_Button")

    if active_id != "placeholder":
      del (self.Graphical_Kanban)
      self.Kanban           = self.Load.Load_Save_File(active_id)
      self.Graphical_Kanban = Graphical_Kanban(self.Kanban, Content_Box)

      Header_Bar.set_title(self.Kanban.Get_Title())
      self.File.Set_Name(active_id)

      Edit_Kanban_Button.set_sensitive(True)
      Add_Column_Button.set_sensitive(True)


    else:
      Edit_Kanban_Button.set_sensitive(False)
      Add_Column_Button.set_sensitive(False)
      Content_Box.hide()
      Header_Bar.set_title("")


    for Column_Box in Content_Box.get_children():
      self.Connect_Column_Buttons(Column_Box)

      Scrolled_Window = Column_Box.get_children()[0]
      Viewport        = Scrolled_Window.get_child()
      List_Box        = Viewport.get_child()

      for List_Row in List_Box.get_children():
        Card_Box    = List_Row.get_child()
        Card_Header = Card_Box.get_children()[0]
        Edit_Button = Card_Header.get_children()[1]

        self.Connect_Card_Buttons(Card_Box)

      self.Set_Drag_Destination(List_Box)


#---------------------------------------------------------------------------
#-- On_Column_Edit_Clicked
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Display Rename_Dialog
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def On_Column_Edit_Clicked(self, P_Edit_Button, P_Column_Box):
    Dialog        = self.Builder.get_object("Rename_Dialog")
    Rename_Entry  = self.Builder.get_object("Rename_Dialog_Entry")
    Column_Header = P_Column_Box.get_children()[1]
    Header_Items  = Column_Header.get_children()
    Column_Label  = Header_Items[0]
    Delete_Button = self.Builder.get_object("Rename_Dialog_Delete_Button")

    Rename_Entry.set_text(Column_Label.get_text())
    Delete_Button.show()
    Dialog.set_title("Edit your column")
    Dialog.show()

    self.action_flag           = "Edit_Column"
    self.Temp_Widget_Reference = P_Column_Box


#---------------------------------------------------------------------------
#-- On_Column_Add_Card_Clicked
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

  def On_Column_Add_Card_Clicked(self, P_Add_Button, P_Column_Box):
    Dialog        = self.Builder.get_object("Edit_Card_Dialog")
    Delete_Button = self.Builder.get_object("Edit_Card_Dialog_Delete_Button")

    Delete_Button.hide()
    Dialog.set_title("Add your card")
    Dialog.show()
    self.action_flag = "Add_Card"
    self.Temp_Widget_Reference = P_Column_Box


#---------------------------------------------------------------------------
#-- On_Add_Column_Button_Clicked
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Check if a kanban is already created or selected
#---------------------------------------------------------------------------

  def On_Add_Column_Button_Clicked(self, *args):
    Rename_Dialog    = self.Builder.get_object("Rename_Dialog")
    Delete_Button    = self.Builder.get_object("Rename_Dialog_Delete_Button")
    self.action_flag = "Add_Column"

    Delete_Button.hide()
    Rename_Dialog.set_title("Add your column")
    Rename_Dialog.show()


#---------------------------------------------------------------------------
#-- On_Card_Edit_Clicked
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

  def On_Card_Edit_Clicked(self, P_Edit_Button, P_Card_Box):
    Edit_Dialog   = self.Builder.get_object("Edit_Card_Dialog")
    Title_Entry   = self.Builder.get_object("Edit_Card_Dialog_Title_Entry")
    Buffer        = self.Builder.get_object("Edit_Card_Dialog_Description_Buffer")
    Delete_Button = self.Builder.get_object("Edit_Card_Dialog_Delete_Button")

    self.action_flag = "Edit_Card"
    Card_Header      = P_Card_Box.get_children()[0]
    Card_Label       = Card_Header.get_children()[0]
    Card_View_Text   = P_Card_Box.get_children()[1]
    Card_Buffer      = Card_View_Text.get_buffer()
    start            = Card_Buffer.get_start_iter()
    end              = Card_Buffer.get_end_iter()

    Title_Entry.set_text(Card_Label.get_text())
    Buffer.set_text(Card_Buffer.get_text(start, end, False))

    self.Temp_Widget_Reference = P_Card_Box
    Delete_Button.show()
    Edit_Dialog.set_title("Edit your card")
    Edit_Dialog.show()


#---------------------------------------------------------------------------
#-- On_Edit_Card_Dialog_Delete_Clicked
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

  def On_Edit_Card_Dialog_Delete_Clicked(self, *args):
    Delete_Dialog    = self.Builder.get_object("Delete_Dialog")
    Edit_Card_Dialog = self.Builder.get_object("Edit_Card_Dialog")
    self.action_flag = "Delete_Card"

    Delete_Dialog.show()
    Edit_Card_Dialog.hide()

#---------------------------------------------------------------------------
#-- On_Rename_Dialog_Delete_Clicked
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

  def On_Rename_Dialog_Delete_Clicked(self, *args):
    Delete_Dialog = self.Builder.get_object("Delete_Dialog")
    Rename_Dialog = self.Builder.get_object("Rename_Dialog")

    if self.action_flag == "Edit_Column":
      self.action_flag = "Delete_Column"

    elif self.action_flag == "Edit_Kanban":
      self.action_flag = "Delete_Kanban"

    Delete_Dialog.show()
    Rename_Dialog.hide()


#---------------------------------------------------------------------------
#-- On_Drag_Data_Get
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

  def On_Drag_Data_Get(self, P_Widget, P_Drag_Context, P_Data, P_Info, P_Time):

    Card_Header      = P_Widget.get_parent()
    Card_Box         = Card_Header.get_parent()
    card_title       = Card_Box.get_name()
    card_buffer      = Card_Box.get_children()[1].get_buffer()
    start            = card_buffer.get_start_iter()
    end              = card_buffer.get_end_iter()
    card_description = card_buffer.get_text(start, end, False)
    Card_Row         = Card_Box.get_parent()
    Card_List_Box    = Card_Box.get_ancestor(Gtk.ListBox)

    self.Dragged_Card                = dict()
    self.Dragged_Card["title"]       = card_title
    self.Dragged_Card["description"] = card_description
    self.Dragged_Card["list_box"]    = Card_List_Box
    self.Dragged_Card["card_row"]    = Card_Row


#---------------------------------------------------------------------------
#-- On_Drag_Drop
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - It is wiser to call Kanban.Delete_Card before Kanban.Add_Card
#--      because it deletes by searching for the title and having twice the same
#--      title would have an unpredicted behavior (I didn't implemented any
#--      control for this. 10/10/2020)
#--  - It deletes the former card then It creates a new card in the desired
#--      column before to connect its elements to the signals, then it saves.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def On_Drag_Drop(self, P_Widget, P_Drag_Context, P_Data, P_Info, P_Time):

    List_Box     = P_Widget

    if List_Box != self.Dragged_Card["list_box"]:
      Card_Row     = self.Dragged_Card["card_row"]
      title        = self.Dragged_Card["title"]
      description  = self.Dragged_Card["description"]
      column_title = List_Box.get_ancestor(Gtk.Grid).get_name()

      Card_Box = (self.Graphical_Kanban.Add_Card(title, description))
      List_Box.add(Card_Box)
      Card_Row.destroy()
      List_Box.show_all()

      Card_Header  = Card_Box.get_children()[0]
      Edit_Button  = Card_Header.get_children()[1]

      self.Kanban.Delete_Card(title)
      self.Kanban.Add_Card(column_title, title, description)

      self.Connect_Card_Buttons(Card_Box)
      self.Set_Drag_Source(Edit_Button)

      self.Save.Write_Save(self.Kanban, P_Overwrite = True)

#---------------------------------------------------------------------------
#-- On_Help_Dialog_Cancel_Clicked
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

  def On_Help_Dialog_Cancel_Clicked(self, *args):
    Dialog = self.Builder.get_object("Help_Dialog")

    Dialog.hide()


#---------------------------------------------------------------------------
#-- On_Help_Dialog_Apply_Clicked
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

  def On_Help_Dialog_Apply_Clicked(self, *args):
    Dialog = self.Builder.get_object("Help_Dialog")

    Dialog.hide()


#---------------------------------------------------------------------------
#-- On_Help_Dialog_Close_Clicked
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

  def On_Help_Dialog_Close_Clicked(self, *args):
    pass

