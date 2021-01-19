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
#--
#--   03/09/2020 Lyaaaaa
#--     - Updated Add_Card. The card description now has a wrap mode set to
#--         word
#--     - Updated Add_Column. The column box now contain a grid with a header
#--         (Gtk.Hbox) to display the column name and buttons and a
#--         Gtk.ScrolledWindow the display the cards.
#--
#--   18/09/2020 Lyaaaaa
#--     - Updated Add_Column.
#--       - It now has a button to add a new card in it.
#--
#--   20/09/2020 Lyaaaaa
#--     - Updated Add_Column:
#--       - to return the column grid instead of the card box
#--       - Replaced the card box by a list box
#--       - Set the column grid's name to the column name.
#--
#--     - Updated Generate_Columns as a consequence of Add_Column's changes
#--     - Updated Add_Card:
#--       - The frame is replaced by a box
#--       - The card has now a header with the card's title and an edit button
#--     - Updated Generate_Card as a consequence of all the previously described
#--         changes.
#--
#--   22/09/2020 Lyaaaaa
#--     - Updated Generate_Columns to adapt the "for" to the dictionnary.
#--     - Updated Add_Card to set the name of the Card_Box widget to the
#--         card's title.
#--
#--   23/09/2020 Lyaaaaa
#--     - Updated Generate_Cards to adapt he "for" to the cards dictionnary.
#--     - Updated Add_Column to edit the Column_Label.set_markup to remove
#--         whitespace between <b> and <big> which was creating whitespace
#--         in the label, therefore making errors later when using the label
#--         as a key to retrieve the column object.
#--
#--   12/10/2020 Lyaaaaa
#--     - Updated Add_Card to add a third element to the cards header.
#--         This new button is used for dragging the card. And added a margin
#--         between the label and the buttons.
#--
#--   13/10/2020 Lyaaaaa
#--     - Updated Add_Card to edit Drag_Image's image. It now use a custom icon.
#--     - Updated Add_Column to give a shadow to each column.
#--     - Updated Add_Card to add a bottom margin.
#--
#--    15/10/2020 Lyaaaaa
#--     - Updated Generate_Kanban to use the new Get_Columns_By_Id method to
#--         get the columns ordered by id. It solve the problem of the columns
#--         reordering themselves by alphabetical order.
#--     - Updated Generate_Columns to adapt to this change, the Columns given in
#--         parameters are now stored in a list instead of a dict.
#--
#--   17/10/2020 Lyaaaaa
#--     - Updated Add_Column and Add_Card to add tooltips to their buttons.
#--
#--   26/10/2020 Lyaaaaa
#--     - Updated Add_Card to edit the card's style.
#--       - Set a line wrap to the card's title
#--       - Set a size request of 200 to the card's title
#--       - Set a xalign so all the titles are aligned
#--       - Doubled the bottom margin of the cards.
#--
#--    19/01/2021 Lyaaaaa
#--      - Removed outdated comments
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
#--  -
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
    Columns = self.Kanban.Get_Columns_By_Id()

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
#--  -
#---------------------------------------------------------------------------

  def Generate_Columns(self, P_Columns):
    for Column in P_Columns:
      column_title    = Column.Get_Title()
      Cards           = Column.Get_Cards()
      Column_Box      = self.Add_Column(column_title)
      Scrolled_Window = Column_Box.get_children()[0]
      Viewport        = Scrolled_Window.get_child()
      List_Box        = Viewport.get_child()

      self.Generate_Cards(Cards, List_Box)

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
#--  -
#---------------------------------------------------------------------------

  def Generate_Cards(self, P_Cards, P_List_Box):
    for Card in P_Cards.values():
      card_title       = Card.Get_Title()
      card_description = Card.Get_Description()
      Card_Box         = self.Add_Card(card_title, card_description)

      P_List_Box.prepend(Card_Box)

#---------------------------------------------------------------------------
#-- Add_Column
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Generate the graphical elements of a column.
#--      - it's composed of a grid with a header on top with buttons and a title
#--      - then a scrolled window to display the cards.
#--
#-- Anticipated Changes:
#--  - Add a counter displaying the number of card
#---------------------------------------------------------------------------

  def Add_Column(self, P_Title):

    Column_Grid     = Gtk.Grid()
    Column_Header   = Gtk.HBox()
    Column_Label    = Gtk.Label()
    Scrolled_Window = Gtk.ScrolledWindow()
    Viewport        = Gtk.Viewport()
    List_Box        = Gtk.ListBox()
    Edit_Image      = Gtk.Image()
    Edit_Button     = Gtk.Button()
    Add_Button      = Gtk.Button()
    Add_Image       = Gtk.Image()


    Edit_Image.set_from_icon_name("gtk-edit", 1)
    Edit_Button.set_image(Edit_Image)
    Edit_Button.set_relief(Gtk.ReliefStyle.NONE)

    Add_Image.set_from_icon_name("list-add", 1)
    Add_Button.set_image(Add_Image)
    Add_Button.set_relief(Gtk.ReliefStyle.NONE)

    List_Box.set_vexpand(True)
    Viewport.add(List_Box)

    Scrolled_Window.add(Viewport)
    Scrolled_Window.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
    Scrolled_Window.set_shadow_type(Gtk.ShadowType.ETCHED_OUT)

    Column_Label.set_markup("<b><big>"+ P_Title + "</big></b>")
    Column_Header.add(Column_Label)
    Column_Header.add(Edit_Button)
    Column_Header.add(Add_Button)

    Column_Grid.set_name(P_Title)
    Column_Grid.set_column_homogeneous(True)
    Column_Grid.attach(Column_Header, 0, 0, 1, 1)
    Column_Grid.attach_next_to (Scrolled_Window,
                                Column_Header,
                                Gtk.PositionType.BOTTOM,
                                1,
                                1)


    self.Gtk_Box.add(Column_Grid)

    return Column_Grid


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
    Card_Box      = Gtk.VBox()
    Card_Header   = Gtk.HBox()
    Buffer        = Gtk.TextBuffer()
    Text_View     = Gtk.TextView()
    Label         = Gtk.Label()
    Edit_Image    = Gtk.Image()
    Edit_Button   = Gtk.Button()
    Drag_Image    = Gtk.Image()
    Drag_Button   = Gtk.Button()

    Edit_Image.set_from_icon_name("gtk-edit", 1)
    Edit_Button.set_image(Edit_Image)
    Edit_Button.set_relief(Gtk.ReliefStyle.NONE)
    Edit_Button.set_tooltip_markup("Click to edit this card.")

    Drag_Image.set_from_file("ui_ressources/grab24.png")
    Drag_Button.set_image(Drag_Image)
    Drag_Button.set_relief(Gtk.ReliefStyle.NONE)
    Drag_Button.set_tooltip_markup(  "Hold the left click to drag this card "
                                   + "into another column.")

    Label.set_markup("<b>" + P_Title + "</b>")
    Label.set_margin_right(10)
    Label.set_line_wrap(True)
    Label.set_size_request(200, -1)
    Label.set_xalign(0)

    Buffer.set_text(P_Description)
    Text_View.set_buffer(Buffer)
    Text_View.set_editable(False)
    Text_View.set_cursor_visible(False)
    Text_View.set_wrap_mode(Gtk.WrapMode.WORD)

    Card_Header.add(Label)
    Card_Header.add(Edit_Button)
    Card_Header.add(Drag_Button)

    Card_Box.set_name(P_Title)
    Card_Box.add(Card_Header)
    Card_Box.add(Text_View)
    Card_Box.set_margin_bottom(10)


    return Card_Box


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
