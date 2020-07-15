# ConsoleContactBook
### Tobias Fuentebuena Guardon - Engineering Student at UTN-FRBA 2020
#### Contact:
Student: tfuentebuena@est.frba.utn.edu.ar  
Personal: tobiasfuentebuenaguardon@gmail.com

Simple console-based contact book which works with CSV files.  
SQLite may be added in the future.  
The script dumps in a CSV the name, address, phone number and e-mail of every person you want. You can also update or delete any entry.  
Search is supported even in another files if you rename them as 'contacts.csv' and they have the same format (name-address-phone-email) at the time. 

*I DO NOT RECOMMEND USING IT AS IT IS NOW*, but if you still want to try, consider the next points:
- The script has a default CSV file for testing. You have to delete it (it is safe) to have a new formatted file.
- If you want to update a contact, every cell must be filled when asked. Otherwise, you will get an empty cell for every one you didn't fill. 
- When you are asked for a name (search, delete, update) you have to enter exactly the same name as in the CSV but the upper and lowercase doesn't matter. 


