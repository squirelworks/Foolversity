# Boundary

Foolversity, Foolcourse, and Foolbook are separate repositories.
They do not import each other. They meet at files.

| file | who writes | who reads |
| --- | --- | --- |
| `.fcs` | Foolversity (`main/fcs.py`) | Foolcourse and Foolbook, each with its own opener |
| `.curriculum.json` | Foolversity (`main/curriculum.py`) | Foolcourse |
| `.school.json` | Foolversity (`main/school.py`) | Foolversity |

`.fcs` is the Foolcourse Student standard. Foolversity implements a
writer for that envelope. It is not a copy of Foolcourse's opener.

`.school.json` is Foolversity's own file. Foolcourse does not read it.
