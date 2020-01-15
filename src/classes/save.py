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
#--   30/12/2019 Lyaaaaa
#--     - Created file.
#--     - Save method calls File.Create_File method so it creates the directory
#--       and save file before to try writing anything.
#--     - Save becomes Write_Save.
#--     - Created Read_Save method
#---------------------------------------------------------------------------

from file import File

class Save():
  """Represent the save actions"""

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

  def __init__(self, P_File):
    self.File = P_File

  #---------------------------------
  #--       Functions Set         --
  #---------------------------------

#---------------------------------------------------------------------------
#-- Set_File
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

  def Set_File(self, P_File):
    self.File = P_File
    return True

  #---------------------------------
  #--       Functions Get         --
  #---------------------------------

#---------------------------------------------------------------------------
#-- Get_File
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

  def Get_File(self):
    return self.File

  #-----------------------------
  #--       Functions         --
  #-----------------------------

#---------------------------------------------------------------------------
#-- Save
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

  def Write_Save(self):
    self.File.Create_File()

    path        =        self.File.Get_Path()
    path        = path + self.File.Get_Name()
    opened_file = open(path, "w")

    opened_file.write("Project MSOA") #TODO Write useful data with good format
    return True

#---------------------------------------------------------------------------
#-- Read_Save
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - Correctly parse the file depending of the futur format.
#---------------------------------------------------------------------------

  def Read_Save(self): #TODO Parse data from save or send it into a function.

    path        =        self.File.Get_Path()
    path        = path + self.File.Get_Name()
    opened_file = open(path, "r")

    print (opened_file.read())
