#!/usr/bin/env python3
"""
Test script to validate the README.md structure and content
测试脚本用于验证README.md的结构和内容
"""

import re
import os
import sys

def test_readme_structure():
    """Test the README.md file structure and content"""
    
    # Check if README.md exists
    readme_path = "readme.md"
    if not os.path.exists(readme_path):
        print("❌ README.md file not found")
        return False
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Test cases
    tests = [
        {
            'name': 'Title contains project interpretation (项目解读)',
            'pattern': r'# Day One On AWS - 项目解读',
            'required': True
        },
        {
            'name': 'Contains project overview section',
            'pattern': r'## 📖 项目概述 \| Project Overview',
            'required': True
        },
        {
            'name': 'Contains project structure section',
            'pattern': r'## 🏗️ 项目结构 \| Project Structure',
            'required': True
        },
        {
            'name': 'Contains ML on AWS section',
            'pattern': r'## 🤖 机器学习 \| ML on AWS',
            'required': True
        },
        {
            'name': 'Contains Big Data section',
            'pattern': r'## 📊 大数据 \| Big Data on AWS',
            'required': True
        },
        {
            'name': 'Contains DevOps section',
            'pattern': r'## 🔧 开发运维 \| DevOps on AWS',
            'required': True
        },
        {
            'name': 'Contains Serverless section',
            'pattern': r'## ⚡ 无服务器架构 \| Serverless on AWS',
            'required': True
        },
        {
            'name': 'Contains Quick Start section',
            'pattern': r'## 🚀 快速开始 \| Quick Start',
            'required': True
        },
        {
            'name': 'Contains Learning Path section',
            'pattern': r'## 📚 学习路径建议 \| Learning Path',
            'required': True
        },
        {
            'name': 'Contains Contributing section',
            'pattern': r'## 🤝 贡献指南 \| Contributing',
            'required': True
        },
        {
            'name': 'Contains License section',
            'pattern': r'## 📄 许可证 \| License',
            'required': True
        },
        {
            'name': 'Contains Contact section',
            'pattern': r'## 📞 联系方式 \| Contact',
            'required': True
        }
    ]
    
    # Test GitHub links
    github_links = [
        'https://github.com/VerRan/ml-on-aws/',
        'https://github.com/VerRan/bigdata-on-aws',
        'https://github.com/VerRan/devops',
        'https://github.com/VerRan/cloud_university',
        'https://github.com/VerRan/farget-log-collect-demo',
        'https://github.com/VerRan/ivs-vod-merge',
        'https://github.com/VerRan/serverless-workshop',
        'https://github.com/VerRan/lamabda-image-demo',
        'https://github.com/VerRan/image-serverless-java',
        'https://github.com/VerRan/lambda-pc-test'
    ]
    
    results = []
    
    # Test structure
    for test in tests:
        if re.search(test['pattern'], content):
            results.append(f"✅ {test['name']}")
        else:
            results.append(f"❌ {test['name']}")
    
    # Test GitHub links
    for link in github_links:
        if link in content:
            results.append(f"✅ GitHub link found: {link}")
        else:
            results.append(f"❌ GitHub link missing: {link}")
    
    # Test badges
    badge_patterns = [
        r'!\[AWS\]',
        r'!\[Learning\]',
        r'!\[Open Source\]'
    ]
    
    for pattern in badge_patterns:
        if re.search(pattern, content):
            results.append(f"✅ Badge found: {pattern}")
        else:
            results.append(f"❌ Badge missing: {pattern}")
    
    # Test bilingual content (Chinese and English)
    if '项目概述' in content and 'Project Overview' in content:
        results.append("✅ Bilingual content (Chinese/English) found")
    else:
        results.append("❌ Bilingual content missing")
    
    # Test emojis in headers
    emoji_count = len(re.findall(r'## [📖🏗️🤖📊🔧⚡🚀📚🤝📄📞🙏]', content))
    if emoji_count >= 10:
        results.append(f"✅ Emoji headers found: {emoji_count}")
    else:
        results.append(f"❌ Insufficient emoji headers: {emoji_count}")
    
    return results

def test_license_file():
    """Test if LICENSE file exists"""
    if os.path.exists("LICENSE"):
        return "✅ LICENSE file exists"
    else:
        return "❌ LICENSE file missing"

def main():
    """Main test function"""
    print("🧪 Testing README.md structure and content...")
    print("=" * 50)
    
    # Test README structure
    readme_results = test_readme_structure()
    for result in readme_results:
        print(result)
    
    print("\n🧪 Testing LICENSE file...")
    print("=" * 30)
    print(test_license_file())
    
    # Count passed and failed tests
    total_tests = len(readme_results) + 1
    passed_tests = len([r for r in readme_results if r.startswith("✅")]) + (1 if os.path.exists("LICENSE") else 0)
    failed_tests = total_tests - passed_tests
    
    print(f"\n📊 Test Summary:")
    print(f"Total tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {failed_tests}")
    
    if failed_tests == 0:
        print("🎉 All tests passed!")
        return 0
    else:
        print("⚠️  Some tests failed!")
        return 1

if __name__ == "__main__":
    sys.exit(main())