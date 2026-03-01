# 🧠 LLM Domain Evaluation Prompts

## 项目简介 (Introduction)
本项目旨在针对特定垂直领域（泛金融、户外文旅、代码生成、语言学习），构建一套高质量的 Prompt（提示词）模板与评测标准（Evaluation Criteria）。通过边界测试（Edge-case testing）和压力测试，精准识别大语言模型（LLMs）在垂直领域输出中的逻辑漏洞与事实错误（Hallucinations）。

## 📂 领域分类 (Domains)

### 1. 泛金融与加密资产 (Finance & Crypto)
- **重点评测**: 智能合约基础逻辑解析、行情分析数据滞后性测试、信用卡积分收益最大化算法模型。

### 2. 户外徒步与跨境文旅 (Outdoors & Travel)
- **重点评测**: 高海拔徒步（如香格里拉阿布吉措）安全预警生成、新西兰 WHV 签证政策时效性校验、极端天气应对逻辑。

### 3. 语言学习与语料校验 (Language Learning)
- **重点评测**: PTE 学术英语长难句解析、多语种（中/英/德）语境切换的地道性、机器翻译生硬度评估。

### 4. 计算机与前沿技术 (Computer Science)
- **重点评测**: Python/C 代码生成边界测试、算法原理解释的准确度。

## 🛠 评测维度 (Evaluation Metrics)
1. **Factuality (真实性)**: 是否存在捏造数据或失效政策。
2. **Logical Rigor (逻辑严密性)**: 步骤推导是否连贯，是否存在自相矛盾。
3. **Safety & Ethics (安全性)**: 是否包含高风险投资诱导或危险户外行为建议。
