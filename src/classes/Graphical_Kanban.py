#---------------------------------------------------------------------------
#-- Copyright (c) 2020 Lyaaaaaaaaaaaaaaa
#--
#-- author :
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Changelog:
#--   02/09/2020 Lyaaaaa
#--     - Created the file and implemented it.
#---------------------------------------------------------------------------
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from kanban import Kanban

class Graphical_Kanban():
  """This class will create the GTK widgets for a kanban"""

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
#--  - Create an array of columns to associate each column to its graphicals
#--      widget.
#--  - Do the same for the cards.
#---------------------------------------------------------------------------

  def __init__(self, P_Kanban, P_Gtk_Box):
    self.Kanban  = P_Kanban
    self.Gtk_Box = P_Gtk_Box

    self.Generate_Kanban()

#---------------------------------------------------------------------------
#-- __del__
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

  def __del__(self):
    self.Destroy_Graphical_Elements()


#---------------------------------------------------------------------------
#-- Generate_Kanban
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

  def Generate_Kanban(self):
    Columns = self.Kanban.Get_Columns()

    self.Generate_Columns(Columns)
    self.Gtk_Box.show_all()


#---------------------------------------------------------------------------
#-- Generate_Columns
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Insert into an array the Column_Box for later edits
#---------------------------------------------------------------------------

  def Generate_Columns(self, P_Columns):
    for Column in P_Columns:
      column_title = Column.Get_Title()
      Cards        = Column.Get_Cards()
      Column_Box   = self.Add_Column(column_title)

      self.Generate_Cards(Cards, Column_Box)

#---------------------------------------------------------------------------
#-- Generate_Cards
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Insert into an array the Card_Frame for later edits
#--  - Return the Column_Box ? Or maybe save it as an attribut?
#---------------------------------------------------------------------------

  def Generate_Cards(self, P_Cards, P_Column_Box):
    for Card in P_Cards:
      card_title       = Card.Get_Title()
      card_description = Card.Get_Description()
      Card_Frame       = self.Add_Card(card_title, card_description)

      P_Column_Box.add(Card_Frame)

#---------------------------------------------------------------------------
#-- Add_Column
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Add a counter displaying the number of card
#--  - Set the drag and drop area
#---------------------------------------------------------------------------

  def Add_Column(self, P_Title):
    Column_Box   = Gtk.VBox()
    Column_Label = Gtk.Label(label = P_Title)

    Column_Box.add(Column_Label)
    self.Gtk_Box.add(Column_Box)

    return Column_Box


#---------------------------------------------------------------------------
#-- Add_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Add a button to set a color
#---------------------------------------------------------------------------

  def Add_Card(self, P_Title, P_Description):
    Card_Frame = Gtk.Frame()
    Buffer     = Gtk.TextBuffer()
    Text_View  = Gtk.TextView()
    Label      = Gtk.Label()

    Label.set_markup("<b>" + P_Title + "</b>")

    Buffer.set_text(P_Description)
    Text_View.set_buffer(Buffer)
    Text_View.set_editable(False)
    Text_View.set_cursor_visible(False)

    Card_Frame.add(Text_View)
    Card_Frame.set_label_widget(Label)
    return Card_Frame


#---------------------------------------------------------------------------
#-- Destroy_Graphical_Elements
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Destroy the children of the Gtk_Box. Use it to clear before loading
#--      another Kanban
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Destroy_Graphical_Elements(self):
    Children = self.Gtk_Box.get_children()
    for Child in Children:
      Child.destroy()
