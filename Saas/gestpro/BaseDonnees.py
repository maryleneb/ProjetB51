import sqlite3

class  BaseDonnees():
    def __init__(self):
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables(self.genererListeTables())
        self.insertion("stocks", ['date','trans', 'symbol',53.2,5.2])
        self.selection('Select * FROM stocks ')
        self.connecteur.close()
    
    def genererListeTables(self):
        listeTables = [ 
            ['stocks', ['date','text'], ['trans','text'], ['symbol','text'], ['qty','real'], ['price','real']],
            ['banane', ['date','text'], ['type','text'], ['symbol','text'], ['qty','real'], ['price','real']]
            ]
        return listeTables
        
    def creerTables(self, listeTables):
        try:
            for table in listeTables:
                stringDropTable = "DROP TABLE "
                stringDropTable += table[0]
                self.curseur.execute(stringDropTable)
        except:
            pass
        finally:
            for table in listeTables:
                stringCreate = "CREATE TABLE " + table[0] + "(" 
                for indiceEntrees in range(len(table)):
                    if indiceEntrees > 0:
                        stringCreate +=  table[indiceEntrees][0] + " " + table[indiceEntrees][1]
                        if indiceEntrees < len(table)-1:
                            stringCreate += ", "
                stringCreate += ")"
                self.curseur.execute(stringCreate)
                
    
    def insertion(self, nomTable = "", listeValeurs=[]):
        stringInsert = "INSERT INTO " + nomTable + " VALUES("
        for indiceEntree in range(len(listeValeurs)):
            if isinstance(listeValeurs[indiceEntree],str):
                listeValeurs[indiceEntree] = "'"+listeValeurs[indiceEntree]+"'"
                stringInsert += listeValeurs[indiceEntree]
            else:
                stringInsert += str(listeValeurs[indiceEntree])
            if indiceEntree < len(listeValeurs)-1:
                stringInsert += ", "
        stringInsert += ")"
        self.curseur.execute(stringInsert)
    
    
    def selection(self, stringSelect = ""):
        for rangee in self.curseur.execute(stringSelect):
            print(rangee)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()