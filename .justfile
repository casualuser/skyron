# Automation Justfile

# Default: list commands
default:
    @just --list

# --- Skyron Commands ---

# Run skyron locally
skyron-run:
    @cd ../skyron && ./venv/bin/python app.py

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

# Run local hardhat node
lottery-node:
    @cd ../lottery && yarn hardhat node

# Lint lottery contracts
lottery-lint:
    cd ../lottery && yarn solhint 'contracts/*.sol'

# Pick a winner for the lottery (local)
lottery-pick-winner:
    @cd ../lottery && yarn hardhat run scripts/pickWinner.ts --network localhost

# Run a full end-to-end raffle cycle (multi-player, pick winner, report)
lottery-full-cycle:
    @cd ../lottery && yarn hardhat run scripts/fullCycleTest.ts --network localhost

# Run the Skyron-Lottery bridge
skyron-bridge:
    @cd ../skyron && ./venv/bin/python bridge.py

# Power down all services
powerdown:
    @echo "🔌 Powering down Postilize services..."
    @-lsof -ti:5000 | xargs kill -9 2>/dev/null || true
    @-lsof -ti:8545 | xargs kill -9 2>/dev/null || true

# Powerup both parts with connection
powerup:
    @just powerdown
    @echo "🚀 Powering up the Postilize ecosystem..."
    @echo "📡 Starting Skyron Blockchain (Port 5000)..."
    @./venv/bin/python app.py > /dev/null 2>&1 & sleep 3
    @echo "🎰 Starting Lottery Node (Port 8545)..."
    @cd ../lottery && yarn hardhat node > /dev/null 2>&1 & sleep 7
    @echo "🌉 Starting Skyron-Lottery Bridge..."
    @./venv/bin/python bridge.py > /dev/null 2>&1 &

# Restart all services
restart:
    @just powerup
