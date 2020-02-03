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
#--     - Added Create_File method (which create a directory too).
#--
#--   03/02/2020 Lyaaaa
#--     - Edited __init__ to add a P_Name parameter to change the name
#--         of the file when it's created
#---------------------------------------------------------------------------

import os

class File():
  """Represent the save file"""

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
#--  - TODO Name the file after the kanban. Exemple: Kanban's name is Shipping50
#--      the save's name would be Shipping50_save.yaml
#---------------------------------------------------------------------------

  def __init__(self, P_Name = "save"):
    self.path = "saves/"
    self.name = P_Name + ".yaml"

  #---------------------------------
  #--       Functions Set         --
  #---------------------------------s

#---------------------------------------------------------------------------
#-- Set_Path
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - #TODO Control P_Path to be a valid path before to edit the path attribut
#--    and return true if everything alright.
#---------------------------------------------------------------------------

  def Set_Path(self, P_Path):
    self.path = P_Path
    return True

#---------------------------------------------------------------------------
#-- Set_Name
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - #TODO Control name, forbid whitespaces, special characters and length
#---------------------------------------------------------------------------

  def Set_Name(self, P_Name):
    P_Name = P_Name + ".yaml"
    self.name = P_Name
    return True

  #---------------------------------
  #--       Functions Get         --
  #---------------------------------

#---------------------------------------------------------------------------
#-- Get_Path
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

  def Get_Path(self):
    return self.path

#---------------------------------------------------------------------------
#-- Get_Name
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

  def Get_Name(self):
    return self.name

  #-----------------------------
  #--       Functions         --
  #-----------------------------

#---------------------------------------------------------------------------
#-- Create_File
#--
#-- Portability Issues:
#--  - Tries creating a directory, I guess permissions could create problems
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Create_File(self):
    path = self.path + self.name

    try:
      os.mkdir(self.path)
    except FileExistsError:
      print("Directory ", self.path , "already exists")

    try:
      open(path, "x")
      return True
    except FileExistsError:
      print("File ", self.name , "already exists")
      return False
