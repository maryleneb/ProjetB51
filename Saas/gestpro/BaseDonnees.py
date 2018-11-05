import sqlite3

class  BaseDonnees():
    def __init__(self):
        self.connecteur = sqlite3.connect('SAAS.db')
        self.curseur = self.connecteur.cursor()
        self.creerTables(self.genererListeTables(),self.genererListeConst())
        self.insertion("stocks", ['date','trans', 'symbol',53.2,5.2])
        self.selection('Select * FROM stocks ')
        self.connecteur.close()
    
    def genererListeTables(self):
        listeTables = [ 
            ['stocks', ['date','text'], ['trans','text'], ['symbol','text'], ['qty','real'], ['price','real']],
            ['banane', ['date','text'], ['type','text'], ['symbol','text'], ['qty','real'], ['price','real']]
            ]
        return listeTables
    
    def genererListeConst(self):
        listeConst = [
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ['table a modifier', 'nom de la contrainte', 'laForeign Key', 'la table de reference', 'variable de reference'],
            ]
        
    def creerTables(self, listeTables, listeConst):
        try:
            for table in listeTables:
                stringDropTable = "DROP TABLE "
                stringDropTable += table[0]
                stringDropTable += "CASCADE CONSTRAINTS;"
                self.curseur.execute(stringDropTable)
        except:
            pass
        finally:
            for table in listeTables:
                stringCreate = "CREATE TABLE " + table[0] + "(" 
                for indiceEntrees in range(len(table)):
                    if indiceEntrees > 0:
                        stringCreate +=  table[indiceEntrees][0] + " " + table[indiceEntrees][1] + " " + table[indiceEntrees][2]
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
            
    def alterTable(self):
        for contrainte in listeConst:
            stringCreate = "ALTER TABLE " + table[0] + " ADD CONSTRAINT " + table[1] + " FOREIGN KEY(" + table[2] + ") REFERENCES " + table[3] + "(" + table[4] + ");"
            self.curseur.execute(stringCreate)
           
        
if __name__ == "__main__":
    baseDonnees = BaseDonnees()