import sqlite3

class  BaseDonnees():
    def __init__(self):
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables()
        self.creerTablesPrototype()
        self.insertion()
        self.selection()
        self.connecteur.close()
        
        
        
    def creerTables(self):
        listeTables = ['stocks', ['date','text'], ['trans','text'], ['symbol','text'], ['qty','real'], ['price','real']]
        try:
            self.curseur.execute("DROP TABLE stocks")
        except:
            pass
        finally:
            self.curseur.execute('''CREATE TABLE ''' +  listeTables[0] +''' ('''+listeTables[1][0]+listeTables[1][1]+
                                 ''',''' +listeTables[2][0]+listeTables[2][1]+''',''' +listeTables[3][0]+listeTables[3][1]+''',''' 
                                 +listeTables[4][0]+listeTables[4][1]+''',''' +listeTables[5][0]+listeTables[5][1]+''')''')
    def creerTablesPrototype(self):
        listeTables = [ 
            ['stocks', ['date','text'], ['trans','text'], ['symbol','text'], ['qty','real'], ['price','real']]
            ]
        """
        try:
            self.curseur.execute("DROP TABLE stocks")
        except:
            pass
        finally:
            self.curseur.execute('''CREATE TABLE ''' +  listeTables[0][0] +''' ('''+listeTables[0][1][0]+listeTables[0][1][1]+
                                 ''',''' +listeTables[0][2][0]+listeTables[2][1]+''',''' +listeTables[0][3][0]+listeTables[0][3][1]+''',''' 
                                 +listeTables[0][4][0]+listeTables[0][4][1]+''',''' +listeTables[0][5][0]+listeTables[0][5][1]+''')''')
        """
        print(listeTables)
    def insertion(self):
        self.curseur.execute("INSERT INTO stocks VALUES('text1','text2', 'BMO', 50, 100)")
        
    def selection(self):
        for rangee in self.curseur.execute('Select * FROM stocks '):
            print(rangee)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()