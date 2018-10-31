import sqlite3

class  BaseDonnees():
    def __init__(self):
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        #self.creerTables()
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
            stringBD = '''CREATE TABLE ''' +  listeTables[0] +''' ('''+listeTables[1][0]+listeTables[1][1]+''',''' +listeTables[2][0]+listeTables[2][1]+''',''' +listeTables[3][0]+listeTables[3][1]+''',''' +listeTables[4][0]+listeTables[4][1]+''',''' +listeTables[5][0]+listeTables[5][1]+''')'''
            self.curseur.execute(stringBD)
    
    def creerTablesPrototype(self):
        listeTables = [ 
            ['stocks', ['date','text'], ['trans','text'], ['symbol','text'], ['qty','real'], ['price','real']],
            ['banane', ['date','text'], ['type','text'], ['symbol','text'], ['qty','real'], ['price','real']]
            ]
        try:
            self.curseur.execute("DROP TABLE stocks")
            self.curseur.execute("DROP TABLE banane")
        except:
            pass
        finally:
            for table in listeTables:
                stringBD = "CREATE TABLE " + table[0] + "(" 
                for indiceEntrees in range(len(table)):
                    if indiceEntrees > 0:
                        stringBD +=  table[indiceEntrees][0] + " " + table[indiceEntrees][1]
                        if indiceEntrees < len(table)-1:
                            stringBD += ", "
                stringBD += ")"
                self.curseur.execute(stringBD)
                
        
   
            
    def insertion(self):
        self.curseur.execute("INSERT INTO stocks VALUES('text1','text2', 'BMO', 50, 100)")
        
    def selection(self):
        for rangee in self.curseur.execute('Select * FROM stocks '):
            print(rangee)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()