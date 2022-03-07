from __main__ import app
from flask import Flask, jsonify, request
import veri
import fonksiyonlar as f

veri.CrateTable("""
    CREATE TABLE IF NOT EXISTS Yazi (
        YaziID INTEGER PRIMARY KEY AUTOINCREMENT,
        Baslik TEXT NOT NULL,
        AltBaslik TEXT NOT NULL,
        Tag TEXT NOT NULL,
        Icerik TEXT NOT NULL
    )
""")

@app.route('/Yazi', methods=["GET"])
def YaziGetAll():
    db = veri.GetDB()
    cursor = db.cursor()
    query = "SELECT YaziID, Baslik, AltBaslik, Tag, Icerik FROM Yazi"
    cursor.execute(query)
    row_headers = [x[0] for x in cursor.description]
    return f.ResJson(cursor.fetchall(), row_headers)


@app.route("/Yazi/<id>", methods=["GET"])
def YaziGetById(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "SELECT YaziID, Baslik, AltBaslik, Tag, Icerik FROM Yazi WHERE YaziID = ?"
    cursor.execute(statement, [id])
    row_headers = [x[0] for x in cursor.description]
    return f.ResJsonOne(cursor.fetchone(), row_headers)


@app.route("/Yazi", methods=["POST"])
def YaziAdd():
    details = request.get_json()

    Baslik = details["Baslik"]
    AltBaslik = details["AltBaslik"]
    Tag = details["Tag"]
    Icerik = details["Icerik"]
   

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "INSERT INTO Yazi(Baslik, AltBaslik, Tag, Icerik) VALUES (?, ?, ?, ?)"
    cursor.execute(statement, [Baslik, AltBaslik, Tag, Icerik])
    db.commit()
    return jsonify(True)


@app.route("/Yazi", methods=["PUT"])
def YaziSet():
    details = request.get_json()

    YaziID = details["YaziID"]
    Baslik = details["Baslik"]
    AltBaslik = details["AltBaslik"]
    Tag = details["Tag"]
    Icerik = details["Icerik"]

    db = veri.GetDB()
    cursor = db.cursor()
    statement = "UPDATE Yazi SET Baslik = ?, AltBaslik = ?, Tag = ?, Icerik = ? WHERE YaziID = ?"
    cursor.execute(statement, [Baslik, AltBaslik, Tag, Icerik, YaziID])
    db.commit()
    return jsonify(True)


@app.route("/Yazi/<id>", methods=["DELETE"])
def YaziDelete(id):
    db = veri.GetDB()
    cursor = db.cursor()
    statement = "DELETE FROM Yazi WHERE YaziID = ?"
    cursor.execute(statement, [id])
    db.commit()
    return jsonify(True)
