# 三角洲行动 - G.T.I.干员登录系统

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.6+](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/downloads/)

一个基于Python的交互式文本界面游戏，模拟全球反恐特勤组（G.T.I.）的干员登录系统。

## ⚠️ 免责声明

本项目是独立开发的非商业性质的个人作品，与腾讯集团以及琳琅天上运营团队没有任何关联。本项目的创意来源于玩《三角洲行动》游戏时的灵感，仅作为学习和娱乐用途。游戏中的角色、组织名称和背景设定均为虚构，如有雷同，纯属巧合。

## 📖 项目简介

在2035年的未来世界背景下，玩家将扮演全球反恐特勤组（G.T.I.）的精英特战干员，通过身份验证后获取任务简报并执行特殊行动。这是一个纯文本界面的模拟程序，展示了游戏化的登录流程和任务分配系统。

## ✨ 功能特点

- 沉浸式G.T.I.登录界面，包含动态安全扫描动画
- 4种不同定位的干员角色可供选择
- 身份认证系统，支持多次尝试与安全警报机制
- 个性化干员档案展示，包含详细个人信息
- 随机生成的任务简报，提供多样化的游戏体验
- 基于干员角色的智能任务建议
- 动态任务倒计时和部署动画效果
- 简洁的启动脚本，便于快速运行

## 📁 项目结构

```
├── delta_operator_login.py  # 主程序文件
├── run_operator.bat         # Windows启动脚本
├── LICENSE                  # Apache-2.0许可证文件
├── README.md                # 项目说明文档
```

## 🚀 快速开始

### 前提条件

- Python 3.6 或更高版本
- Windows操作系统（目前仅测试了Windows环境）

### 安装方法

1. 克隆本仓库到本地
   ```bash
   git clone https://github.com/willla888/Interesting-Delta-Action-Login-System.git
   cd Interesting-Delta-Action-Login-System
   ```

2. 无需额外安装依赖包，程序使用Python标准库

### 使用方法

#### 方法一：使用启动脚本（推荐）

直接双击运行 `run_operator.bat` 文件，程序将自动启动。

#### 方法二：命令行启动

1. 打开命令提示符（CMD）
2. 导航到程序所在目录
   ```bash
   cd path\to\Interesting-Delta-Action-Login-System
   ```
3. 运行命令：
   ```bash
   python delta_operator_login.py
   ```

## 🎮 游戏操作指南

### 可用干员

| 干员代号 | 密码 | 定位 | 专长 |
|---------|------|------|------|
| redwolf | alpha123 | 攻击型 | 高伤害输出 + 灵活机动 |
| beehive | medic456 | 支援型 | 快速治疗 + 负面状态清除 |
| shepherd | engineer789 | 工程师型 | 防御增益 + 区域控制 |
| luna | sniper007 | 侦察型 | 墙体穿透侦测 + 精准打击 |

### 游戏流程

1. 启动程序后，等待安全扫描完成
2. 输入干员代号和密码进行身份验证
3. 查看个人档案信息
4. 接收随机生成的任务简报
5. 根据倒计时准备任务
6. 等待任务部署完成

## ❓ 常见问题解决

### 问题：找不到Python

**解决方法**：请先安装Python，可以从 [Python官网](https://www.python.org/downloads/) 下载安装，并确保添加到系统PATH环境变量中。

### 问题：登录失败，显示"安全系统已触发警报"

**解决方法**：每个账户最多有3次尝试机会，请确认您使用的是正确的干员代号和密码，可参考上面的可用干员表格。

### 问题：程序闪退或显示乱码

**解决方法**：请使用提供的`run_operator.bat`启动脚本，这是经过测试的稳定启动方式。

## 🛠️ 开发说明

这是一个基于文本界面的模拟登录程序，主要使用Python标准库开发，包含以下核心模块：

- **登录认证系统**：处理用户输入验证和安全检查
- **干员数据库管理**：存储和检索干员信息
- **动态任务生成**：随机创建多样化的任务信息
- **文本动画效果**：提供打字机、闪烁等视觉效果

## 📝 更新日志

- 修复了Python代码中os模块导入问题
- 添加了简化版启动器以解决编码和兼容性问题
- 优化了文本动画效果和用户交互体验
- 添加了Unity游戏项目文件夹
- 更新了项目结构和GitHub仓库信息
- 更新了许可证为Apache-2.0

## 📄 许可证

本项目采用Apache-2.0许可证 - 详见 [LICENSE](LICENSE) 文件

## 🤝 贡献指南

欢迎提交问题和改进建议！如果您想为项目做出贡献，请遵循以下步骤：

1. Fork本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📧 联系信息

如有任何问题或建议，请随时联系项目维护者。

---

*全球反恐特勤组 - 为了更安全的未来* 🌍⚔️
