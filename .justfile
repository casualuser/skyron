# Automation Justfile

# Default: list commands
default:
    @just --list

# --- Skyron Commands ---

# Run skyron locally
skyron-run:
    cd ../skyron && ./venv/bin/python app.py

# Add a sample transaction to skyron
skyron-tx sender recipient amount:
    curl -X POST -H "Content-Type: application/json" -d '{"sender": "{{sender}}", "recipient": "{{recipient}}", "amount": {{amount}}}' http://127.0.0.1:5000/transaction

# Mine a block in skyron
skyron-mine:
    curl -X POST http://127.0.0.1:5000/mine

# View full blockchain
skyron-chain:
    curl -s http://127.0.0.1:5000/chain

# Check chain validity
skyron-valid:
    curl -s http://127.0.0.1:5000/chain/valid

# --- Lottery Commands ---

# Run lottery tests
lottery-test:
    cd ../lottery && yarn hardhat test

# Deploy lottery raffle
lottery-deploy:
    cd ../lottery && yarn hardhat deploy --tags raffle

# Lint lottery contracts
lottery-lint:
    cd ../lottery && yarn solhint 'contracts/*.sol'
