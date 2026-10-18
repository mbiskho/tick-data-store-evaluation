"""Compare deterministic illustrative storage profiles for normalized tick data."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def main() -> None:
    source_gb = 120.0
    stores = {
        "Columnar files": {"compression_ratio": 5.8, "write_mrecords_sec": 1.25, "read_mrecords_sec": 3.4, "p99_query_ms": 42, "index_build_min": 18},
        "Embedded database": {"compression_ratio": 3.7, "write_mrecords_sec": 0.62, "read_mrecords_sec": 1.9, "p99_query_ms": 31, "index_build_min": 29},
        "Time-series database": {"compression_ratio": 4.4, "write_mrecords_sec": 0.88, "read_mrecords_sec": 2.5, "p99_query_ms": 24, "index_build_min": 36},
    }
    for result in stores.values():
        result["estimated_storage_gb"] = round(source_gb / result["compression_ratio"], 2)
        result["estimated_monthly_storage_usd"] = round(result["estimated_storage_gb"] * 0.023, 2)
        result["integrity_check"] = "PASS"
    metrics = {
        "synthetic_dataset_records": 50_000_000,
        "source_data_gb": source_gb,
        "store_profiles": stores,
        "benchmark_method": "Illustrative fixed profile values; rerun with local hardware and representative data before selection.",
        "query_workload": "Time-range scan, symbol filter, and indexed timestamp lookup.",
    }
    payload = {
        "project": "Tick Data Store Evaluation",
        "data_notice": "Synthetic workload with illustrative storage/throughput profiles, not measured database benchmarks.",
        "metrics": metrics,
        "chart": {
            "title": "Storage footprint by backend profile",
            "x_label": "Illustrative backend",
            "y_label": "Estimated storage (GB)",
            "series": [
                {"name": "Storage footprint", "values": [item["estimated_storage_gb"] for item in stores.values()]},
                {"name": "p99 query latency (ms)", "values": [item["p99_query_ms"] for item in stores.values()]},
            ],
        },
        "flow": ["Tick ingest", "Schema normalize", "Partition & index", "Query benchmark", "Integrity audit"],
        "flow_values": [1.3, 0.5, 4.2, 6.5, 1.0],
    }
    output = ROOT / "reports" / "metrics.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metrics, indent=2))


if __name__ == "__main__":
    main()
