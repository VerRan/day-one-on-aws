#!/bin/bash

# Run tests for README validation
# 运行README验证测试

echo "🚀 Starting README validation tests..."
echo "开始README验证测试..."

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "✅ Python3 found, running tests..."
    python3 test_readme.py
elif command -v python &> /dev/null; then
    echo "✅ Python found, running tests..."
    python test_readme.py
else
    echo "❌ Python not found. Please install Python to run tests."
    echo "Manual validation checklist:"
    echo "1. Check if readme.md exists"
    echo "2. Check if LICENSE exists"
    echo "3. Verify all sections are present"
    echo "4. Verify all GitHub links are included"
    exit 1
fi

echo ""
echo "📝 Manual verification checklist:"
echo "1. Open readme.md and verify the content is readable"
echo "2. Check that all GitHub links are accessible"
echo "3. Verify bilingual content (Chinese/English)"
echo "4. Confirm project structure makes sense"
echo ""
echo "✨ Test completed!"