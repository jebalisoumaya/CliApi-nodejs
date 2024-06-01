from flask import Flask, jsonify, request
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
try:
    stores_df = pd.read_excel(r'c:\Users\SOUMAYA\Desktop\DataPlus\shops_df.xlsx' )
    events_df = pd.read_excel(r'c:\Users\SOUMAYA\Desktop\DataPlus\events_df.xlsx')
except Exception as e:
    print("Error loading data:", str(e))

@app.route('/search', methods=['GET'])
def search():
    try:
        address = request.args.get('address')

        nearby_stores = stores_df[stores_df['address'] == address].to_dict(orient='records')
        nearby_events = events_df[events_df['address'] == address].to_dict(orient='records')

        return jsonify({'shops': nearby_stores, 'events': nearby_events})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

    
