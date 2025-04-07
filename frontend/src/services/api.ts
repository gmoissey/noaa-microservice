import axios from "axios";
import { WeatherResponse, WeatherRequest } from "../types/weather";

const API_BASE_URL = "http://127.0.0.1:5001/weather-api";

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000, // 10 seconds timeout
});

export const getWeatherByLocation = async (location: string): Promise<WeatherResponse> => {
  try {
    const response = await apiClient.get<WeatherResponse>(`/location/${location}`);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response) {
        // Server responded with an error status (4xx, 5xx)
        console.error(`Weather API error (${error.response.status}):`, error.response.data);
        
        // Return a valid but empty weather response instead of throwing
        return {
          forecast: [],
          location: location
        };
      } else if (error.request) {
        // Request was made but no response received
        console.error("Weather API no response:", error.message);
      } else {
        // Something happened in setting up the request
        console.error("Weather API request setup error:", error.message);
      }
    } else {
      // Handle non-Axios errors
      console.error("Weather API unexpected error:", error);
    }
    
    // Return an empty but valid response object instead of throwing
    return {
      forecast: [],
      location: location
    };
  }
};

export const getRequestHistory = async (limit: number = 10): Promise<WeatherRequest[]> => {
  try {
    const response = await apiClient.get<{ requests: WeatherRequest[] }>(`/requests`, {
      params: { limit },
    });
    return response.data.requests;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      if (error.response) {
        console.error(`Request history API error (${error.response.status}):`, error.response.data);
      } else if (error.request) {
        console.error("Request history API no response:", error.message);
      } else {
        console.error("Request history API request setup error:", error.message);
      }
    } else {
      console.error("Request history API unexpected error:", error);
    }
    
    return [];
  }
};

apiClient.interceptors.response.use(
  response => response,
  error => {
    return Promise.reject(error);
  }
);