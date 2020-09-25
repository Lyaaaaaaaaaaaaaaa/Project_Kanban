# Project Kanban
---

## What does this project do?

This project is a lightweight user-friendly desktop software to create and manage basic [kanbans boards](#https://en.wikipedia.org/wiki/Kanban) for your personal use.

- [x] Create your kanban in one click.
- [x] Create your columns.
- [x] Create your cards.
- [ ] Drag and drop your cards from one column to another. *Not connected with the interface*
- [x] Auto save on your computer.
- [x] No account.
- [x] self-sufficient (It only needs GTK, no internet or other softwares needed).

## Why is this project useful?

I personally got disappointed by kanban softwares. You either had to pay for it or have to sign dark contracts and hope your information would stay yours...

Otherwise, open source softwares were fine but far too heavy for my humble use. I needed something simple and yet efficient to track my work (without mandatory Agile methodology). Then, I found [My Personal Kanban](#https://github.com/greggigon/my-personal-kanban). It was perfectly what I needed. Until I cleared my web browser cache and lost all my kanbans... (You can export your kanban into a file but doing it every time you edit a card is annoying).

That's why I'm making this project.

## How to test it?

The classes are done but there is no interface connected (WIP in Handler branch) to use them.
If you really want to try it I recommend taking a look at [Class' diagram](https://raw.githubusercontent.com/Lyaaaaaaaaaaaaaaa/Project_Kanban/master/management/uml/Class_Diagram.jpeg). 
The classes are in `src/classes/`.

The Handler branch is advanced enough to test it 
(it's still WIP! some signals are not done yet and the drag and drop feature isn't implemented yet!).
If you want to test it download the project and use the Handler branch,
then create a main.py in the `src/classes/` folder (the file name is not important)
and simply write the following lines
```
from interface import Interface

Interface = Interface()
Interface.Connect_Interface()
Interface.Connect_Signals()
Interface.Start_Application()
```
then run this file. 

## More information:


[Code of conduct](https://github.com/Lyaaaaaaaaaaaaaaa/Project_Kanban/blob/master/CODE_OF_CONDUCT.md)

[How to contribute](https://github.com/Lyaaaaaaaaaaaaaaa/Project_Kanban/blob/master/CONTRIBUTING.md)

