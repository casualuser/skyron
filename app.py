from argparse import ArgumentParser
import logging
import os
from flask import Flask, jsonify, request
import flask.cli
flask.cli.show_server_banner = lambda *args: None

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Configure file logging for heartbeats
heartbeat_logger = logging.getLogger('heartbeats')
heartbeat_logger.setLevel(logging.INFO)
# Clear existing handlers to avoid duplicates on reload
if heartbeat_logger.hasHandlers():
    heartbeat_logger.handlers.clear()
file_handler = logging.FileHandler('logs/skyron.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
heartbeat_logger.addHandler(file_handler)

# Suppress development headers and heartbeats from the console
class QuietFilter(logging.Filter):
    def filter(self, record):
        msg = record.getMessage()
        # Suppress heartbeats and reroute to file
        if "/chain" in msg:
            heartbeat_logger.info(f"HEARTBEAT: {msg}")
            return False
        # Suppress dev server warnings
        if "development server" in msg or "production deployment" in msg:
            return False
        return True

# Apply filter to werkzeug to silence console spam
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.addFilter(QuietFilter())

from skyron.node import Node
from skyron.miner import Miner
from skyron.blockchain import BlockChain
from skyron.transaction import Transaction

app = Flask('sky-ron')

app.node = Node()
app.miner = Miner(app.node.id)
app.blockchain = BlockChain()


@app.route('/transaction', methods=['POST'])
def add_transaction():
    # data.sender(str)
    # data.recipient(str)
    # data.amount(int)
    data = request.get_json()

    transaction = Transaction.init_from_json(data)

    try:
        next_index = app.blockchain.add_transaction(transaction)
    except Exception as e:
        return jsonify({'message': str(e)}), 403

    response = {'message': f'Transaction will be added to {next_index}th block.'}

    return jsonify(response), 201


@app.route('/transaction', methods=['GET'])
def get_pending_transactions():
    transactions = [t.dump() for t in app.blockchain.transactions]

    return jsonify(transactions), 201


@app.route('/mine', methods=['POST'])
def mine():
    """Mining
    Have to make a standalone process
    But it's just a prototype
    """
    block = app.miner(app.blockchain)

    response = {
        'message': "New block is mined!",
        'block': block.dump()
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def get_full_chain():
    response = {
        'chain': app.blockchain.dump(),
        'length': len(app.blockchain)
    }

    return jsonify(response), 200


@app.route('/node', methods=['GET'])
def get_all_nodes():
    response = {
        'nodes': list(app.node.neighbor),
        'total': len(app.node)
    }

    return jsonify(response), 201


@app.route('/node', methods=['POST'])
def add_node():
    # data.address(str)
    data = request.get_json()

    app.node.add(data['address'])

    response = {
        'message': 'New app.node is added.',
        'total': len(app.node)
    }

    return jsonify(response), 201


@app.route('/chain/valid', methods=['GET'])
def valid_chain():
    valid = app.blockchain.valid()

    response = {'result': valid}

    return jsonify(response), 200


@app.route('/consensus', methods=['POST'])
def consensus():
    new_blockchain = app.node.consensus_with_neighbor(app.blockchain)

    if new_blockchain:
        app.blockchain = new_blockchain
        response = {'message': 'Our chain was replaced.'}
    else:
        response = {'message': 'I\'m King of the World.'}

    return jsonify(response), 200


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--port', default=5000, type=int)
    args = parser.parse_args()

    app.run(port=args.port)
