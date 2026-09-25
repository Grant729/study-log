# GitHub 基建保姆级教程（零基础版）

> 预计总时长 60~90 分钟。全程用图形界面，**不需要记任何 Git 命令**。
> 四大步：① 注册账号 → ② 安装并登录 GitHub Desktop → ③ 把学习日志文件夹变成仓库 → ④ 发布到网上。
> 完成后你就是有 GitHub 主页的人了，以后每天只需 2 分钟。

---

## 第 1 步：注册 GitHub 账号（约 15 分钟）

1. 浏览器打开官网：**https://github.com**（英文界面，没有官方中文版，照下面点就行）
2. 点右上角 **Sign up**（注册）
3. 输入邮箱 → 点 **Continue**（继续）
   - 建议用常用邮箱；学校邮箱以后可免费领学生福利（教程末尾有说）
4. 设置密码（至少 8 位，含字母和数字）→ 点 **Continue**
5. 起用户名（Username）→ 点 **Continue**
   - 这是你主页网址的一部分：`github.com/用户名`，建议用名字拼音或专业相关，全小写英文字母/数字/连字符
   - 页面提示 **already taken**（已被占用）就换一个，比如加数字后缀
6. 问是否接收产品更新邮件 → 选哪个都行 → **Continue**
7. 人机验证：按页面提示做（可能是旋转图片、点选图形；卡住就刷新页面重来）
8. 去邮箱收验证码（8 位数字；**没收到就翻垃圾箱**），填进页面 → 登录成功
9. 个性化问卷（团队人数、是否学生等）→ 全部不用管，拉到页面最底部点 **Skip personalization**（跳过个性化）
10. 进入你的主页 → ✅ 注册完成

---

## 第 2 步：安装并登录 GitHub Desktop（约 20 分钟）

1. 浏览器打开：**https://desktop.github.com/**
2. 点紫色大按钮 **Download for Windows (64bit)** → 下载 `GitHubDesktopSetup-x64.exe`
3. 双击安装（不需要管理员权限，等 2~3 分钟装完）
   - 如果这个网站打不开：按 Win 键搜索 PowerShell 打开，输入 `winget install GitHub.GitHubDesktop` 回车，也能装
4. 打开 GitHub Desktop → 首次启动界面点 **Sign in to GitHub.com**（登录 GitHub.com）
5. 浏览器自动打开授权页 → 点绿色按钮 **Authorize github**（或 Authorize desktop，授权）
6. 浏览器弹窗问"是否打开 GitHub Desktop"→ 点 **打开 / Open**
7. 回到 Desktop 窗口：出现 **Configure Git**（配置 Git）对话框
   - Name（姓名）填你的名字拼音，如 `Guangtao Wang`
   - Email 填**注册时用的那个邮箱**
   - 点 **Finish**（完成）
8. 进入 "Let's get started" 界面 → ✅ 登录完成

---

## 第 3 步：把学习日志文件夹变成仓库（约 10 分钟）

> 你的学习日志已经在 `D:\AI project\demo\study-log` 文件夹里，直接把它原地变成 Git 仓库，不用复制任何文件。

1. 在 GitHub Desktop 里，点菜单 **File（文件）→ Add local repository...（添加本地仓库）**
2. 点 **Choose...（选择）**，导航到 `D:\AI project\demo\study-log` 文件夹，选中后点 **Select Folder**
3. 弹窗提示"这个文件夹还不是 Git 仓库，要在这里创建一个吗？"→ 点 **create a repository**（创建仓库）
4. 弹出的对话框：Name 保持 `study-log`，其他全部不动 → 点 **Create repository**（创建仓库）
5. 左侧仓库栏出现 `study-log`，右侧 **Changes**（更改）列表里已经能看到你所有的学习日志文件 → ✅ 仓库建好

---

## 第 4 步：第一次提交并发布到网上（约 15 分钟）

1. 看左下角的 **Summary**（摘要）输入框，填一句说明：`初始化学习日志`
2. 点下方 **Commit to main**（提交到 main）按钮 → 右侧 Changes 列表清空，说明提交成功
3. 点顶部右侧的蓝色 **Publish repository**（发布仓库）按钮
4. 弹出对话框：
   - Name 保持 `study-log`
   - **不勾选** "Keep this code private"（保持私有）= 公开仓库，**推荐**——这就是你以后的作品集，面试官能看到
   - 如果不想让别人看到，就勾上（以后也能改）
   - 点 **Publish repository**（发布仓库）
5. 等待上传（国内网络可能慢，失败就点 Retry 重试）
6. **验证**：浏览器打开 `https://github.com/你的用户名/study-log` → 能看到文件列表 ✅
7. 再打开你的主页 `https://github.com/你的用户名` → 今天的小格子已经变绿 ✅

🎉 恭喜，你的 GitHub 基建完成，学习日志正式上线。

---

## 以后每天只需 2 分钟

1. 学完，在 week00.md 里写当日记录（或改任何文件）
2. 打开 GitHub Desktop → 左侧选 `study-log` 仓库 → Changes 里看到改动
3. Summary 写一句话（如 `第0周D3 R向量练习`）→ 点 **Commit to main**（提交到 main）
4. 点右上角 **Push origin**（推送 origin，第一次提交后才会出现）→ 完成
5. 你的主页格子又绿了一天 🟩

---

## 常见问题（提前打预防针）

| 问题 | 解法 |
|---|---|
| 邮箱验证码没收到 | 翻垃圾箱；等 1 分钟；点重新发送 |
| 用户名被占用 | 加数字后缀或换组合，如 `guangtaowang2026` |
| 注册卡在人机验证 | 换 Chrome / Edge 浏览器，或换个网络再试 |
| 授权后 Desktop 没反应/白屏 | 完全退出 Desktop 再打开，重新点 Sign in |
| 网站打开极慢 | github.com 在国内网络波动大，多刷新几次；实在不行开手机热点 |
| Publish / Push 失败 | 点 Retry；网络恢复后 Desktop 会自动补传 |
| 改了文件但 Changes 里没显示 | 确认改的是 `study-log` 文件夹里的文件，且左上角选的是这个仓库 |

---

## 完成后可选：免费学生福利

用**学校邮箱**到 **https://education.github.com/pack** 申请 GitHub Student Developer Pack（学生开发包），研究生也能申，免费领 GitHub Pro、Copilot 等，验证可能要等几天。现在不做也不影响任何事，先放着。
