from rel import Relation
from sqliteEnum import SqliteTypes as sType
from expr import Expression


class Select(Expression):
	#Select(Condition("Attribut","Valeur",Relation))
	#Show all arguments
	# exemple : Select(Neq(’Country’, 'Mali’),'CC') = S_Country="Mali" (CC)
	
	def __init__(self, ope: Expression)-> None:
		
		__checkOpe(self,ope),
		
		super().__init__(rel,None,None)
		self.ope=ope
		
		self.newName = str(self.ope)
	
	def __checkOpe(self,ope):
		if (len(ope) == 0):
			raise Exception("The length of operation must be greater than 0")
	
	def __checkArgCompare(self,key,val):
		if(not self.rel.args.__contains__(key)):
			raise Exception("The relation "+self.rel.name+" don't have key called \""+key+"\"")
		try:
			float(val)


class Eq(Select):
	#Eq("Attribut","Value",rel) = \sigma_{'Attribut'=Value}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self):  
		return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" = "+self.val
	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:		#gère le cas si value est un nombre ou non (à vérifier si ça marche sans convertir en float)
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) == float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:	
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper == self.val.upper:
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
		
	
	
	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R

class Neq(Select):
	#Neq("Attribut","Value",rel) = \sigma_{'Attribut'!=Value}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self): 
			return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" <> "+self.val

	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) != float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper != self.val.upper:		#gérer le cas full majuscule
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs

	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R

class Gteq(Select):
	#Gteq("Attribut","Value",rel) = \sigma_{'Attribut'>=Value}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self): 
			return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" >= "+self.val

	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) >= float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper >= self.val.upper:		#gérer le cas full majuscule
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs

	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R
		
class Gt(Select):
	#Gt("Attribut","Value",rel) = \sigma_{'Attribut'>'Value'}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self): 
			return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" > "+self.val

	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) > float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper > self.val.upper:		#gérer le cas full majuscule
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs

	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R

class Lteq(Select):
	#Lteq("Attribut","Value",rel) = \sigma_{'Attribut'<='Value'}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self): 
			return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" <= "+self.val

	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) <= float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper <= self.val.upper:		#gérer le cas full majuscule
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs

	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R

class Lt(Select):
	#Lt("Attribut","Value",rel) = \sigma_{'Attribut'<'Value'}(rel)
	def __init__(self,key: str,val: str,rel: Relation)->None:
		
		self.__checkArgCompare(self,key,val)
		
		self.rel=rel
		self.key=key
		self.val=val
	
	def __str__(self): 
			return "SELECT * FROM " + self.rel.getName()+" WHERE "+self.key+" < "+self.val

	
	def __getNewArgs(self) -> dict:
		newArgs = {}
		
		try:
			for k in self.rel.getArgs():
				if (k == self.key and float(self.rel.getArgs()[k]) < float(self.val):
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs
			
		except:
			for k in self.rel.getArgs():
				if (k == self.key and self.rel.getArgs()[k].upper < self.val.upper:		#gérer le cas full majuscule
					newArgs[k] = self.rel.getArgs()[k]
			return newArgs

	def __createRelation(self) -> Relation:
        # We get the new arguments of the new Relation
        newArgs = self.__getNewArgs()
        # We create the rel with those new Args
        R = Relation(self.rel.getDataBase(),self.newName,newArgs)
        
    
        # We re add all the tuple from the other relation
        nbOfTup = self.rel.getNbOfTuple()
        cursor = self.rel.getCursor().execute(str(self))
        tup = cursor.fetchall()
        self.rel.killCursor()
        for i in range(nbOfTup):
            R.addTuple(tup[i])
        
        return R