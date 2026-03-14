import zipfile
import os

# 定义文件内容
files = {
    "index.html": """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学术会议通用管理平台 - MVP 演示</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-slate-50">
    <div id="env-switcher" class="bg-gray-900 text-white text-xs py-2 px-4 flex justify-between items-center sticky top-0 z-[100]">
        <div><i class="fas fa-code-branch mr-2"></i> v1.0 MVP 稳定版</div>
        <div class="flex space-x-2">
            <button onclick="switchView('admin')" id="btn-admin" class="bg-blue-600 px-3 py-1 rounded">B端：管理系统</button>
            <button onclick="switchView('client')" id="btn-client" class="bg-gray-700 px-3 py-1 rounded">C端：展示系统</button>
        </div>
    </div>
    <div id="admin-view"></div>
    <div id="client-view" class="hidden"></div>
    <script src="admin.js"></script>
    <script src="client.js"></script>
    <script>
        function switchView(view) {
            const admin = document.getElementById('admin-view');
            const client = document.getElementById('client-view');
            const btnA = document.getElementById('btn-admin');
            const btnC = document.getElementById('btn-client');
            if(view === 'admin') {
                admin.classList.remove('hidden');
                client.classList.add('hidden');
                btnA.className = 'bg-blue-600 px-3 py-1 rounded';
                btnC.className = 'bg-gray-700 px-3 py-1 rounded';
            } else {
                admin.classList.add('hidden');
                client.classList.remove('hidden');
                btnC.className = 'bg-blue-600 px-3 py-1 rounded';
                btnA.className = 'bg-gray-700 px-3 py-1 rounded';
            }
        }
        window.onload = () => { renderAdmin(); renderClient(); };
    </script>
</body>
</html>""",
    "style.css": """
:root { --primary: #1e40af; --secondary: #64748b; }
body { font-family: 'PingFang SC', 'Microsoft YaHei', sans-serif; }
.card { @apply bg-white rounded-lg shadow-sm border border-gray-100; }
.btn-primary { @apply bg-blue-700 text-white px-4 py-2 rounded hover:bg-blue-800 transition-all; }
.status-pill { @apply px-2 py-1 rounded text-xs font-medium; }
""",
    "admin.js": """
const adminData = {
    stats: { registrations: 1284, submissions: 45, hotels: "82%", revenue: "24.8w" },
    conferences: [
        { id: 1, name: "2026 AI国际学术会议", date: "2026-05-20", status: "报名中", count: "856/1000" },
        { id: 2, name: "第三届生物材料论坛", date: "2026-07-15", status: "草稿", count: "0/500" }
    ]
};
function renderAdmin() {
    const container = document.getElementById('admin-view');
    container.innerHTML = `
        <div class="flex min-h-screen">
            <aside class="w-64 bg-slate-800 text-slate-300 p-6">
                <div class="text-white font-bold text-xl mb-8">会议管理系统</div>
                <nav class="space-y-4">
                    <div class="text-white bg-blue-600 p-2 rounded cursor-pointer"><i class="fas fa-home mr-2"></i> 控制台</div>
                    <div class="p-2 hover:bg-slate-700 rounded cursor-pointer"><i class="fas fa-calendar mr-2"></i> 会议管理</div>
                    <div class="p-2 hover:bg-slate-700 rounded cursor-pointer"><i class="fas fa-user-friends mr-2"></i> 参会管理</div>
                </nav>
            </aside>
            <main class="flex-1 p-8">
                <div class="flex justify-between items-center mb-8">
                    <h2 class="text-2xl font-bold text-slate-800">数据总览</h2>
                    <button class="btn-primary" onclick="alert('进入创建会议流程')">+ 创建新会议</button>
                </div>
                <div class="grid grid-cols-4 gap-6 mb-8">
                    ${Object.entries(adminData.stats).map(([k, v]) => `
                        <div class="bg-white p-6 rounded-xl shadow-sm border border-slate-100">
                            <div class="text-slate-500 text-sm uppercase">${k}</div>
                            <div class="text-2xl font-bold text-slate-800 mt-1">${v}</div>
                        </div>
                    `).join('')}
                </div>
                <div class="bg-white rounded-xl shadow-sm border border-slate-100 overflow-hidden">
                    <table class="w-full text-left">
                        <thead class="bg-slate-50 border-b">
                            <tr><th class="p-4">会议名称</th><th class="p-4">举办日期</th><th class="p-4">状态</th><th class="p-4">人数</th></tr>
                        </thead>
                        <tbody>
                            ${adminData.conferences.map(c => `
                                <tr class="border-b hover:bg-slate-50">
                                    <td class="p-4 font-medium">${c.name}</td>
                                    <td class="p-4 text-slate-600">${c.date}</td>
                                    <td class="p-4"><span class="px-2 py-1 bg-green-100 text-green-700 rounded text-xs">${c.status}</span></td>
                                    <td class="p-4">${c.count}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            </main>
        </div>`;
}""",
    "client.js": """
function renderClient() {
    const container = document.getElementById('client-view');
    container.innerHTML = `
        <nav class="bg-white border-b px-6 py-4 flex justify-between items-center">
            <div class="text-blue-800 font-black text-2xl tracking-tighter">ICAI 2026</div>
            <div class="space-x-6 text-sm font-medium text-slate-600">
                <a href="#" class="text-blue-600 border-b-2 border-blue-600 pb-1">首页</a>
                <a href="#">日程</a><a href="#">投稿</a><a href="#">住宿</a>
            </div>
            <button class="bg-blue-700 text-white px-6 py-2 rounded-full text-sm font-bold shadow-lg shadow-blue-100">立即报名</button>
        </nav>
        <div class="bg-slate-900 text-white py-20 px-6 text-center bg-[url('https://www.transparenttextures.com/patterns/cubes.png')]">
            <h1 class="text-5xl font-extrabold mb-4">2026 国际人工智能学术交流大会</h1>
            <p class="text-slate-400 text-lg max-w-2xl mx-auto">汇聚全球顶尖学者，探讨通用人工智能与大模型的未来演进。</p>
        </div>
        <div class="max-w-4xl mx-auto py-12 px-6">
            <div class="bg-white border rounded-2xl p-8 shadow-sm">
                <h3 class="text-xl font-bold mb-6">参会报名信息登记</h3>
                <div class="grid grid-cols-2 gap-6 mb-6">
                    <div>
                        <label class="block text-sm font-medium text-slate-700 mb-2">姓名</label>
                        <input type="text" class="w-full border rounded-lg p-3 outline-none focus:ring-2 ring-blue-500/20" placeholder="请输入姓名">
                    </div>
                    <div>
                        <label class="block text-sm font-medium text-slate-700 mb-2">参会身份</label>
                        <select class="w-full border rounded-lg p-3 outline-none" onchange="window.updatePrice(this.value)">
                            <option value="2500">正式代表 (¥2500)</option>
                            <option value="1200">学生代表 (¥1200)</option>
                        </select>
                    </div>
                </div>
                <div class="bg-slate-50 p-6 rounded-xl border border-dashed border-slate-200 flex justify-between items-center">
                    <div>
                        <div class="text-sm text-slate-500">应付总额</div>
                        <div class="text-3xl font-black text-blue-700" id="total-price">¥ 2500.00</div>
                    </div>
                    <button class="bg-slate-900 text-white px-8 py-3 rounded-xl font-bold hover:scale-105 transition-transform" onclick="alert('报名成功！')">确认并支付</button>
                </div>
            </div>
        </div>`;
}
window.updatePrice = (val) => { document.getElementById('total-price').innerText = '¥ ' + val + '.00'; };"""
}

# 创建 ZIP
zip_name = "Academic_Conference_MVP.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        zipf.write(filename)
        os.remove(filename)

print(f"成功生成压缩包: {os.path.abspath(zip_name)}")
