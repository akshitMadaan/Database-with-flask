from flask import Flask, render_template
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    with open('sample.csv') as csv_file:
        data = csv.reader(csv_file, delimiter=',')
        first_line = True
        dataheader=[]
        dataset = []
        for row in data:
            # if first_line:
                dataheader.append({
                "Sr_No": row[0],
                "instrument_token": row[1],
                "exchange_token": row[2],
                "tradingsymbol": row[3],
                "name": row[4],
                "last_price": row[5],
                "expiry": row[6],
                "strike" : row[7],
                "tick_size": row[8],
                "lot_size" :row[9],
                "instrument_type": row[10],
                "segment": row[11],
                "exchange": row[12]
                })
                break
        for row in data:        
            # elif not first_line:
                dataset.append({
                "Sr_No": row[0],
                "instrument_token": row[1],
                "exchange_token": row[2],
                "tradingsymbol": row[3],
                "name": row[4],
                "last_price": row[5],
                "expiry": row[6],
                "strike" : row[7],
                "tick_size": row[8],
                "lot_size" :row[9],
                "instrument_type": row[10],
                "segment": row[11],
                "exchange": row[12]
                })
            # first_line = False
    return render_template("index.html", dataset = dataset, dataheader= dataheader)
    
app.run(debug= True)