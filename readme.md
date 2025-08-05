# Day One On AWS - 项目解读

![AWS](https://img.shields.io/badge/AWS-Cloud-orange)
![Learning](https://img.shields.io/badge/Learning-Resources-blue)
![Open Source](https://img.shields.io/badge/Open%20Source-MIT-green)

## 📖 项目概述 | Project Overview

**"Every day is day one! Keep curious and keep learning."**

本项目是一个综合性的AWS学习资源集合，旨在为云计算学习者和实践者提供系统化的AWS技术栈学习路径。项目涵盖了机器学习、大数据、DevOps和无服务器架构等多个核心领域，每个领域都包含实际的项目示例和最佳实践。

This project is a comprehensive collection of AWS learning resources, designed to provide systematic learning paths for cloud computing learners and practitioners. It covers multiple core areas including Machine Learning, Big Data, DevOps, and Serverless architecture, with practical project examples and best practices.

## 🏗️ 项目结构 | Project Structure

```
Day-One-On-AWS/
├── 📚 ML on AWS (机器学习)
├── 📊 Big Data on AWS (大数据)
├── 🔧 DevOps on AWS (开发运维)
└── ⚡ Serverless on AWS (无服务器)
```

## 🤖 机器学习 | ML on AWS

### 项目描述
机器学习模块提供了在AWS平台上构建、训练和部署机器学习模型的完整解决方案。

### 核心技术栈
- Amazon SageMaker
- AWS Lambda
- Amazon S3
- Amazon EC2

### 项目链接
- **主项目**: [ml-on-aws](https://github.com/VerRan/ml-on-aws/)
  - 包含端到端的机器学习工作流
  - 数据预处理、模型训练、模型部署示例
  - 最佳实践和性能优化指南

## 📊 大数据 | Big Data on AWS

### 项目描述
大数据模块展示了如何在AWS上构建可扩展的数据处理和分析解决方案。

### 核心技术栈
- Amazon EMR
- Amazon Redshift
- AWS Glue
- Amazon Kinesis
- Amazon Athena

### 项目链接
- **主项目**: [bigdata-on-aws](https://github.com/VerRan/bigdata-on-aws)
  - 大数据处理管道设计
  - 实时数据流处理
  - 数据仓库和数据湖架构

## 🔧 开发运维 | DevOps on AWS

### 项目描述
DevOps模块提供了现代化的持续集成/持续部署(CI/CD)解决方案和容器化应用管理。

### 核心技术栈
- Amazon EKS
- AWS CodePipeline
- AWS CodeBuild
- Amazon ECR
- AWS CloudFormation

### 项目详情

#### 1. DevOps 基础设施
- **项目**: [devops](https://github.com/VerRan/devops)
- **描述**: AWS DevOps工具链的完整实现
- **特性**: CI/CD管道、基础设施即代码、自动化部署

#### 2. SpringCloud on EKS
- **项目**: [cloud_university](https://github.com/VerRan/cloud_university)
- **描述**: 在Amazon EKS上部署SpringCloud微服务架构
- **特性**: 服务发现、配置管理、负载均衡、监控

#### 3. 容器日志收集
- **项目**: [farget-log-collect-demo](https://github.com/VerRan/farget-log-collect-demo)
- **描述**: AWS Fargate容器日志收集解决方案
- **特性**: 集中化日志管理、实时监控、日志分析

## ⚡ 无服务器架构 | Serverless on AWS

### 项目描述
无服务器模块展示了如何构建高效、可扩展的无服务器应用程序。

### 核心技术栈
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS Step Functions
- Amazon EventBridge

### 项目详情

#### 1. 媒体转换服务
- **项目**: [ivs-vod-merge](https://github.com/VerRan/ivs-vod-merge)
- **描述**: 使用Lambda和MediaConvert的视频处理服务
- **特性**: 自动视频转码、格式转换、批量处理

#### 2. SparkJava Lambda应用
- **项目**: [serverless-workshop](https://github.com/VerRan/serverless-workshop)
- **描述**: 在AWS Lambda上运行SparkJava应用
- **特性**: 轻量级Web框架、RESTful API、快速部署

#### 3. Lambda容器镜像
- **项目**: [lamabda-image-demo](https://github.com/VerRan/lamabda-image-demo)
- **描述**: 使用Docker镜像部署Lambda函数
- **特性**: 容器化部署、自定义运行时、大型依赖包支持

#### 4. 图像处理服务
- **项目**: [image-serverless-java](https://github.com/VerRan/image-serverless-java)
- **描述**: Java版本的无服务器图像处理服务
- **特性**: 图像缩放、格式转换、水印添加

#### 5. Lambda并发测试
- **项目**: [lambda-pc-test](https://github.com/VerRan/lambda-pc-test)
- **描述**: Lambda预配置并发性能测试
- **特性**: 并发控制、性能基准测试、成本优化

## 🚀 快速开始 | Quick Start

### 前置要求
- AWS账户
- AWS CLI配置
- Docker (用于容器化项目)
- Java 8+ (用于Java项目)
- Node.js (用于前端项目)

### 安装步骤
1. **克隆项目**
   ```bash
   git clone https://github.com/VerRan/Day-One-On-AWS.git
   cd Day-One-On-AWS
   ```

2. **配置AWS凭证**
   ```bash
   aws configure
   ```

3. **选择感兴趣的模块**
   - 访问对应的GitHub仓库
   - 按照各项目的README进行部署

## 📚 学习路径建议 | Learning Path

### 初学者路径
1. **DevOps基础** → 了解AWS基础服务和部署流程
2. **Serverless入门** → 学习无服务器架构概念
3. **大数据处理** → 掌握数据处理和分析技能
4. **机器学习** → 深入AI/ML在云端的应用

### 进阶路径
1. **微服务架构** → SpringCloud on EKS
2. **数据工程** → 端到端大数据解决方案
3. **MLOps** → 机器学习运维自动化
4. **成本优化** → Lambda并发和性能调优

## 🤝 贡献指南 | Contributing

我们欢迎社区贡献！请遵循以下步骤：

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

## 📄 许可证 | License

本项目采用MIT许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 联系方式 | Contact

- **项目维护者**: VerRan
- **GitHub**: [@VerRan](https://github.com/VerRan)

## 🙏 致谢 | Acknowledgments

感谢AWS社区和所有贡献者的支持和帮助！

---

**记住：每一天都是第一天！保持好奇心，持续学习！**

**Remember: Every day is day one! Keep curious and keep learning!**

