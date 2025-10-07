# 三角洲行动 - G.T.I.干员登录系统
# 
# ⚠️ 免责声明
# 本项目是独立开发的非商业性质的个人作品，与腾讯集团以及琳琅天上运营团队没有任何关联。
# 本项目的创意来源于玩《三角洲行动》游戏时的灵感，仅作为学习和娱乐用途。
# 游戏中的角色、组织名称和背景设定均为虚构，如有雷同，纯属巧合。
# 
# 项目GitHub地址：https://github.com/willla888/Interesting-Delta-Action-Login-System
# 许可证：Apache-2.0

import os
import time
import random
import getpass

# 清屏函数
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 打字机效果函数
def typewriter_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# 闪烁效果函数
def blink_text(text, times=3, delay=0.2):
    for _ in range(times):
        clear_screen()
        print(text)
        time.sleep(delay)
        clear_screen()
        print(' ' * len(text))
        time.sleep(delay)
    print(text)

# 干员数据库（模拟）
def get_operators_database():
    return {
        "redwolf": {
            "password": "alpha123",
            "name": "红狼",
            "rank": "上尉",
            "role": "攻击型",
            "skill": "高伤害输出 + 灵活机动",
            "status": "活跃",
            "missions_completed": 127,
            "deployment_count": 42
        },
        "beehive": {
            "password": "medic456",
            "name": "蜂医",
            "rank": "中尉",
            "role": "支援型",
            "skill": "快速治疗 + 负面状态清除",
            "status": "活跃",
            "missions_completed": 98,
            "deployment_count": 36
        },
        "shepherd": {
            "password": "engineer789",
            "name": "牧羊人",
            "rank": "少尉",
            "role": "工程师型",
            "skill": "防御增益 + 区域控制",
            "status": "活跃",
            "missions_completed": 85,
            "deployment_count": 31
        },
        "luna": {
            "password": "sniper007",
            "name": "露娜",
            "rank": "中尉",
            "role": "侦察型",
            "skill": "墙体穿透侦测 + 精准打击",
            "status": "活跃",
            "missions_completed": 112,
            "deployment_count": 39
        }
    }

# 随机任务生成函数
def generate_mission():
    mission_types = [
        "渗透侦察", "人质救援", "摧毁目标", 
        "情报窃取", "定点清除", "防御行动"
    ]
    locations = ["阿萨拉地区", "东欧某国", "中东沙漠", "东南亚丛林", "北极基地"]
    targets = ["哈夫克公司据点", "恐怖分子训练营", "秘密研究设施", "武器交易点", "敌方指挥中心"]
    threats = ["重火力防御", "生化武器威胁", "高价值目标保护", "恶劣天气条件", "复杂地形"]
    
    return {
        "type": random.choice(mission_types),
        "location": random.choice(locations),
        "target": random.choice(targets),
        "threat": random.choice(threats),
        "priority": random.choice(["低", "中", "高", "极高"]),
        "team_size": random.randint(2, 6)
    }

# 显示G.T.I.标志和标题
def show_gti_logo():
    logo = """
    ╔══════════════════════════════════════════════════════╗
    ║                                                      ║
    ║      ██████╗ ███████╗██████╗ ███████╗███████╗        ║
    ║      ██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝        ║
    ║      ██████╔╝█████╗  ██████╔╝█████╗  ███████╗        ║
    ║      ██╔══██╗██╔══╝  ██╔══██╗██╔══╝  ╚════██║        ║
    ║      ██║  ██║███████╗██████╔╝███████╗███████║        ║
    ║      ╚═╝  ╚═╝╚══════╝╚═════╝ ╚══════╝╚══════╝        ║
    ║                                                      ║
    ║                  GLOBAL TACTICAL INITIATIVE          ║
    ║                        全球反恐特勤组                ║
    ╚══════════════════════════════════════════════════════╝
    """
    print(logo)
    time.sleep(1.5)

# 登录界面
def login_interface():
    clear_screen()
    show_gti_logo()
    
    typewriter_effect("欢迎回来，干员。请进行身份验证以接入G.T.I.系统...", 0.05)
    print("\n正在初始化安全模块...")
    time.sleep(1)
    
    # 模拟安全扫描动画
    for i in range(101):
        time.sleep(0.02)
        print(f"\r安全扫描进度: {i}%", end='')
    print()
    
    # 获取数据库
    operators_db = get_operators_database()
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        username = input("\n干员代号: ")
        password = getpass.getpass("认证密码: ")
        
        if username in operators_db and operators_db[username]["password"] == password:
            # 登录成功
            clear_screen()
            blink_text("身份验证成功！正在加载干员档案...")
            time.sleep(1)
            return operators_db[username]
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"\n错误: 干员代号或密码不正确。剩余尝试次数: {remaining}")
            
            if attempts >= max_attempts:
                print("\n安全系统已触发警报！程序将在5秒后自动退出...")
                for i in range(5, 0, -1):
                    print(f"\r退出倒计时: {i}", end='')
                    time.sleep(1)
                exit()
            
            time.sleep(1)

