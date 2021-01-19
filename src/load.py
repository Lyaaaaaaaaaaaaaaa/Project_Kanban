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
#--   03/02/2020 Lyaaaaa
#--     - Created file.
#--
#--   04/02/2020 Lyaaaaa
#--     - Added a new method: Yaml_Object_Constructor to create Python objects
#--         from the save file
#--     - Added yaml package in imports
#--     - Renamed Load method into Load_Save_File to avoid confusing with the
#--         class' name
#--     - Implemented Load_Save_File method
#--
#--   31/08/2020 Lyaaaaa
#--     - To fix an error appearing when Scan_Saves is called but no saves
#--         folder exist, I created a new method Create_Directory which call
#--         a File's method named Create_Directory.
#--     - Create_Directory is called on the init of the class right before
#--         Scan_Saves.
#--
#--   03/09/2020 Lyaaaaa
#--     - Get_Files_Names now return the names without the .yaml.
#--     - Load_Save_File now loads the file named after the parameter given but
#--         manually adds .yaml at the end of the name given.
#--
#--   30/10/2020 Lyaaaaa
#--     - Updated Load_Save_File to directly return yaml.load as it is the
#--         Kanban object already.
#--
#--   31/10/2020 Lyaaaaa
#--     - Added expanduser module to use the home path.
#--     - Updated Load_Save_File and Scan_Saves to use the home.
#--     - Updated the saves location, saves are now located at
#--         `home`/project_kanban_saves/
#--
#--    19/01/2021 Lyaaaaa
#--      - Updated Scan_Saves and Load_Save_File to change the saves path.
#---------------------------------------------------------------------------

from .kanban import Kanban
from .file   import File
from os.path import expanduser

import yaml
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
    self.Create_Directory()
    self.Scan_Saves()

#---------------------------------------------------------------------------
#-- Load_Save_File
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Load the file named like P_File_Name with a .yaml at the end.
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Load_Save_File(self, P_File_Name):
    yaml.add_constructor(u'tag:yaml.org,2002:python/object:kanban.Kanban',
                         self.Yaml_Object_Constructor)
    home = expanduser("~")
    data = home + "/.var/app/io.github.lyaaaaaaaaaaaaaaa.Project_Kanban/data"

    with open( data + "/saves/" + P_File_Name + ".yaml", 'r') as stream:
      try:
        Kanban = (yaml.load(stream, Loader=yaml.Loader))
        return Kanban

      except yaml.YAMLError as error_message:
        print(error_message)
        return False

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
    home = expanduser("~")
    data = home + "/.var/app/io.github.lyaaaaaaaaaaaaaaa.Project_Kanban/data"

    for file in os.listdir(data + "/saves"):
      if file.endswith(".yaml"):
        self.Files_Names.append(file)

#---------------------------------------------------------------------------
#-- Get_Files
#--
#-- Portability Issues:
#--  -
#--
#-- Implementation Notes:
#--  - Returns the saves names without the extentions ".yaml"
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Get_Files_Names(self):
    names = []

    for file_name in self.Files_Names:
      name = file_name.replace(".yaml", "")
      names.append(name)

    return names

#---------------------------------------------------------------------------
#-- Yaml_Object_Constructor
#--
#-- Portability Issues:
#--  - Heavy dependancy on the yaml package
#--
#-- Implementation Notes:
#--  -
#--
#-- Anticipated Changes:
#--  -
#---------------------------------------------------------------------------

  def Yaml_Object_Constructor(self, P_Loader, P_Node):
    value = P_Loader.construct_mapping(P_Node)
    return value

#---------------------------------------------------------------------------
#-- Create_Directory
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

  def Create_Directory(self):
    Temp_File = File()
    Temp_File.Create_Directory()
