from column import Column

Column = Column()
print (Column.Get_Cards_Number())
Column.Add_Card()
print (Column.Get_Cards_Number())
Column.Add_Card()
print (Column.Get_Cards_Number())


Cartes = Column.Get_Cards()

print (Cartes[0].Get_Title())
Cartes[1].Set_Title("Nouveau titre")
print (Cartes[1].Get_Title())

Column.Set_Cards(Cartes)
Cartes = Column.Get_Cards()

print (Cartes[1].Get_Title())
