from flask import Flask, jsonify, request
# from flask_cors import CORS
from blockchain import Blockchain
from argparse import ArgumentParser

app = Flask(__name__)
# CORS(app)


@app.route('/', methods=['GET'])
def chian():
    chain = test.chain
    dictChain = [block.__dict__.copy() for block in chain]
    for dictBlock in dictChain:
        dictBlock['transactions'] = [tx.__dict__ for tx in dictBlock['transactions']]
    return jsonify(dictChain), 200


@app.route('/mine', methods=['POST'])
def mine():
    last_block = blockchain.last_block
        last_proof = last_block['proof']
        proof = blockchain.proof_of_work(last_proof)
        blockchain.new_transaction(
            sender="0",
            recipient=node_identifier,
            amount=1,
        )
        previous_hash = blockchain.hash(last_block)
        block = blockchain.new_block(proof, previous_hash)
response = {
            'message': "New Block Created",
            'index': block['index'],
            'transactions': block['transactions'],
            'proof': block['proof'],
            'previous_hash': block['previous_hash'],
        }
        return jsonify(response), 200

@app.route('/opentxs', methods=['GET'])
def opentxs():
    """ get the unconfirmed transactions or any transaction has not been included in a block """
    pass
txs = test.unconfirmed
    if txs != None:
        dictTx = [tx.__dict__ for tx in txs]
        res = 
        {
            'Transaction': dictTx;
        }
        return jsonify(res), 200
    else:
        res = 
        {
            "Message" = 'There are no transaction'
        }
        return jsonify(res), 500
        

@app.route('/sendtx', methods=['POST'])
def sendtx():
    """ send a transaction"""
    pass
    values = request.get_json()
    if not values:
        res =
        {
            "Message": 'There are no Transaction'
        }
        return jsonify(res), 500

        reqkeys = ['sender', 'receiver', 'amount']
        if not all (key in values in reqkeys)
        res = 
        {
            "Message" = 'There are missing value'
        }
        return jsonify(res), 400

    sender = values['sender']
    receiver = values['receiver']
    amount = values['amount']
    addTx = test.addTransaction(sender,receiver,amount)
    if addTx !=None:
        res = 
        {
            'Transaction':{
                'sender': values['sender']
                'receiver': values['receiver']
                'amount': values['amount']
            }
        }   
        return jsonify(res), 200
        else:
            res = {
                'Message': 'The transaction does not pass'
            }
            return jsonify(res), 200


if __name__ == '__main__':
    ser = ArgumentParser()
    ser.add_argument('-p', '--port', default=8020)
    args = ser.parse_args()
    port = args.port
    test = Blockchain()
    app.run(debug=True, port=port)