# 显示干员信息
def show_operator_info(operator):
    clear_screen()
    
    header = "\n===== G.T.I. 干员档案 ====="
    print(header)
    print("=" * len(header))
    print(f"姓名: {operator['name']}")
    print(f"代号: {operator['name'].lower()}")
    print(f"军衔: {operator['rank']}")
    print(f"定位: {operator['role']}")
    print(f"专长: {operator['skill']}")
    print(f"状态: {operator['status']}")
    print(f"已完成任务: {operator['missions_completed']}")
    print(f"出勤次数: {operator['deployment_count']}")
    print("=" * len(header))
    
    input("\n按回车键继续...")

# 显示任务简报
def show_mission_briefing(operator):
    clear_screen()
    
    typewriter_effect("正在接收最新任务简报...", 0.05)
    time.sleep(1)
    
    # 生成任务
    mission = generate_mission()
    
    clear_screen()
    briefing_header = f"\n===== 任务简报 - {mission['type']} ====="
    print(briefing_header)
    print("=" * len(briefing_header))
    typewriter_effect(f"任务类型: {mission['type']}", 0.03)
    typewriter_effect(f"任务地点: {mission['location']}", 0.03)
    typewriter_effect(f"目标: {mission['target']}", 0.03)
    typewriter_effect(f"威胁等级: {mission['threat']}", 0.03)
    typewriter_effect(f"任务优先级: {mission['priority']}", 0.03)
    typewriter_effect(f"小队规模: {mission['team_size']}人", 0.03)
    print("=" * len(briefing_header))
    
    # 任务分配
    typewriter_effect(f"\n{operator['name']}干员，你的角色定位是{operator['role']}，", 0.03)
    typewriter_effect(f"请根据你的专长{operator['skill']}执行任务。", 0.03)
    
    # 动态任务建议
    if operator['role'] == "攻击型":
        typewriter_effect("\n建议: 作为攻击型干员，你将负责突破敌方防线，为团队开辟前进道路。", 0.03)
    elif operator['role'] == "支援型":
        typewriter_effect("\n建议: 作为支援型干员，你将负责保障团队成员的生命安全，提供必要的医疗支持。", 0.03)
    elif operator['role'] == "工程师型":
        typewriter_effect("\n建议: 作为工程师型干员，你将负责设置防御工事，控制关键区域。", 0.03)
    elif operator['role'] == "侦察型":
        typewriter_effect("\n建议: 作为侦察型干员，你将负责收集敌方情报，为团队提供精准的目标位置。", 0.03)
    
    print("\n")
    typewriter_effect("任务准备时间剩余: 30秒", 0.05)
    
    # 倒计时
    for i in range(30, 0, -1):
        time.sleep(1)
        print(f"\r任务准备时间剩余: {i}秒", end='')
    print()

# 部署确认
def deployment_confirmation():
    clear_screen()
    
    deployment_text = """
    ╔════════════════════════════════════════════╗
    ║           任务部署确认                     ║
    ╠════════════════════════════════════════════╣
    ║                                            ║
    ║     所有系统检查完毕，装备准备就绪         ║
    ║     通讯系统已连接，小队频道已建立         ║
    ║     目标坐标已锁定，航线规划完成           ║
    ║                                            ║
    ║     G.T.I.指挥部祝各位干员任务顺利！       ║
    ║                                            ║
    ╚════════════════════════════════════════════╝
    """
    
    print(deployment_text)
    time.sleep(2)
    
    typewriter_effect("\n3...", 0.5)
    typewriter_effect("2...", 0.5)
    typewriter_effect("1...", 0.5)
    typewriter_effect("出发！", 0.5)
    
    # 闪烁效果模拟起飞
    for _ in range(5):
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t✈️  任务部署中...")
        time.sleep(0.1)
        clear_screen()
        time.sleep(0.1)

# 主函数
def main():
    try:
        # 登录流程
        operator = login_interface()
        
        # 显示干员信息
        show_operator_info(operator)
        
        # 任务简报
        show_mission_briefing(operator)
        
        # 部署确认
        deployment_confirmation()
        
        # 结束界面
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t任务已启动")
        typewriter_effect("\n\t\t\t\tG.T.I.系统已断开连接", 0.05)
        
    except KeyboardInterrupt:
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\t\t\t\t系统连接已中断")
        print("\t\t\t\t安全协议已激活")
    
    finally:
        time.sleep(2)

if __name__ == "__main__":
    main()