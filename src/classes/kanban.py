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
    self.Columns = []

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
    self.Columns = P_Columns
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

  def Delete_Column(self, P_Column):
    P_Column.Delete_Card()
    del P_Column
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
    self.Columns.append(New_Column)
    return True


