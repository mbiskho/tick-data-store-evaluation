# Tick Data Store Evaluation

A reproducible comparison template for storage footprint, write/read throughput, query tail latency, index-build time, and integrity across three illustrative backend profiles.

Run `python3 run.py` to write `reports/metrics.json`; `python3 ../run_all.py` from the portfolio root refreshes the overview and workflow images.

![Tick-store comparison overview](reports/project-overview.png)

![Tick-data evaluation flow](reports/project-flow.png)

The backend profiles are explicitly illustrative, not measured database results. Replace them with controlled tests on representative hardware and data before making a storage decision.
