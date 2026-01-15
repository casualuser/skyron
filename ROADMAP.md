# Skyron Roadmap

## 🛠️ Technical Enhancements

### 1. Core Blockchain Integrity
- **Persistent Storage**: Move from in-memory/JSON storage to a robust SQLite backend for transactional data and chain history.
- **Wallet Implementation**: Introduce RSA/ECC-based transaction signing and public/private key pairs for user accounts.
- **Advanced Consensus**: Transition from simple Proof of Work to a hybrid model or optimize the difficulty adjustment algorithm.

### 2. Network & Scalability
- **Dynamic Peer Discovery**: Implement a gossip protocol for nodes to discover neighbors automatically instead of manual registration.
- **Mempool Optimization**: Improve the handling of pending transactions and prioritize those with higher optional "fees".

### 3. Developer Experience
- **Client SDK**: Create a lightweight Python/TypeScript library to interact with the Skyron API easily.
- **Enhanced OpenSpec Integration**: Automate the generation of API documentation from the code using the OpenSpec scaffolding.

## 🔗 Mutual Integration with Lottery

### 1. Raffle-as-a-Service (RaaS)
- **Native Raffle Support**: Implement a specific transaction type or "smart script" layer in Skyron that natively supports draws, using the Lottery contract's logic as a design template.
- **Proof-of-Donation**: Enable Skyron nodes to verify donations made in the `CharityRaffle` contract to unlock specific network privileges or miner rewards on Skyron.

### 2. Decentralized Entropy
- **Shared Entropy Pool**: Use Skyron's Proof of Work solutions as an additional source of entropy for off-chain oracular inputs that the Lottery contract can consume.
