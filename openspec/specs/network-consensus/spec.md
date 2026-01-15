# network-consensus Specification

## Purpose
TBD - created by archiving change wire-existing-capabilities. Update Purpose after archive.
## Requirements
### Requirement: Node Registration
The system SHALL support registering neighboring nodes by their network address.

#### Scenario: Add new neighbor
- **WHEN** a POST request is made to `/node` with an address
- **THEN** the address is added to the set of neighboring nodes

### Requirement: Consensus Algorithm
The system SHALL resolve conflicts by replacing its chain with a neighbor's chain if that chain is valid and longer.

#### Scenario: Chain replaced by longer valid chain
- **WHEN** `/consensus` is triggered and a longer valid chain exists in the network
- **THEN** the local chain is replaced by the longest valid neighbor chain

