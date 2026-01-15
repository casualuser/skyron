# mining-operations Specification

## Purpose
TBD - created by archiving change wire-existing-capabilities. Update Purpose after archive.
## Requirements
### Requirement: Execution of Mining
The system SHALL allow triggering the mining process to find a valid proof and create a new block.

#### Scenario: Block mined successfully
- **WHEN** a POST request is made to `/mine`
- **THEN** the system finds a proof of work, creates a reward transaction, and adds the block to the chain

### Requirement: Miner Rewards
The system MUST reward the miner with 1 credit for every block successfully mined.

#### Scenario: Reward transaction created
- **WHEN** a block is mined
- **THEN** a transaction from "0" to the miner's address with amount 1 is included

