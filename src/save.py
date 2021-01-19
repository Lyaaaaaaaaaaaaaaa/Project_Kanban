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
#--     - Save method calls File.Create_File method so it creates the directory
#--       and save file before to try writing anything.
#--     - Save becomes Write_Save.
#--     - Created Read_Save method
#--
#--   03/02/2020 Lyaaaaa
#--     - Added yaml import
#--     - Edited Write_Save
#--         - Added P_Kanban parameter. This is the kanban the class will save
#--         - Added a file header to the save files.
#--         - Now successfully export a kanban object and all it's attributs!
#--
#--   04/02/2020 Lyaaaaa
#--     - Made Write_Save a private method "__Write_Save"
#--     - Added a new method, Write_Save (replaced the former one) which cannot
#--         overwrite a save (Except if you specifically ask it to overwrite).
#--         this method, then call __Write_Save if everything alright.
#--
#--   01/09/2020 Lyaaaaa
#--     - Updated Write_Save and __Write_Save.
#--       - __Write_Save no longer calls Create_File because Write_Save does
#--           and Write_Save calls __Write_Save. Therefore, it was useless.
#--       - Corrected an error in Write_Save. The condition for calling
#--           __Write_Save was wrong and it was never called if P_Overwrite
#--           wans't set to True.
#--       - Write_Save now return True if everything is good.
#--
#--   23/09/2020 Lyaaaaa
#--     - Removed a useless comment and edited an incorrect one.
#--
#--    19/01/2021 Lyaaaaa
#--      - Removed outdated comments.
#--      - Set_File no longer returns bool.
#--      - Deleted Read_Save (never used, Moreover, Save class is here to save
#--          not read).
#---------------------------------------------------------------------------

from file import File
import yaml

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
#-- Write_Save
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - It's recommended not to use this method directly. Instead, use Write_Save
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def __Write_Save(self, P_Kanban):

    path        =        self.File.Get_Path()
    path        = path + self.File.Get_Name()
    opened_file = open(path, "w")

    opened_file.write("#" + "-----" * 15 + "\n")
    opened_file.write("#-- Copyright (c) 2020 Lyaaaaaaaaaaaaaaa \n")
    opened_file.write("#-- Project Kanban \n")
    opened_file.write("#" + "-----" * 15 + "\n")
    opened_file.write("\n \n")

    try:
      opened_file.write(yaml.dump(P_Kanban))
      return True
    except yaml.YAMLError as exc:
      print(exc)
      return False

#---------------------------------------------------------------------------
#-- Write_Save
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Safeguard for __Write_Save to avoid erasing existing save!
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Write_Save(self, P_Kanban, P_Overwrite = False):

    if P_Overwrite == True:
      self.__Write_Save(P_Kanban)

    elif P_Overwrite == False:

      if self.File.Create_File() == True:
        self.__Write_Save(P_Kanban)
        return True

      else:
        print ("Can't erase existing file : "
               + self.File.Get_Name()
               + ". Overwrite not allowed.")
        return False
