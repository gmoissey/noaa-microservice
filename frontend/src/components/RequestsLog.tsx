"use client";

import { useEffect, useState } from "react";
import { WeatherRequest } from "@/types/weather";
import { getRequestHistory } from "@/services/api";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Skeleton } from "@/components/ui/skeleton";
import { CalendarIcon, MapPinIcon, ThermometerIcon } from "lucide-react";

type RequestsLogProps = {
  updateTrigger: number;
};

export function RequestsLog({ updateTrigger }: RequestsLogProps) {
  const [requests, setRequests] = useState<WeatherRequest[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchRequests = async () => {
      try {
        const data = await getRequestHistory();
        setRequests(data);
      } catch (error) {
        console.error("Error fetching requests:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchRequests();
  }, [updateTrigger]);

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  const getStatusColor = (status: number) => {
    if (status >= 200 && status < 300) return "bg-green-100 text-green-800";
    if (status >= 400 && status < 500) return "bg-yellow-100 text-yellow-800";
    if (status >= 500) return "bg-red-100 text-red-800";
    return "bg-gray-100 text-gray-800";
  };

  return (
    <Card className="h-full border-0 shadow-none">
        <CardHeader className="px-2 py-2 border-b">
            <CardTitle className="text-2xl font-bold">Request History</CardTitle>
        </CardHeader>
        <ScrollArea className="h-[calc(100vh-8rem)]">
        <CardContent className="p-0">
          {loading ? (
            <div className="space-y-3 p-4">
              {[1, 2, 3].map((i) => (
                <div key={i} className="space-y-2">
                  <Skeleton className="h-4 w-3/4" />
                  <Skeleton className="h-4 w-1/2" />
                </div>
              ))}
            </div>
          ) : requests.length > 0 ? (
            <div className="divide-y">
              {requests.map((request, index) => (
                <div key={index} className="p-3 hover:bg-slate-50">
                  <div className="flex justify-between items-center mb-1">
                    <div className="flex items-center gap-1 text-xs text-slate-500">
                      <CalendarIcon className="h-3 w-3" />
                      <span>{formatTimestamp(request.timestamp)}</span>
                    </div>
                    <Badge className={getStatusColor(request.status)} variant="outline">
                      {request.status}
                    </Badge>
                  </div>
                  
                  <div className="flex items-center gap-1 text-xs mb-2">
                    <MapPinIcon className="h-3 w-3 text-slate-400" />
                    <span className="font-medium">{request.location}</span>
                  </div>
                  
                  {request.error && (
                    <div className="text-xs text-red-600 bg-red-50 p-2 rounded mt-1">
                      {request.error}
                    </div>
                  )}
                  
                  {request.response && request.response.forecast && (
                    <div className="mt-2 space-y-1">
                      <div className="text-xs text-slate-500">Forecast summary:</div>
                      {request.response.forecast.slice(0, 1).map((forecast, i) => (
                        <div key={i} className="flex items-center gap-2 text-xs bg-slate-50 p-1 rounded">
                          <ThermometerIcon className="h-3 w-3 text-slate-400" />
                          <span>{forecast.shortForecast}, </span>
                          <span className="font-medium">{forecast.temperature}°{forecast.temperatureUnit}</span>
                        </div>
                      ))}
                      {request.response.forecast.length > 1 && (
                        <div className="text-xs text-slate-400">
                          +{request.response.forecast.length - 1} more periods
                        </div>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <div className="flex items-center justify-center h-32">
              <p className="text-sm text-slate-500">No requests found</p>
            </div>
          )}
        </CardContent>
      </ScrollArea>
    </Card>
  );
}