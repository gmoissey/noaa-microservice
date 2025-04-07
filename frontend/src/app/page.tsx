"use client";
import dynamic from 'next/dynamic';
import { getWeatherByLocation } from '@/services/api';
import { useState } from 'react';
import { WeatherResponse } from '@/types/weather';
import WeatherPopup from '@/components/WeatherPopup';
import { RequestsLog } from '@/components/RequestsLog';

const MapWidget = dynamic(() => import('../components/MapWidget'), {
  ssr: false,
});

export default function Home() {
  const [weatherData, setWeatherData] = useState<WeatherResponse | null>();
  const [showPopup, setShowPopup] = useState(true);
  const [updateTrigger, setUpdateTrigger] = useState(0);

  const handleLocationSelect = async (lat: number, lng: number) => {
    try {
      const location = `${lat},${lng}`;
      const data = await getWeatherByLocation(location);
      setWeatherData(data);
      setShowPopup(true);
      setUpdateTrigger((prev) => prev + 1);
    } catch (error) {
      console.error("Error fetching weather:", error);
      setWeatherData({} as WeatherResponse);
      setShowPopup(true);
    }
  };

  return (
    <div style={{ display: "flex", height: "100vh", width: "100vw", position: "relative" }}>
      <div style={{ width: "20%", backgroundColor: "#f0f0f0" }}>
          <RequestsLog updateTrigger={updateTrigger} />
      </div>
      <div style={{ flex: 1 }}>
        <MapWidget onLocationSelect={handleLocationSelect} />
      </div>
      
      {/* Floating weather popup in the lower right corner */}
      <div style={{
        position: "fixed",
        bottom: "20px",
        right: "20px",
        zIndex: 1000,
      }}>
        {weatherData && <WeatherPopup weatherData={weatherData} open={showPopup} />}
      </div>
    </div>
  );
}