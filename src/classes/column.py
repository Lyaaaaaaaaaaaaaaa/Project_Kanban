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
#--   13/12/2019 Lyaaaaa
#--     - Created file.
#--
#--   14/01/2020 Lyaaaaa
#--     - Implemented Set_Cards.
#--
#--   15/01/2020 Lyaaaaa
#--     - Added Add_Card method.
#--     - Implemented Update_Cards_Number method.
#--     - Made Cards attribut a list
#--
#--   03/02/2020 Lyaaaaa
#--     - Edited __init__, Added P_Title parameter with "Column's title" as
#--         default value
#--     - Edited Add_Card to add parameters to pass title and description
#--
#--   04/02/2020 Lyaaaaa
#--     - Edited Delete_Card, it now receives a title instead of a card and
#--         check if within its Cards the title match with one, if it does, it
#--         deletes the matching card.
#---------------------------------------------------------------------------

from card import Card

  #-------------------------------------
  #--        class declaration        --
  #-------------------------------------

class Column():
  """Represent the column of a kanban"""
  """Each column can have many cards"""

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
#--  - Make Cards an array of cards.
#---------------------------------------------------------------------------

  def __init__(self, P_Title = "Column's title"):
    self.title        = P_Title
    self.cards_number = 0
    self.Cards        = []


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
#--  - #TODO Control type and length of the title
#---------------------------------------------------------------------------

  def Set_Title(self, P_Title):
    self.title = P_Title
    return True

#---------------------------------------------------------------------------
#-- Set_Cards
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - TODO Control P_Cards type. Must be type Card
#---------------------------------------------------------------------------

  def Set_Cards(self, P_Cards):
    self.Cards = P_Cards
    self.Update_Cards_Number()
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
#-- Get_Cards
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

  def Get_Cards(self):
    return self.Cards

#---------------------------------------------------------------------------
#-- Get_Cards_Number
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

  def Get_Cards_Number(self):
    return self.cards_number


  #-----------------------------
  #--       Functions         --
  #-----------------------------

#---------------------------------------------------------------------------
#-- Update_Cards_Number
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

  def Update_Cards_Number(self):
    self.cards_number = len (self.Cards)


#---------------------------------------------------------------------------
#-- Delete_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - #TODO Make a call on P_Card after deleting it and return if it succeeds
#      deleting it. Make sure P_Card's type id Card
#---------------------------------------------------------------------------

  def Delete_Card(self, P_Title):
    i = 0

    for Card in self.Cards:
      if (Card.Get_Title() == P_Title):
        del self.Cards[i]
      i = i + 1


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
#--  - TODO Control the creation of the Card
#---------------------------------------------------------------------------

  def Add_Card(self,
               P_Title = "Card's title",
               P_Description = "Card's description"):

    New_Card = Card(P_Title, P_Description)

    self.Cards.append(New_Card)
    self.Update_Cards_Number()

    return True
