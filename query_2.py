#executes query that finds how many recipes there are that have misspelled "cinnamon"
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipesdb"]
my_collection = mydb["Recipes"]

item = list(my_collection.find({"info.ingredients":{"$regex":"cinamon"}},
                              {"_id":0, "name": 1}))  
            
print(len(item),"recipes found")
print(item)
