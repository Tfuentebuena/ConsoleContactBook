# ConsoleContactBook
### Tobias Fuentebuena Guardon - Engineering Student at UTN-FRBA 2020
#### Contact:
Student: tfuentebuena@est.frba.utn.edu.ar  
Personal: tobiasfuentebuenaguardon@gmail.com

Simple console-based contact book which works with CSV files.  
SQLite may be added in the future.  
The script dumps in a CSV the name, address, phone number and e-mail of every person you want. You can also update or delete any entry.  
Now the script is able to work with custom csv files if they have the default format of columns. The default one is still 'contacts.csv'. 
Added the function to order the data, only when needed, alphabetically. 


*I DO NOT RECOMMEND USING IT AS IT IS NOW*, but if you still want to try, consider the next points:
- If you want to update a contact, every cell must be filled when asked. Otherwise, you will get an empty cell for every one you didn't fill. 
- When you are asked for a name (search, delete, update) you have to enter exactly the same name as in the CSV but the upper and lowercase doesn't matter. Also, be sure to not add two or more contacts with the same name because doing will result in the first ones being ignored during search and all of them deleted at once with the delete command.


