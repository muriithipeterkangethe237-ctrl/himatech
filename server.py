from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT = Path(__file__).resolve().parent
FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/styles.css": ("styles.css", "text/css; charset=utf-8"),
    "/script.js": ("script.js", "text/javascript; charset=utf-8"),
    "/assets/logo-transparent.svg": ("assets/logo-transparent.svg", "image/svg+xml"),
    "/assets/RG-ANT13-360-datasheet.pdf": (
        "assets/RG-ANT13-360-datasheet.pdf",
        "application/pdf",
    ),
    "/assets/RG-RAP2260-E-specifications.pdf": (
        "assets/RG-RAP2260-E-specifications.pdf",
        "application/pdf",
    ),
    "/assets/Starlink-Ubiquiti-PowerBeam-guide.pdf": (
        "assets/Starlink-Ubiquiti-PowerBeam-guide.pdf",
        "application/pdf",
    ),
    "/assets/Grandstream-access-points-pricing.pdf": (
        "assets/Grandstream-access-points-pricing.pdf",
        "application/pdf",
    ),
    "/assets/inventory-pricing.pdf": (
        "assets/inventory-pricing.pdf",
        "application/pdf",
    ),
    "/assets/Ruijie-Reyee-routers-specifications.pdf": (
        "assets/Ruijie-Reyee-routers-specifications.pdf",
        "application/pdf",
    ),
    "/assets/Ruijie-Reyee-price-specifications.pdf": (
        "assets/Ruijie-Reyee-price-specifications.pdf",
        "application/pdf",
    ),
    "/assets/RG-AirMetro460G-specifications.pdf": (
        "assets/RG-AirMetro460G-specifications.pdf",
        "application/pdf",
    ),
    "/assets/RG-ANT13-360-Hemitech-datasheet.pdf": (
        "assets/RG-ANT13-360-Hemitech-datasheet.pdf",
        "application/pdf",
    ),
    "/assets/RG-RAP2260-G-specifications.pdf": (
        "assets/RG-RAP2260-G-specifications.pdf",
        "application/pdf",
    ),
    "/assets/RG-RAP2260-H-specifications.pdf": (
        "assets/RG-RAP2260-H-specifications.pdf",
        "application/pdf",
    ),
    "/assets/Hemitech-Grandstream-pricing.pdf": (
        "assets/Hemitech-Grandstream-pricing.pdf",
        "application/pdf",
    ),
    "/assets/Hemitech-Ruijie-router-pricing.pdf": (
        "assets/Hemitech-Ruijie-router-pricing.pdf",
        "application/pdf",
    ),
    "/assets/PowerBeam-5AC-Gen2-specifications.pdf": (
        "assets/PowerBeam-5AC-Gen2-specifications.pdf",
        "application/pdf",
    ),
    "/assets/Rocket-Prism-5AC-Gen2-datasheet.pdf": (
        "assets/Rocket-Prism-5AC-Gen2-datasheet.pdf",
        "application/pdf",
    ),
}


class WebsiteHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requested_file = FILES.get(self.path.split("?", 1)[0])
        if requested_file is None:
            self.send_error(404, "Not found")
            return

        file_path = ROOT / requested_file[0]
        try:
            content = file_path.read_bytes()
        except OSError:
            self.send_error(500, "Unable to read website file")
            return

        self.send_response(200)
        self.send_header("Content-Type", requested_file[1])
        self.send_header("Content-Length", str(len(content)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"Hemitech Kenya website running at http://{address[0]}:{address[1]}")
    try:
        ThreadingHTTPServer(address, WebsiteHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nWebsite server stopped.")
