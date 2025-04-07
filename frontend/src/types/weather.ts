export interface Forecast {
    name: string;
    shortForecast: string;
    temperature: number;
    temperatureUnit: string;
  }
  
export interface WeatherResponse {
    forecast: Forecast[];
    location: string;
  }
  
export interface WeatherRequest {
    error: string | null;
    location: string;
    response: WeatherResponse;
    status: number;
    timestamp: string;
  }
  
export interface WeatherData {
    requests: WeatherRequest[];
  }
  