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
#--   3/2/2020 Lyaaaaa
#--     - Created file.
#--
#---------------------------------------------------------------------------

from kanban import Kanban
from file   import File

import os

class Load():
  """Scan save's folder and create objects from file"""

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

  def __init__(self):
    self.Files_Names = []
    self.Scan_Saves()

#---------------------------------------------------------------------------
#-- Load
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  - TODO Create a kanban from the file.
#---------------------------------------------------------------------------

  def Load(self, P_File_Name):
    pass

#---------------------------------------------------------------------------
#-- Scan_Saves
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Returns False if no save found
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Scan_Saves(self):
    for file in os.listdir("saves"):
      if file.endswith(".yaml"):
        self.Files_Names.append(file)

#---------------------------------------------------------------------------
#-- Get_Files
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

  def Get_Files_Names(self):
    return self.Files_Names
