#!/usr/bin/env python3
import sys
import datetime

if len(sys.argv) < 2:
    print("Usage: ./deploy_check.py <environment>")
    print("Example: ./deploy_check.py staging")
    sys.exit(1)

environment = sys.argv[1]

print("=== Deploy Check ===")
print(f"Environment: {environment}")
print(f"Date:        {datetime.date.today()}")
print(f"Python:      {sys.version.split()[0]}")
