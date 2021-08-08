#HEADER
from flask import Flask, request, json, jsonify
import os
import random, string
app = Flask(__name__)


@app.route('/')
def api_root():
        return 'Welcome guys'

@app.route('/webhook', methods=['POST'])
def webhook():
    webhook_message = json.loads(request.data)
    raw_message = json.dumps(request.json)
    price = webhook_message['orderID'] 
    ordertype = webhook_message['orderLabel'] 
    
    print (raw_message)
    print (price)
    print (ordertype)

    return webhook_message


#FOOTER
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)