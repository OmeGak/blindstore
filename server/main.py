import base64
import json

from flask import Flask, request
import numpy as np
from scarab import EncryptedArray, PublicKey

from .store import Store
from common.utils import binary


app = Flask(__name__)

store = Store(database=np.array([[1, 1, 1, 1],
                                 [1, 1, 1, 0],
                                 [1, 1, 0, 0],
                                 [1, 0, 0, 0]]))


@app.route('/db_size')
def get_db_size():
    data = {
        'num_records': store.record_count,
        'record_size': store.record_size,
        'index_length': store.index_length
    }
    return json.dumps(data), 200, {'Content-Type': 'text/json'}


@app.route('/retrieve', methods=['POST'])
def retrieve():
    print("Starting retrieve call...")
    public_key = PublicKey(str(request.form['PUBLIC_KEY']))

    enc_index = EncryptedArray(store.index_length, public_key, request.form['ENC_INDEX'])
    try:
        enc_data = store.retrieve(enc_index, public_key)
    except ValueError as e:
        print(str(e))
        return str(e), 400

    s_bits = [str(b) for b in enc_data]
    obj = json.dumps(s_bits)

    return obj


@app.route('/set', methods=['POST'])
def set():
    index = int(request.form['INDEX'])
    data = int.from_bytes(base64.b64decode(request.form['DATA']), 'big')

    store.set(index, binary(data, store.record_size))
    return '', 200
