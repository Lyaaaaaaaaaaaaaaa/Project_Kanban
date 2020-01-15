#---------------------------------------------------------------------------
#-- Copyright (C) 2019 Lyaaaaaaaaaaaaaaa
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
#--   10/12/2019 Lyaaaaa
#--     - Created file.
#---------------------------------------------------------------------------

class Card():
  """Represent the cards of a kanban"""
  """Basically, each card is a task"""

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
#--  - Possibility to add an end date attribut
#---------------------------------------------------------------------------

  def __init__(self):
    self.title       = "Card's title"
    self.description = "Card's description"


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
#--  - #TODO Add a check (like length check or type check)
#---------------------------------------------------------------------------

  def Set_Title(self, P_Title):
    self.title = P_Title
    return True

#---------------------------------------------------------------------------
#-- Set_Description
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - #TODO Add a check (like length check or type check)
#---------------------------------------------------------------------------

  def Set_Description(self, P_Description):
    self.description = P_Description
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
#-- Get_Description
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

  def Get_Description(self):
    return self.description


