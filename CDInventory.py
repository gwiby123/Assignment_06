#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# GByron, 2022-Mar-09, Modified/ File and Completed Alterations
#------------------------------------------#

# -- DATA -- #
strChoice = '' 
lstTbl = []  
dicRow = {} 
strFileName = 'CDInventory.txt'  
objFile = None  


# -- PROCESSING -- #
class DataProcessor: 
    """ Searches for ID in table, if it exists entry is deleted. 
     if not user recieves 'Could not find this CD!' """
     
    def delete_cd_from_table(intIDDel):
        intRowNr = -1
        blnCDRemoved = False
        for row in lstTbl:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del lstTbl[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
            
    """"THis saves the data within the system"""
    
    def save_data(strFileName):
        if strYesNo == 'y':
            objFile = open(strFileName, 'w')
            for row in lstTbl:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
            objFile.close()
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
            
    def adding_cd():
        cd_lst= IO.add_cd()
        dicRow = {'ID': cd_lst[0], 'Title': cd_lst[1], 'Artist': cd_lst[2]}
        lstTbl.append(dicRow)
                         
class FileProcessor:
    """Processing the data to and from text file"""
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

# -- PRESENTATION (Input/Output) -- #

class IO:    
    """Handling Input / Output"""

    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print() 
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')
        
        
        """Adds CD of user choice to the list, does not save the CD to memory"""
        
    def add_cd():
        strID = input('Enter ID: ').strip()
        strTitle = input('Enter the CD\'s title. ').strip()
        stArtist = input('Enter the Artist\'s name. ').strip()
        intID = int(strID)
        return [intID, strTitle, stArtist]

# 2. start main loop
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue
    elif strChoice == 'a':
        DataProcessor.adding_cd()
        IO.show_inventory(lstTbl)
        continue  
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  
    elif strChoice == 'd':
        IO.show_inventory(lstTbl)
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        DataProcessor.delete_cd_from_table(intIDDel)
        IO.show_inventory(lstTbl)
        continue
    elif strChoice == 's':
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        DataProcessor.save_data(strFileName)

        continue
    else:
        print('General Error')


