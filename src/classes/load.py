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
#--   04/02/2020 Lyaaaa
#--     - Added a new method: Yaml_Object_Constructor to create Python objects
#--         from the save file
#--     - Added yaml package in imports
#--     - Renamed Load method into Load_Save_File to avoid confusing with the
#--         class' name
#--     - Implemented Load_Save_File method
#---------------------------------------------------------------------------

from kanban import Kanban
from file   import File

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
    self.Scan_Saves()

#---------------------------------------------------------------------------
#-- Load_Save_File
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

  def Load_Save_File(self, P_File_Name):
    yaml.add_constructor(u'tag:yaml.org,2002:python/object:kanban.Kanban',
                         self.Yaml_Object_Constructor)

    with open("saves/" + P_File_Name, 'r') as stream:
      try:
        value         = (yaml.load(stream, Loader=yaml.Loader))
        Loaded_Kanban = Kanban(value['title'])

        Loaded_Kanban.Set_Columns(value['Columns'])
        return Loaded_Kanban

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
    
