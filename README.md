RiskPilot

AI Portfolio Risk & Execution Agent for Binance AgentOS

RiskPilot is a risk-first AI portfolio agent designed to inspect a Binance portfolio, identify concentration risk, explain why the risk matters, stress-test the portfolio, propose a controlled rebalance, require user confirmation, and verify the execution result.

«Don't trade first. Understand the risk first.»

---

🚀 What RiskPilot Does

RiskPilot turns a simple trading request into a controlled risk-management workflow:

User Request
     │
     ▼
Portfolio Audit
     │
     ▼
Risk Engine
     │
     ▼
WHY / Explanation
     │
     ▼
Stress Test
     │
     ▼
Rebalance Proposal
     │
     ▼
User Confirmation
     │
     ▼
AgentOS Permission
     │
     ▼
Execution
     │
     ▼
Verification
     │
     ▼
Final Risk Report

The core principle is simple:

Risk assessment comes before execution.

---

🧠 Core Features

1. Risk Audit

RiskPilot evaluates portfolio concentration and identifies the largest position.

Example:

Total Value       : $10,000.00
Largest Position  : BTC
Largest Weight    : 60.00%
Risk Level        : HIGH
Recommended Action: REDUCE_CONCENTRATION

2. WHY Explainability

RiskPilot does not simply return a risk label.

It explains why the portfolio is considered risky:

BTC represents 60.00% of the portfolio.
This exceeds the 50% high-risk concentration limit.

A large allocation to one position can make the
portfolio more vulnerable to a significant loss
if that asset declines.

3. Stress Testing

RiskPilot can simulate portfolio-level market shocks.

Example:

Scenario       : All positions drop 20.0%
Original Value : $10,000.00
Stressed Value : $8,000.00
Potential Loss : $2,000.00

4. Rebalance Proposal

Instead of immediately trading, RiskPilot creates a proposal.

Example:

BTC: 60.00% -> 50.00%
Action: REDUCE
Value Change: -$1,000.00

5. Confirmation Gate

Portfolio-changing actions require explicit user confirmation.

Proposal
   ↓
User Confirmation
   ↓
Execution

RiskPilot never treats a proposal as automatic permission to trade.

6. Execution Safety

The execution layer blocks unconfirmed requests:

Unconfirmed → BLOCKED
Confirmed   → READY

Actual Binance execution is kept separate from the risk and proposal layers.

7. Verification

After execution, RiskPilot compares the expected result with the actual result.

Expected Value : -$1,000.00
Actual Value   : -$1,000.00
Difference     : $0.00
Status         : VERIFIED

This creates a complete control loop:

Assess → Explain → Propose → Confirm → Execute → Verify

---

🔌 Binance AgentOS Integration

RiskPilot is designed to work with Binance AgentOS / MCP.

The AgentOS integration provides access to read-only portfolio and market information such as:

- Spot account balances
- Spot market prices
- Futures positions
- Futures account information
- Wallet information
- Market data

RiskPilot uses an adapter and bridge architecture so that Binance AgentOS responses can be converted into RiskPilot portfolio objects without coupling the risk engine directly to the external tool layer.

Binance AgentOS / MCP
          │
          ▼
    Binance Adapter
          │
          ▼
     AgentOS Bridge
          │
          ▼
      Risk Engine
          │
          ▼
    RiskPilot Decision

Read-only validation

The AgentOS connection has been tested using:

spot.getAccount
spot.tickerPrice

The test account returned an empty Spot portfolio and no trading or account-modifying action was performed.

---

🛡️ Safety Architecture

RiskPilot uses multiple independent safety layers.

┌─────────────────────────────┐
│       User Request          │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│       Risk Assessment       │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│      Risk Explanation       │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│     Rebalance Proposal      │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│      User Confirmation      │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│     AgentOS Permission      │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│          Execute            │
└──────────────┬──────────────┘
               ▼
┌─────────────────────────────┐
│          Verify             │
└─────────────────────────────┘

This separation helps prevent an AI recommendation from becoming an unintended trade.

---

🏗️ Architecture

