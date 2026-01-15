# blockchain-core Specification

## Purpose
TBD - created by archiving change wire-existing-capabilities. Update Purpose after archive.
## Requirements
### Requirement: Block Structure
The system SHALL maintain a list of blocks where each block contains an index, timestamp, list of transactions, proof, and the hash of the previous block.

#### Scenario: Block contains valid headers
- **WHEN** a block is retrieved from the chain
- **THEN** it MUST include index, timestamp, transactions, proof, and previous_hash

### Requirement: Block Hashing
The system MUST use SHA-256 to hash block headers for cryptographic integrity.

#### Scenario: Hash consistency
- **WHEN** a block's content is hashed
- **THEN** it MUST yield a consistent 64-character hex string

### Requirement: Proof of Work
The system SHALL require a valid proof of work (nonce) to accept a new block.

#### Scenario: Verify proof
- **WHEN** the hash of (last_proof, proof) starts with "0000"
- **THEN** the proof is considered valid

