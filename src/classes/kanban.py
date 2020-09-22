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
#---------------------------------------------------------------------------

from column import Column

  #-------------------------------------
  #--        class declaration        --
  #-------------------------------------

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
#--  - Make Columns an array of column.
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
#--  - TODO Control P_Columns type. Must be type Column
#---------------------------------------------------------------------------

  def Set_Columns(self, P_Columns): #TODO
    for Column in P_Columns:
      key = Column.Get_Title()
      self.Columns[key] = Column

    return True

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


  #-----------------------------
  #--       Functions         --
  #-----------------------------

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
#--  - Make a call on P_Column after deleting it and return true if it succeeds
#--    deleting it. Make sure P_Column's type is Column
#---------------------------------------------------------------------------

  def Delete_Column(self, P_Column_Key):

    if P_Column_Key in self.Columns:
      del self.Columns[P_Column_Key]

    return True

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
    New_Column = Column(P_Title)
    self.Columns.update({P_Title : New_Column})
    return True


