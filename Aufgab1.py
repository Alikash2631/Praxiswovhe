from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder


#Mangas Class
class Mangas(BaseModel):
    def __init__(self, *args):
        super(Mangas, self).__init__(*args)
        
    mange_id:int |None = None
    mange_title:str |None = None
    Bande_name:str |None = None
    Erscheinnung_Jahr:str |None = None 
    Herausgeber:str |None = None 
    Autor:str |None = None 
    seitenzahl:int |None = None
    
class Animes(BaseModle):
    def __init__(self, *args):
        super(Animes, self).__init__(*args)
        
    anime_id:int |None = None
    mange_title:str |None = None
    Erscheinnung_Jahr:str |None = None 
    Herausgeber:str |None = None 
    länger:int |None = None
            
    
    
#Mangas
Mangas =[
    {"mange_id":1,"mange_title":'Attack on Titan',"Bande_name":'eins',
     "Erscheinnung_Jahr":2017,"Herausgeber":'Egmonta_Manga',"Autor":'Makoto Shinkal',
     "seitenzahl": 180},
    
    {"mange_id":2,"mange_title":'Attack on Titan',"Bande_name":'eins',
     "Erscheinnung_Jahr":2014,"Herausgeber":'Carlsen',"Autor":'Hajime Isayama',
     "seitenzahl": 192},
    
    {"mange_id":3,"mange_title":'Death Note',"Bande_name":'eins',
     "Erscheinnung_Jahr":2015,"Herausgeber":'TOKYOPOP',"Autor":'Takeshi Obata und Tsugumi Ohba',
     "seitenzahl": 208}] 

#Anime
Animes =[
    {"anime_id":1,"anime_title":'Death Note',"Erscheinnung_Jahr":2006,
     "Herausgeber":'Yosuke Yafune',"länget": 125},
    
    {"anime_id":2,"anime_title":'Attack on Titan',"Erscheinnung_Jahr":2013,
     "Herausgeber":'Mikasa Ackermann',"länget": 120},
    
    {"anime_id":3,"anime_title":'One Piece',"Erscheinnung_Jahr":1999,
     "Herausgeber":'Eiichirō Oda',"länget": 24}]



app = FastAPI()

@app.get("/")
async def root():
    return {"Die werte von Mangas und Anime"} 

@app.get("/Mangas")
async def get_Mange():
    return Mangas

@app.get("/mangas/{id}")
async def get_mange(id):
    for u in Mangas:
        if u["mange_id"] == int(id):
            return u 
@app.post("/Mangass", status_code=201)
async def add_Mangas(new_mange: Mangas):
    users.append(new_mange)
    return(Mangas)

#put
@app.put("/Maangas/{mange_id}")
async def put_mange(mange_id: int, mange: Mangas):
    update_encoded = jsonable_encoder(mange)
    users[mange_id-1] = update_encoded
    return Mangas

#delete
@app.delete("/Maangas/{Mange_id}", status_code=200)
async def delete_mange(mange_id: int) -> None:
    users.remove(Mangas[mange_id-1])
    return Mangas
 
#Animes
@app.get("/Animes")
async def get_anime():
    return Animes

@app.get("/Animes/{id}")
async def get_anime(id):
    for u in Animes:
        if u["anime_id"] == int(id):
            return u 
@app.post("/Animes", status_code=201)
async def add_Animes(new_anime: Animes):
    users.append(new_anime)
    return(Animes)

#put
@app.put("/Animes/{anime_id}")
async def put_anime(anime_id: int, anime: Animes):
    update_encoded = jsonable_encoder(anime)
    users[anime_id-1] = update_encoded
    return Animes

#delete
@app.delete("/AAnimes/{anime_id}", status_code=200)
async def delete_anime(anime_id: int) -> None:
    users.remove(Animes[anime_id-1])
    return Animes 