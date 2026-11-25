import json
import sqlite3
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler

localserver_path = Path(__file__).resolve().parent.parent
db_path = localserver_path/"db"/"database.db"

class MyBaseHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/currencies":
            con = sqlite3.connect(db_path)
            cur = con.cursor()
            res = cur.execute("SELECT * FROM Currencies")
            tuples_list = res.fetchall()
            dicts_list = []
            dict_keys = ("id", "code", "name", "sign")
            for tuple in tuples_list:
                current_dict = {}
                for i in range(len(tuple)):
                    current_dict[dict_keys[i]] = tuple[i]
                dicts_list.append(current_dict)
            json_list = json.dumps(dicts_list, ensure_ascii=False)
            self.send_response(200, "OK")
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json_list.encode("utf-8"))
        else:
            test = { "meesage" : "Пока в работе", "status" : False}
            test_string = json.dumps(test, ensure_ascii=False)
            self.send_response(404, "Error")
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(test_string.encode("utf-8"))                
    def do_POST(self):
        length = int(self.headers.get("Content-Length"))
        readed = self.rfile.read(length)
        to_string = readed.decode("utf-8")
        di = json.loads(to_string)
        print(di)
        response = {"message" : "Данные получены", "success" : True}
        response_string = json.dumps(response, ensure_ascii=False)
        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(response_string.encode("utf-8"))


MyHTTPServer = HTTPServer(("127.0.0.1", 8001), MyBaseHTTPRequestHandler)

MyHTTPServer.serve_forever()