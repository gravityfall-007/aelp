import { MapContainer, TileLayer, Marker } from "react-leaflet";
import "leaflet/dist/leaflet.css";

export default function MapView() {
  return (
    <div style={{ height: "100vh" }}>
      <MapContainer center={[48.13, 11.58]} zoom={12} style={{ height: "100%" }}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <Marker position={[48.13, 11.58]} />
      </MapContainer>
    </div>
  );
}