#!/data/data/com.termux/files/usr/bin/bash
[ -f constants.py ] && [ -f xi.py ] && [ -f test_constants.py ] && [ -f README.md ] && echo "✅ All files present" && echo "▶ Running test_constants.py:" && python test_constants.py && echo "▶ Running xi.py with sample input:" && python xi.py 0.72 0.45
