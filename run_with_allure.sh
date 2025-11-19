#!/bin/bash

# Simple script to run tests and generate Allure report

echo "Running tests..."
pytest

if [ $? -eq 0 ]; then
    echo "✓ Tests completed successfully!"
else
    echo "✗ Some tests failed"
fi

echo ""
echo "Generating Allure report..."

if command -v allure &> /dev/null; then
    allure serve allure-results
else
    echo "⚠ Allure command-line tool not found!"
    echo "Please install it:"
    echo "  macOS:   brew install allure"
    echo "  Linux:   Download from https://github.com/allure-framework/allure2/releases"
    echo "  Windows: scoop install allure"
    echo ""
    echo "Test results are saved in: allure-results/"
fi

