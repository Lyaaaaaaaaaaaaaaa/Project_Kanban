#---------------------------------------------------------------------------
#-- Copyright (c) 2020 Lyaaaaaaaaaaaaaaa
#--
#-- Auteur : Lyaaaaaaaaaaaaaaa
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Changelog:
#--   30/12/2019 Lyaaaaa
#--     - Created file.
#--
#--   14/01/2020 Lyaaaaa
#--     - Implemented Set_Columns.
#--
#--   15/01/2020 Lyaaaaa
#--     - Made Columns attribut into a list.
#--     - Added Add_Column method.
#--
#--   03/02/2020 Lyaaaaa
#--     - Edited __init__, Added P_Title parameter with "Project's name" as
#--         default value
#--     - Edited Add_Column to pass a parameter to directly set its name.
#--
#--   22/09/2020 Lyaaaaa
#--     - Replaced the Columns list by a dictionnary. Each column use its title
#--         as a key.
#--     - Updated Set_Columns, Add_Column and Delete_Column to now use the
#--         dictionnary.
#--     - Added the Get_Column method used to return a single column if you
#--         give it a valid column key (title).
#--
#--   23/09/2020 Lyaaaaa
#--     - Added Set_Column_Title.
#--     - Updated the "for" in Set_Columns to use .values to move through the
#--         values of the dictionnary.
#--     - Added Edit_Card to find a card in the columns by its key then edit it.
#--
#--   25/09/2020 Lyaaaaa
#--     - Added Delete_Card method. It looks for a card by its key in the
#--         columns then delete it if it exists.
#--
#--   10/10/2020 Lyaaaaa
#--     - Added Add_Card method to directly add a card from the Kanban class.
#--
#--    15/10/2020 Lyaaaaa
#--     - Added Get_Columns_By_Id to return the columns ordered by their id
#--         (Ascending).
#--     - Updated the Add_Column method to give an id to the newly created
#--         column.
#--
#--    19/01/2021 Lyaaaaa
#--      - Set_Columns, Add_Column and delete_Column no longer return bool.
#--      - Deleted outdated comments.
#---------------------------------------------------------------------------

from column import Column


class Kanban():
  """Represent the kanban board"""
  """Each kanban can have many column"""

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

  def __init__(self, P_Title = "Project's name"):
    self.title   = P_Title
    self.Columns = {}

  #---------------------------------
  #--       Functions Set         --
  #---------------------------------

#---------------------------------------------------------------------------
#-- Set_Title
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Control type and length of the title
#---------------------------------------------------------------------------

  def Set_Title(self, P_Title):
    self.title = P_Title
    return True

#---------------------------------------------------------------------------
#-- Set_Columns
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

  def Set_Columns(self, P_Columns):
    for Column in P_Columns.values():
      key = Column.Get_Title()
      self.Columns[key] = Column

  #---------------------------------
  #--       Functions Get         --
  #---------------------------------

#---------------------------------------------------------------------------
#-- Get_Title
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

  def Get_Title(self):
    return self.title

#---------------------------------------------------------------------------
#-- Get_Columns
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

  def Get_Columns(self):
    return self.Columns


#---------------------------------------------------------------------------
#-- Get_Column
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Get one column by its key
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Get_Column(self, P_Key):
    return self.Columns[P_Key]



#---------------------------------------------------------------------------
#-- Get_Columns_By_Id
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Returns the columns ordered by ids
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Get_Columns_By_Id(self):
    Columns = []
    for Column in self.Columns.values():
      Columns.append(Column)

    length  = len (Columns)
    for i in range(length -1):
      for y in range(0, length - i - 1):

        if Columns[y].Get_Id() > Columns[y + 1].Get_Id():
          Columns[y], Columns[y+1] = Columns[y + 1], Columns[y]

    return Columns

  #-----------------------------
  #--       Functions         --
  #-----------------------------

#---------------------------------------------------------------------------
#-- Delete_Column
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Make a call on P_Column after deleting it and return true if it succeeds
#--    deleting it. Make sure P_Column's type is Column
#---------------------------------------------------------------------------

  def Delete_Column(self, P_Column_Key):

    if P_Column_Key in self.Columns:
      del self.Columns[P_Column_Key]


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
#--  - TODO Control the creation of the column
#---------------------------------------------------------------------------

  def Add_Column(self, P_Title = "Column's title"):
    columns_number = len(self.Columns)
    New_Column     = Column(P_Title, columns_number)
    self.Columns.update({P_Title : New_Column})

#---------------------------------------------------------------------------
#-- Set_Column_Title
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Update a column and update the dictionnary of column at the same time.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Set_Column_Title(self, P_Key, P_New_Title):
    if P_Key in self.Columns:
      Column = self.Columns[P_Key]

      Column.Set_Title(P_New_Title)
      self.Columns.update({P_New_Title : Column})
      del self.Columns[P_Key]

      return True

    else:
      return False


#---------------------------------------------------------------------------
#-- Edit_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Update a card and update the dictionnary of card at the same time.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Edit_Card(self, P_Key, P_New_Title , P_New_Description):
    for Column in self.Columns.values():
      if (Column.Edit_Card(P_Key,
                           P_New_Title,
                           P_New_Description)
                           == True):
        return True

    return False
    
#---------------------------------------------------------------------------
#-- Delete_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Look for a card in the columns then delete it.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Delete_Card(self, P_Key):
    for Column in self.Columns.values():
      if P_Key in Column.Get_Cards():
        Column.Delete_Card(P_Key)
        return True
    return False


#---------------------------------------------------------------------------
#-- Add_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Add a card in a column by calling Column::Add_Card method
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Add_Card(self, P_Column_Key, P_Title , P_Description):
    self.Columns[P_Column_Key].Add_Card(P_Title, P_Description)

