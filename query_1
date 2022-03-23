#executes a query that finds all recipes for breakfast foods

import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipesdb"]
my_collection = mydb["Recipes"]

item = list(my_collection.find({"$or":[{"info.description":{"$regex":"breakfast"}}, 
                                       {"info.description":{"$regex":"Breakfast"}}]},
                              {"_id":0, "name": 1}))  
            
print(len(item),"recipes found")
print(item)