app/riskpilot/
│
├── risk/
│   ├── portfolio.py
│   ├── risk_limits.py
│   ├── engine.py
│   └── policy.py
│
├── binance/
│   └── adapter.py
│
├── audit/
│   └── auditor.py
│
├── stress/
│   └── stress_test.py
│
├── rebalance/
│   └── proposal.py
│
├── confirmation/
│   └── gate.py
│
├── execution/
│   └── executor.py
│
├── verification/
│   └── verifier.py
│
├── agentos/
│   └── bridge.py
│
├── report/
│   └── formatter.py
│
├── why/
│   └── explainer.py
│
└── demo/
    └── run_demo.py

---

⚙️ Risk Model

The current MVP uses deterministic concentration thresholds:

Largest Position| Risk Level| Action
"< 30%"| LOW| "NO_ACTION"
"30% - <50%"| MEDIUM| "MONITOR"
"≥ 50%"| HIGH| "REDUCE_CONCENTRATION"

The deterministic risk engine is intentionally separated from the AI layer.

This means the AI can explain and orchestrate decisions without being the sole authority for the underlying risk calculation.

---

🧪 Demo

Run the local RiskPilot demo:

PYTHONPATH=app python -m riskpilot.demo.run_demo

The demo demonstrates:

1. Portfolio risk audit
2. 20% stress test
3. Rebalance proposal
4. Confirmation gate
5. Dry-run execution
6. Execution verification

Expected result:

=== RiskPilot Demo ===

[1] RISK AUDIT
Total value: $10,000.00
Largest position: BTC
Largest weight: 60.00%
Concentration risk: HIGH
Action: REDUCE_CONCENTRATION

[2] STRESS TEST
Scenario: All positions drop 20.0%
Original value: $10,000.00
Stressed value: $8,000.00
Loss: $2,000.00

[3] REBALANCE PROPOSAL
BTC: 60.00% -> 50.00%

[4] CONFIRMATION GATE
Confirmed: False
Confirmed: True

[5] EXECUTION
Status: READY

[6] VERIFICATION
Status: VERIFIED

=== Demo Complete ===

---

🧪 Testing

RiskPilot uses Python's built-in "unittest" framework.

Run the complete test suite:

PYTHONPATH=app python -m unittest discover -s tests -v

The current implementation contains comprehensive tests covering:

- Risk engine
- Risk policy
- System prompt
- Binance adapter
- Portfolio audit
- Stress testing
- Rebalance proposals
- Confirmation gate
- Execution
- Verification
- AgentOS bridge
- Report formatting
- WHY explainability

---

🔐 Execution Philosophy

RiskPilot follows three principles:

1. Explain before acting

The system should explain the risk before proposing a portfolio-changing action.

2. Confirm before executing

A proposal is not permission.

User confirmation is required before execution.

3. Verify after executing

An execution result should be checked against the expected outcome.

---

🎯 Why RiskPilot?

Many trading agents focus on:

«"What should I trade?"»

RiskPilot focuses on:

«"What is the risk of my current portfolio, why does it matter, and what should happen before I trade?"»

The goal is not to replace the trader.

The goal is to give the trader a risk-aware control layer between intent and execution.

---

🛣️ Roadmap

Future versions can extend RiskPilot with:

- Multi-asset risk scoring
- Volatility-aware position limits
- Correlation analysis
- Drawdown monitoring
- Liquidity-aware execution
- Slippage estimation
- Futures leverage risk
- Portfolio-level VaR
- Automated monitoring
- More advanced AgentOS execution
- Historical risk analytics

---

⚠️ Current Scope

This project is an MVP / competition prototype.

The current risk model focuses primarily on portfolio concentration. It is not intended to represent a complete institutional risk-management system.

Execution integration is deliberately separated from the deterministic risk engine and currently uses a controlled interface/dry-run architecture.

---

🏁 Project Status

RiskPilot — Phase 16 / Final MVP

Core pipeline implemented:

Risk
→ Policy
→ Audit
→ Stress Test
→ WHY
→ Proposal
→ Confirmation
→ Execution
→ Verification
→ AgentOS Bridge
→ Report

The project is designed around one principle:

Risk first. Execute second.
