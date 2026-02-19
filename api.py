from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class AddCars(BaseModel):
    id:int
    nomi: str
    modeli: int
    narxi: int
    rasm: str

cars = {
    "car1": {
        "nomi": "Chevrolet Malibu",
        "modeli": "2023",
        "narxi": 32000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/9/9e/Chevrolet_Malibu_2023.jpg"
    },
    "car2": {
        "nomi": "Toyota Camry",
        "modeli": "2022",
        "narxi": 35000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/6/6a/2018_Toyota_Camry_SE.jpg"
    },
    "car3": {
        "nomi": "BMW X5",
        "modeli": "2021",
        "narxi": 60000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/5/5c/2019_BMW_X5_xDrive40i.jpg"
    },
    "car4": {
        "nomi": "Mercedes-Benz C-Class",
        "modeli": "2020",
        "narxi": 55000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/3/33/Mercedes-Benz_C-Class_W205.jpg"
    },
    "car5": {
        "nomi": "Chevrolet Spark",
        "modeli": "2021",
        "narxi": 9000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Chevrolet_Spark_2021.jpg"
    },
    "car6": {
        "nomi": "Chevrolet Cobalt",
        "modeli": "2022",
        "narxi": 13000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/8/8b/Chevrolet_Cobalt_2022.jpg"
    },
    "car7": {
        "nomi": "Chevrolet Tracker",
        "modeli": "2023",
        "narxi": 19000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Chevrolet_Tracker_2021.jpg"
    },
    "car8": {
        "nomi": "Hyundai Elantra",
        "modeli": "2022",
        "narxi": 21000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/2/21/Hyundai_Elantra_2021.jpg"
    },
    "car9": {
        "nomi": "Hyundai Sonata",
        "modeli": "2021",
        "narxi": 27000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/1/1a/2020_Hyundai_Sonata.jpg"
    },
    "car10": {
        "nomi": "Kia K5",
        "modeli": "2022",
        "narxi": 26000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/5/5d/Kia_K5_2021.jpg"
    },
    "car11": {
        "nomi": "Kia Sportage",
        "modeli": "2023",
        "narxi": 29000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Kia_Sportage_2022.jpg"
    },
    "car12": {
        "nomi": "Volkswagen Passat",
        "modeli": "2020",
        "narxi": 30000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/7/7d/VW_Passat_B8.jpg"
    },
    "car13": {
        "nomi": "Volkswagen Polo",
        "modeli": "2021",
        "narxi": 17000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/4/4b/VW_Polo_2018.jpg"
    },
    "car14": {
        "nomi": "Audi A6",
        "modeli": "2021",
        "narxi": 58000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Audi_A6_C8.jpg"
    },
    "car15": {
        "nomi": "Audi Q7",
        "modeli": "2022",
        "narxi": 65000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Audi_Q7_2021.jpg"
    },
    "car16": {
        "nomi": "Nissan Altima",
        "modeli": "2021",
        "narxi": 24000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/6/67/2019_Nissan_Altima.jpg"
    },
    "car17": {
        "nomi": "Nissan X-Trail",
        "modeli": "2022",
        "narxi": 33000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/8/87/Nissan_X-Trail_2021.jpg"
    },
    "car18": {
        "nomi": "Ford Mustang",
        "modeli": "2020",
        "narxi": 45000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/2/2e/Ford_Mustang_2018.jpg"
    },
    "car19": {
        "nomi": "Tesla Model 3",
        "modeli": "2023",
        "narxi": 40000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Tesla_Model_3_2023.jpg"
    },
    "car20": {
        "nomi": "Lexus RX",
        "modeli": "2022",
        "narxi": 62000,
        "rasm": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Lexus_RX_2020.jpg"
    }
}


@app.get("/api")
def get_cars():
    return cars
@app.post("/api/add/{car_id}")
def add_car(car_id: int, car: AddCars):
    cars[car_id] = car.dict()
    return {"message": "Qo'shildi", "car": cars[car_id]}
@app.delete("/api/delete/{car_id}")
def delete_car(car_id: int):
    if car_id in cars:
        del cars[car_id]
        return {"message": "O'chirildi"}
    return {"error": "Topilmadi"}
@app.put("/api/update/{car_id}")
def update_car(car_id: int, car: AddCars):
    if car_id in cars:
        cars[car_id] = car.dict()
        return {"message":"Yangilandi",}
    return {"error":"Topilmadi"}
        


    
