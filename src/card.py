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
#--   10/12/2019 Lyaaaaa
#--     - Created file.
#--
#--   03/02/2020 Lyaaaaa
#--     - Edited __init__, Added P_Title parameter with "Card's title" as
#--         default value and P_Description with "Card's description"
#--
#--    19/01/2021 Lyaaaaa
#--      - Removed outdated comments
#--      - Set methods no longer returns a bool.
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

  def __init__(self,
               P_Title = "Card's title",
               P_Description = "Card's description"):
    self.title       = P_Title
    self.description = P_Description


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
#--  -
#---------------------------------------------------------------------------

  def Set_Title(self, P_Title):
    self.title = P_Title

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
#--  -
#---------------------------------------------------------------------------

  def Set_Description(self, P_Description):
    self.description = P_Description


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


