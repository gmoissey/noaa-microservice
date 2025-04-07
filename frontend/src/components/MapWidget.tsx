"use client";

import { MapContainer, TileLayer, Marker, Popup, useMapEvents } from 'react-leaflet';
import { LatLngExpression } from 'leaflet';
import { useState } from 'react';
import L from "leaflet";
import 'leaflet/dist/leaflet.css';

delete (L.Icon.Default.prototype as any)._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
    iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
    shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
    });

interface MapProps {
    onLocationSelect: (lat: number, lng: number) => void;
  }

export default function MapWidget({ onLocationSelect }: MapProps) {
    const [position, setPosition] = useState<LatLngExpression>([39, -96]);
    const [showMarker, setShowMarker] = useState(false);

    const MapEvents = () => {
        useMapEvents({
        click(e) {
            const { lat, lng } = e.latlng;
            setPosition([lat, lng]);
            onLocationSelect(lat, lng);
            setShowMarker(true);
        },
        });
        return null;
    };

    return (
        <MapContainer
            center={[37.0902, -95.7129]} // Center of the US
            zoom={5}
            style={{ height: "100vh", width: "100%" }}
            >
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
            <MapEvents />
            {position && showMarker && <Marker position={position} />}
        </MapContainer>
    );
}