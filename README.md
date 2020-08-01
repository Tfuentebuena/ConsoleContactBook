# ConsoleContactBook
### Tobias Fuentebuena Guardon - Engineering Student at UTN-FRBA 2020
#### Contact:
Student: tfuentebuena@est.frba.utn.edu.ar  
Personal: tobiasfuentebuenaguardon@gmail.com

Simple console-based contact book which works with CSV files.  
Saves in a CSV and SQLite database the name, address, phone number and e-mail of every person you want.

*Functions* 
- Add contacts. Be sure to not add two contacts with identical names. 
- Delete contacts. 
- Search contacts. This function will show you all the data of the contact, but be sure you entered the full name of the contact. There is no partial search.
- Update contacts. If you don't enter a cell (phone number, for example) the program will keep the original one.
The program works with both custom and default files ("contacts.csv" as default). Although, the SQLite database won't be different, it will be overwritten.
The contacts are alphabetically ordered when dumped. 

It may be the one of the last versions of this script with date August 1st, 2020. There are only a few things to clean or improve, but most probably no more big functions will be added. The only thing to be added could be a GUI. 


**NOTE**: As I said, do not add contacts with identical names because they will be added but you won't be able to remove just one of them, it will be deleted all of them. 

