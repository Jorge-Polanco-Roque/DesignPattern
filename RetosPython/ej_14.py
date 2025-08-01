from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Geo</title>
</head>
<body>
  <h2>Obtener Geolocalización</h2>
  <button onclick="getLocation()">Detectar ubicación</button>
  <p id="output"></p>
  <script>
    function getLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
          fetch("/coords", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
              latitude: position.coords.latitude,
              longitude: position.coords.longitude
            })
          }).then(res => res.text()).then(data => {
            document.getElementById("output").innerText = data;
          });
        });
      } else {
        document.getElementById("output").innerText = "Geolocalización no disponible.";
      }
    }
  </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/coords', methods=['POST'])
def coords():
    data = request.get_json()
    return f"Tu ubicación: Latitud {data['latitude']}, Longitud {data['longitude']}"

if __name__ == '__main__':
    app.run(debug=True)
