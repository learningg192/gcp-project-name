from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from db import get_conn

app = Flask(__name__, static_folder="/app/frontend", static_url_path="")
CORS(app)

@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO team_tble(name, city) VALUES (%s, %s)",
            (data['name'], data['city'])
        )
        conn.commit()
        return jsonify({"msg": "Inserted"})
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)})
    finally:
        cur.close()
        conn.close()

@app.route('/get', methods=['GET'])
def get_data():
    conn = get_conn()
    cur = conn.cursor()
    try:
        cur.execute("SELECT name, city FROM team_tble")
        rows = cur.fetchall()
        return jsonify([
            {"name": r[0], "city": r[1]} for r in rows
        ])
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)})
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)