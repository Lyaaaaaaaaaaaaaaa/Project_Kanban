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
#--   03/02/2020 Lyaaaaa
#--     - Edited __init__ to add a P_Name parameter to change the name
#--         of the file when it's created
#--   31/02/2020 Lyaaaaa
#--     - Splitted Create_File into two functions
#--       - Create_Directory, which try to create the directory
#--       - Create_File, which call Create_Directory then try to create the file.
#--
#--   24/09/2020 Lyaaaaa
#--     - Added Delete_File method.
#--     - Updated Create_Directory and Create_File methods to return True if
#--         success and false if failure.
#--     - Added Rename_File method to rename the save file and self.name.
#--
#--   25/09/2020 Lyaaaaa
#--     - Removed some debug prints
#--
#--    19/01/2021 Lyaaaaa
#--      - Removed outdated comments.
#--      - Set_Path, Set_Name no longer return bool.
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
#--  -
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
#--  - Control P_Path to be a valid path before to edit the path attribut
#--    and return true if everything alright.
#---------------------------------------------------------------------------

  def Set_Path(self, P_Path):
    self.path = P_Path

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
#--  - Control name, forbid whitespaces, special characters and length
#---------------------------------------------------------------------------

  def Set_Name(self, P_Name):
    P_Name = P_Name + ".yaml"
    self.name = P_Name

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
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Create_File(self):
    path = self.path + self.name

    self.Create_Directory()
    try:
      open(path, "x")
      return True

    except FileExistsError:
      print("File ", self.name , "already exists")
      return False


#---------------------------------------------------------------------------
#-- Create_Directory
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

  def Create_Directory(self):
    try:
      os.mkdir(self.path)
      return True

    except FileExistsError:
      print("Directory", self.path , "already exists")
      return False

#---------------------------------------------------------------------------
#-- Delete_File
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

  def Delete_File(self):
    try:
      os.remove(self.path + self.name)
      return True

    except OSError:
      print ("Error while trying to delete", self.path + self.name)
      return False


#---------------------------------------------------------------------------
#-- Rename_File
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Rename the actual file and call Set_Name to update self.name.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Rename_File(self, P_New_Name):
    try:
      old_name = self.name
      os.rename(self.path + old_name, self.path + P_New_Name + ".yaml")
      self.Set_Name(P_New_Name)
      return True

    except OSError:
      print ("Error while trying to rename", self.path + old_name)
      return False
