from kanban import Kanban
from file   import File
from save   import Save

file = File()
save = Save(file)


print(file.Get_Path() + file.Get_Name())
file.Set_Name("Project_MSOA")

save.Write_Save()
save.Read_Save()
