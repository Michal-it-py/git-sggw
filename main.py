#tu bedz appka we Flasku


#git pull - zaciagnij zmiany 
#git push - wypchnij swoje zmiany
#git log
#git checkout main - zmiana brancha na main; pozniej git pull
#git status - sprawdzamy gdzie jetesmy, co sie dzieje 
#git add ; . kropka dodaje wszystkie untracked files do add
#git commit -m "wiadmosc"

#-m feat - feature
#-m major - duza zmiana
#-m fix - 

#git push origin main 
#git checkout -b <nazwa>  =(nowa gałąź)


from flask import Flask

app = Flask(__name__)

if __name__ =="__main__":
    app.run(port = 8080)



