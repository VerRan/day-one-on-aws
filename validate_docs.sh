#!/bin/bash

# Simple documentation validation script
# 简单的文档验证脚本

echo "📋 Validating documentation structure..."
echo "验证文档结构..."
echo "=================================="

# Check if readme.md exists
if [ -f "readme.md" ]; then
    echo "✅ readme.md exists"
else
    echo "❌ readme.md not found"
    exit 1
fi

# Check if LICENSE exists
if [ -f "LICENSE" ]; then
    echo "✅ LICENSE file exists"
else
    echo "❌ LICENSE file not found"
fi

# Check for key sections in README
echo ""
echo "🔍 Checking README sections..."

sections=(
    "项目解读"
    "项目概述"
    "项目结构"
    "机器学习"
    "大数据"
    "开发运维"
    "无服务器架构"
    "快速开始"
    "学习路径建议"
    "贡献指南"
    "许可证"
    "联系方式"
)

for section in "${sections[@]}"; do
    if grep -q "$section" readme.md; then
        echo "✅ Section found: $section"
    else
        echo "❌ Section missing: $section"
    fi
done

# Check for GitHub links
echo ""
echo "🔗 Checking GitHub links..."

links=(
    "ml-on-aws"
    "bigdata-on-aws"
    "devops"
    "cloud_university"
    "farget-log-collect-demo"
    "ivs-vod-merge"
    "serverless-workshop"
    "lamabda-image-demo"
    "image-serverless-java"
    "lambda-pc-test"
)

for link in "${links[@]}"; do
    if grep -q "$link" readme.md; then
        echo "✅ Link found: $link"
    else
        echo "❌ Link missing: $link"
    fi
done

# Check for badges
echo ""
echo "🏷️  Checking badges..."
if grep -q "!\[AWS\]" readme.md; then
    echo "✅ AWS badge found"
else
    echo "❌ AWS badge missing"
fi

if grep -q "!\[Learning\]" readme.md; then
    echo "✅ Learning badge found"
else
    echo "❌ Learning badge missing"
fi

if grep -q "!\[Open Source\]" readme.md; then
    echo "✅ Open Source badge found"
else
    echo "❌ Open Source badge missing"
fi

# Check for bilingual content
echo ""
echo "🌐 Checking bilingual content..."
if grep -q "Project Overview" readme.md && grep -q "项目概述" readme.md; then
    echo "✅ Bilingual content (Chinese/English) found"
else
    echo "❌ Bilingual content incomplete"
fi

echo ""
echo "📊 Validation completed!"
echo "验证完成！"