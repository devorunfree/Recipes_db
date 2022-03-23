import pymongo
import json
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["recipesdb"]
my_collection = mydb["Recipes"] # create a collection
count = 1
with open("recipeitems.json", encoding="utf8") as json_file:
    for line in json_file:
        try:
            recipe_obj = json.loads(line)
            
            e_check = [('ingredients'), ('url'), ('image'), 
            ('ts'), ('cookTime'), ('source'), ('recipeYield'), 
            ('datePublished'), ('prepTime'), ('description')]
            for e in e_check:
                if e not in recipe_obj:
                    recipe_obj[e] = "null"
            
            _id = recipe_obj["_id"]["$oid"]
            name = recipe_obj["name"] 
            
            info = {'ingredients': recipe_obj['ingredients'], 'url': recipe_obj['url'], 'image': recipe_obj['image'],
            'date': recipe_obj['ts']['$date'],'cookTime': recipe_obj['cookTime'], 'source': recipe_obj['source'],
            'recipeYield': recipe_obj['recipeYield'],'datePublished': recipe_obj['datePublished'],
            'prepTime': recipe_obj['prepTime'], 'description': recipe_obj['description']}

            print("Adding recipe:", _id, name, count)
            insert_result = my_collection.insert_one(
            {
            '_id': _id,
            'name': name,
            'info': info,
            }
            )
            count += 1
        except Exception as e:
            print(e, name, count)
#             print("Error has occurred.", name, count)
            count += 1
