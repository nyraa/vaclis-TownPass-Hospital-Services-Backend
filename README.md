# ParkFlow-backend-Service
ParkFlow is a parking management system designed to enhance parking efficiency by providing real-time data on parking availability, notifications about parking areas, and intelligent Yellow Line parking services.

## Features
1. ***Real-time Data Pipeline***
Fetches real-time data from external sources, such as the Taipei parking API, and processes it to provide users with current parking grid availability.

2. ***Parking Area Notifications***:
Sends notifications to users about parking duration and fees, ensuring they stay informed and avoid penalties.

3. ***Yellow Line Service***:
Assists users with parking near yellow lines based on traffic conditions. During peak hours, the system provides a 3-minute buffer alert for parking time limits. During off-peak hours, it guides users on how to make the most of yellow line parking where permitted.


## Technology Stack

- Framework: FastAPI
- Middleware: CORSMiddleware for cross-origin requests
- External API: Taipei's parking API for real-time parking data
- Geospatial Analysis: geopy library for distance calculations in Yellow Line Service
- Deployment: Uvicorn with SSL support for secure deployment


## Installation
1. Clone the repository:
```bash 
https://github.com/nyraa/vaclis-TownPass-Services-Backend.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables by creating a .env file:
```env
   SSL_KEYFILE=your_ssl_keyfile
   SSL_CERTFILE=your_ssl_certfile
   SSL_PASSWORD=your_ssl_password
```
4. Run the server:
```bash
uvicorn app:app --host 0.0.0.0 --port 25569 --ssl-keyfile $SSL_KEYFILE --ssl-certfile $SSL_CERTFILE --ssl-keyfile-password $SSL_PASSWORD
```


## API Endpoints
- `/`:Fetches and returns real-time data on parking lots and parking grids based on user coordinates (longitude and latitude).
- `/get_line`:Returns nearby yellow line locations within a 1-kilometer radius from the user's coordinates.

## Team Members
- [@vaclisinc](https://www.github.com/vaclisinc)
- [@SimonLiu423](https://www.github.com/SimonLiu423)
- [@nyraa](https://github.com/nyraa)
- [@WavJaby](https://www.github.com/WavJaby)
- [@Andrewtangtang](https://www.github.com/Andrewtangtang) 


<br>

---


Developed with ❤️ by 游松澤 (Yu Song-Ze), 張羿軒 (Zhang Yi-Xuan), 劉力瑋 (Liu Li-Wei), 楊乃昀(Yang Naiyun) ,張昀棠 (Chang Yun-Tang)

Project Team: 嘻嘻的時候，黑客松松澤
