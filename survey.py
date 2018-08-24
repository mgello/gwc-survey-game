import json
answer = {"name":[], "genre":[], "origin":[], "books":[], "artist": []}


i = 0
while True:
    if i<5:
        
        print("\n\nhello. this is a survey now ANSWER MY QUESTIONS (please)\n")
                #wait

        name = input("\nwhat is your name?\n")
        print("who names someone " + name + "...\n")
        print("        ------     ")

        genre = input("\ndo you prefer pop or rock?\n")
        print("wow " + genre + "? Interesting\n")
        print("        ------     ")

        origin = input("\nwhere are you from?\n")
        print(origin + "! nice nice.\n")
        print("        ------     ")

        books = input("\ndo you enjoy reading books?\n")
        print("okay.\n")
        print("        ------     ")

        artist = input("\nwho is your favorite artist?\n")
        print(artist +"? ill check them out.\n")
        print("        ------     ")
        
        i+=1
        answer['name'].append(name)
        answer['genre'].append(genre)
        answer['origin'].append(origin)
        answer['books'].append(books)
        answer['artist'].append(artist)
        
            
        print("\n\nyour answers\n")
        print(answer)
        
        
    else:
        i=0
        jsonDict = json.dumps(answer)
        f = open("jsurvey.json", 'w')
        f.write(jsonDict)
        f.close()
        

            






