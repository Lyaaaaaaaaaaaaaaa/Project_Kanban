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
#--
#--   22/09/2020 Lyaaaaa
#--     - Replaced the Cards list by a dictionnary. Each card use its title as
#--         a key.
#--     - Updated Set_Cards, Delete_Card, Add_Card to now use the dictionnary.
#--     - Added the Get_Card method used to return a single card if you give
#--         it a valid key (title)
#--
#--   23/09/2020 Lyaaaaa
#--     - Added Edit_Card to find a card in the Cards dictionnary then edit it.
#--
#--   12/10/2020 Lyaaaaa
#--     - Updated Delete_Card to call Update_Cards_Number after deleting a card.
#--
#--    15/10/2020 Lyaaaaa
#--     - Added an id attribute to the columns. Init at 0 by default.
#--     - Added a method to return the id and another one to change it.
#--         the Set_Id method isn't used for now.
#--
#--   17/10/2020 Lyaaaaa
#--     - Updated Edit_Card to add a condition. It will now verify if the
#--         title of the card changed (because the title is used as key) and it
#--         won't delete anymore the key if the title isn't changed (Fixes the
#--         error making cards disappear if you don't edit the title while
#--         editing a card).
#--
#--    19/01/2021 Lyaaaaa
#--      - Set methods no longer return a bool.
#--      - Removed outdated comments.
#--      - Add_Card no longer returns a bool.
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

  def __init__(self, P_Title = "Column's title", P_Id = 0):
    self.title        = P_Title
    self.id           = P_Id
    self.cards_number = 0
    self.Cards        = {}


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
#-- Set_Cards
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

  def Set_Cards(self, P_Cards):
    for Card in P_Cards:
      key = Card.Get_Title()
      self.Cards[key] = Card

    self.Update_Cards_Number()


#---------------------------------------------------------------------------
#-- Set_Id
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

  def Set_Id(self, P_Id):
    self.id = P_Id


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
#-- Get_Id
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

  def Get_Id(self):
    return self.id


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


#---------------------------------------------------------------------------
#-- Get_Card
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Get one card by its key
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Get_Card(self, P_Key):
    return self.Cards[P_Key]


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

  def Delete_Card(self, P_Key):

    if P_Key  in self.Cards:
      del self.Cards[P_Key]
      self.Update_Cards_Number()


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
#--  - TODO Control the creation of the Card.
#--    - Be sure no card is already named like this one.
#---------------------------------------------------------------------------

  def Add_Card(self,
               P_Title = "Card's title",
               P_Description = "Card's description"):

    New_Card = Card(P_Title, P_Description)

    self.Cards.update({P_Title : New_Card})
    self.Update_Cards_Number()

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

  def Edit_Card(self, P_Key, P_New_Title, P_New_Description):
    if P_Key in self.Cards:
      Card = self.Cards[P_Key]

      Card.Set_Title(P_New_Title)
      Card.Set_Description(P_New_Description)
      self.Cards.update({P_New_Title : Card})

      if P_Key != P_New_Title:
        del self.Cards[P_Key]

      return True

    else:
      return False
