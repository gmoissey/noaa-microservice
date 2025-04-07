import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { WeatherResponse } from "@/types/weather";
import { X } from "lucide-react";
import { Button } from "@/components/ui/button";

type WeatherPopupProps = {
  weatherData: WeatherResponse | null;
  open: boolean;
  onClose?: () => void;
};

function WeatherPopup({ weatherData, open, onClose }: WeatherPopupProps) {
  if (!open) return null;

  return (
    <Card className="w-64 shadow-lg">
      <CardHeader className="pb-2">
        <div className="flex justify-between items-center">
          <CardTitle className="text-sm font-medium">Weather Information</CardTitle>
          {onClose && (
            <Button variant="ghost" size="sm" className="h-6 w-6 p-0" onClick={onClose}>
              <X className="h-4 w-4" />
            </Button>
          )}
        </div>
        {weatherData?.location && (
          <Badge variant="outline" className="text-xs">
            {weatherData.location}
          </Badge>
        )}
      </CardHeader>
      <CardContent className="pt-0">
        {weatherData && (weatherData.forecast?.length > 0) ? (
          <div className="space-y-3">
            {weatherData.forecast.map((forecast, index) => (
              <div key={index} className="bg-slate-50 p-2 rounded-md">
                <div className="flex justify-between items-center mb-1">
                  <span className="font-medium text-xs">{forecast.name}</span>
                  <span className="text-sm font-bold">
                    {forecast.temperature}°{forecast.temperatureUnit}
                  </span>
                </div>
                <p className="text-xs text-slate-600">{forecast.shortForecast}</p>
              </div>
            ))}
          </div>
        ) : (
          <div className="flex items-center justify-center h-16">
            <p className="text-sm text-slate-500">No weather data available</p>
          </div>
        )}
      </CardContent>
    </Card>
  );
}

export default WeatherPopup;