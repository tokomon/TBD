from neo4jrestclient.client import GraphDatabase

db = GraphDatabase("http://localhost:7474/", username="neo4j", password="neo4j")

query = "MATCH p=(e:WordStem {Stem:'lion'})-[r:Weights]-(c:WordStem) WHERE tofloat(r.Weight)>0.1 RETURN  c.Stem" # ORDER BY tofloat(r.Weight) DESC"
results = db.query(query,data_contents=True)
list = []
listT=[]
for i in results.rows:
    q = []
    query = "MATCH p=(e:WordStem{Stem:'"+i[0]+"'} )-[r:Weights]->(c:WordStem) WHERE tofloat(r.Weight)>0.1 RETURN  c.Word, (r.Weight)"
    resultsA = db.query(query,data_contents=True)
    for j in resultsA.rows:
        """cont = 0
        for k in range(0,len(listT)):
            #print (listT[k])
            if j[0]==listT[k][0]:
                listT[k][1]+=float(j[1])
            else:
                cont+=1
        if cont==len(listT):
            listT.append([j[0],0])
        """
        if ( [j[0],0] not in listT):
            listT.append([j[0],0])
        q.append([j[0],float(j[1])])
    list.append(q)



for i in listT:
    for j in list:
        for k in j:
            if i[0] in k:
                i[1]+=k[1]

def takeSecond(elem):
    return float(elem[1])

# sort list with key
listT.sort(reverse=True,key=takeSecond)
for i in range (0,100):
    print(listT[i])






#ranking de Aristas



#interseccion de palabras en list


#load csv with headers from "file:///home/tokomon/Documentos/Vocc/vocabularioRelations_0.csv"
#as relations  MATCH (a:WordStm),(b:WordStm)
#WHERE a.Stem =relations.Stem1 AND b.Stem = relations.Stem2
#CREATE (a)-[r:WEIGHT {weight:relations.Peso}]->(b)

#query = "load csv with headers from 'file:///home/tokomon/Documentos/vocabularioNeo.csv' as words CREATE (a:WordStem { id : words.ID,stem : words.Stem , word : words.Word })"
"""
totalDoc=59728
for num in range(1,totalDoc):#totalDoc):#0,10000):#10000,20000):#0,20000):#30,25000):#2305963
    #os.remove('vocabularioRelations_'+str(num)+'.csv')
    print (num)

    query = "load csv with headers from 'file:///home/tokomon/Documentos/Vocc/vocabularioRelations_"+str(num)+".csv' as relations MATCH (a:WordStem),(b:WordStem) WHERE a.id =relations.ID1 AND b.id = relations.ID2 CREATE (a)-[r:WEIGHT {weight:relations.Weight}]->(b) "

    #query = ("MATCH (a:WordStem),(b:WordStem) WHERE a.id ='3' AND b.id = '4' CREATE (a)-[r:WEIGHT {weight:'1'}]->(b)")

    results = db.query(query,data_contents=True)
    print (results.rows)
"""







"""
# Create some nodes with labels
user = db.labels.create("User")
u1 = db.nodes.create(name="dog",stem="",valo)
user.add(u1)
u2 = db.nodes.create(name="Daniela")
user.add(u2)

beer = db.labels.create("Beer")
b1 = db.nodes.create(name="Punk IPA")
b2 = db.nodes.create(name="Hoegaarden Rosee")
# You can associate a label with many nodes in one go
beer.add(b1, b2)
"""
