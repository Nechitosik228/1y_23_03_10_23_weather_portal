from .. import app


@app.get("/weather/<city>/<forecast_type>") # /weather/kherson/forecast|weather=weather
def weather(city:str, forecast_type:str="weather"):
    data = make_weather_data(city, forecast_type)
    return jsonify(data)


# @app.route('/get_weather')
# def get_weather():
#    location = request.args.get('location')
#    if location:
#        url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweather_api_key}&units=metric'
#        response = requests.get(url)
#        data = response.json()
#        return jsonify(data)
#    else:
#        return jsonify(error='Location not provided'), 400
   

# # Теперь зробимо роут для погоди на декілька днів
# @app.route('/get_weather_forecast')
# def get_weather_forecast():
#    location = request.args.get('location')
#    if location:
#        url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={openweather_api_key}&units=metric'
#        response = requests.get(url)
#        data = response.json()


#        # get weather info for nearest few days
#        forecast = []
#        print(data)
#        for entry in data['list']:
#            extracted_data = extract_weather_data(entry)
#            forecast.append(extracted_data)
#        return jsonify(forecast)
#    else:
#        return jsonify(error='Location not provided'), 400