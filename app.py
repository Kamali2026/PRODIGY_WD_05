from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
api_key = "64639cc1136c59e142dd9947abc02826"

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/weather', methods=['POST'])
def get_weather():
    # Get location from form input
    location = request.form['location']

    # API request to OpenWeatherMap
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        # Extract relevant weather information
        weather_description = weather_data['weather'][0]['description'].capitalize()
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        humidity = weather_data['main']['humidity']

        # Render weather template with weather details
        return render_template('weather.html', location=location, weather=weather_description,
                               temperature=temperature_celsius, humidity=humidity)
    else:
        return render_template('error.html', message="Location not found")

if __name__ == '__main__':
    app.run(debug=True)