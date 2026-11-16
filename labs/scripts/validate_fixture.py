#!/usr/bin/env python3
"""Validate completely fictional CSV fixture. No external connections, stdlib only."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"
ALLOWED_ACCOUNT_STATUS = {"ACTIVE", "SUSPENDED", "CLOSED"}
ALLOWED_REQUEST_STATUS = {"OPEN", "IN_PROGRESS", "CLOSED"}

def rows(path):
    with Path(path).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))

def validate_data(accounts, customers, members, requests):
    """Return a list of human-readable schema and relationship errors."""
    errors = []
    def unique(table, label, fields):
        seen = set()
        for i, row in enumerate(table, 2):
            key = tuple(row.get(f, "").strip() for f in fields)
            if any(not x for x in key):
                errors.append(f"{label} line {i}: empty key")
            if key in seen:
                errors.append(f"{label} line {i}: duplicate key {key}")
            seen.add(key)
    unique(accounts, "accounts", ["source_system", "account_id"])
    unique(customers, "customers", ["source_system", "customer_id"])
    unique(requests, "requests", ["source_system", "request_id"])
    unique(members, "memberships", ["account_id", "customer_id"])
    account_ids = {a["account_id"] for a in accounts}
    customer_ids = {c["customer_id"] for c in customers}
    for i, acc in enumerate(accounts, 2):
        if acc.get("status") not in ALLOWED_ACCOUNT_STATUS:
            errors.append(f"accounts line {i}: invalid status")
        if not acc.get("source_updated_at", "").endswith("Z"):
            errors.append(f"accounts line {i}: missing UTC timestamp")
    for i, req in enumerate(requests, 2):
        if req.get("account_id") not in account_ids:
            errors.append(f"requests line {i}: orphan account")
        if req.get("status") not in ALLOWED_REQUEST_STATUS:
            errors.append(f"requests line {i}: invalid status")
        if not req.get("updated_at_utc", "").endswith("Z"):
            errors.append(f"requests line {i}: missing UTC timestamp")
    for i, m in enumerate(members, 2):
        if m.get("account_id") not in account_ids:
            errors.append(f"memberships line {i}: orphan account")
        if m.get("customer_id") not in customer_ids:
            errors.append(f"memberships line {i}: orphan customer")
        if m.get("active") not in {"true", "false"}:
            errors.append(f"memberships line {i}: invalid active boolean")
    return errors

def main():
    filenames = ["accounts.csv", "customers.csv", "account_memberships.csv", "service_requests.csv"]
    accounts, customers, members, requests = [rows(DATA / n) for n in filenames]
    errors = validate_data(accounts, customers, members, requests)
    if errors:
        print("Fixture invalid:\n" + "\n".join(errors))
        raise SystemExit(1)
    print(f"PASS: {len(accounts)} accounts, {len(customers)} customers, {len(members)} memberships, {len(requests)} requests; unique keys and relationships valid.")

if __name__ == "__main__":
    main()
