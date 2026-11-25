    def do_GET(self):
        test = { "meesage" : "Привет", "status" : True}
        test_string = json.dumps(test, ensure_ascii=False)
        self.send_response(200, "OK")
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



MyHTTPServer.serve_forever()




con = sqlite3.connect(db_path)
cur = con.cursor()
res = cur.execute("SELECT * FROM Currencies")
print(res.fetchall())