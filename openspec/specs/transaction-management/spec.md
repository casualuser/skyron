# transaction-management Specification

## Purpose
TBD - created by archiving change wire-existing-capabilities. Update Purpose after archive.
## Requirements
### Requirement: Transaction Creation
The system SHALL allow adding new transactions with a sender, recipient, and amount.

#### Scenario: Transaction added to mempool
- **WHEN** a POST request is made to `/transaction` with valid data
- **THEN** the transaction is added to the pending transactions list

### Requirement: View Pending Transactions
The system SHALL provide an interface to view all transactions awaiting to be mined.

#### Scenario: Retrieve pending transactions
- **WHEN** a GET request is made to `/transaction`
- **THEN** it returns a list of all transactions in the current mempool

