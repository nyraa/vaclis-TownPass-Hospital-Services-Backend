from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import requests
import uvicorn

headers = {"Content-Type": "application/x-www-form-urlencoded"}
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(lon: float, lat: float):
    print(lon, lat)
    response = requests.post(
        "https://itaipeiparking.pma.gov.taipei/MapAPI/GetAllPOIData",
        data={"lon": lon, "lat": lat, "catagory": "car", "type": 1},
        headers=headers,
    )
    data = response.json()
    parkingLot = []
    parkingGrid = []
    for i in data:
        if i["wkt"] is None:
            parkingLot.append(
                {
                    "parkId": i["parkId"],
                    "parkName": i["parkName"],
                    "lon": i["lon"],
                    "lat": i["lat"],
                    "carTotalNum": i["carTotalNum"],
                    "carRemainderNum": i["carRemainderNum"],
                    "payex": i["payex"],
                    "chargeStationTotalNum": i["chargeStationTotalNum"],
                    # "entrance": json.loads(i["entrance"]) if i["entrance"] is not None else None,
                }
            )
        else:
            if i["remark"] != "目前空格" and i["remark"] != "目前有車停放":
                print(i["remark"])
            parkingGrid.append(
                {
                    "parkId": i["parkId"],
                    "parkName": i["parkName"],
                    "lon": i["lon"],
                    "lat": i["lat"],
                    "available": i["remark"] == "目前空格",
                    "payex": i["payex"],
                    "chargeStationTotalNum": i["chargeStationTotalNum"],
                    # "entrance": json.loads(i["entrance"]) if i["entrance"] is not None else None,
                    "wkt": list(map(strToCord, i["wkt"][10:-2].split(", "))),
                }
            )
    return {"parkingLot": parkingLot, "parkingGrid": parkingGrid}

def strToCord(string):
    string = string.split(" ")
    return (float(string[0]),float(string[1]))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
