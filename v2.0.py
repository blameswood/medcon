import zipfile
import os

files = {
    "index.html": """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学术会议管理平台 - v2.0 最终闭环版</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .active-nav { @apply bg-blue-600 text-white shadow-md; }
        .glass-panel { background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px); }
        @keyframes pulse-soft { 0%, 100% { opacity: 1; } 50% { opacity: 0.7; } }
        .live-indicator { animation: pulse-soft 2s infinite; }
    </style>
</head>
<body class="bg-slate-100 font-sans">
    <div class="bg-black text-white text-[10px] py-1 px-4 flex justify-between sticky top-0 z-[100]">
        <span><i class="fas fa-check-circle text-green-400 mr-1"></i> 状态: v2.0 生产演示环境 (Final)</span>
        <div class="flex gap-4">
            <button onclick="switchView('admin')" id="btn-admin" class="bg-blue-600 px-3 rounded">管理端 (商家)</button>
            <button onclick="switchView('client')" id="btn-client" class="bg-slate-800 px-3 rounded">宣传端 (C端)</button>
        </div>
    </div>
    <div id="admin-view"></div>
    <div id="client-view" class="hidden"></div>
    <script src="admin.js"></script>
    <script src="client.js"></script>
    <script>
        function switchView(view) {
            document.getElementById('admin-view').classList.toggle('hidden', view !== 'admin');
            document.getElementById('client-view').classList.toggle('hidden', view !== 'client');
            document.getElementById('btn-admin').className = view === 'admin' ? 'bg-blue-600 px-3 rounded' : 'bg-slate-800 px-3 rounded';
            document.getElementById('btn-client').className = view === 'client' ? 'bg-blue-600 px-3 rounded' : 'bg-slate-800 px-3 rounded';
        }
        window.onload = () => { renderAdmin(); renderClient(); };
    </script>
</body>
</html>""",

    "admin.js": """
let adminState = {
    tab: 'stats',
    checkInData: { total: 1200, arrived: 456 },
    revenue: { registration: 15.2, submission: 4.8, hotel: 8.5 }
};

function renderAdmin() {
    const container = document.getElementById('admin-view');
    container.innerHTML = `
        <div class="flex min-h-screen">
            <aside class="w-64 bg-slate-900 text-slate-400 p-5 flex flex-col">
                <div class="text-white font-black text-xl mb-10 flex items-center gap-2">
                    <i class="fas fa-shield-alt text-blue-500"></i> 管理控制中心
                </div>
                <nav class="space-y-2 flex-1">
                    ${adminNavItem('stats', 'fas fa-chart-line', '数据大盘')}
                    ${adminNavItem('checkin', 'fas fa-qrcode', '现场签到')}
                    ${adminNavItem('exhibitors', 'fas fa-store', '展商管理')}
                    ${adminNavItem('finance', 'fas fa-wallet', '财务对账')}
                </nav>
                <div class="mt-auto p-4 bg-slate-800 rounded-xl text-xs">
                    <p class="text-slate-500">当前承办单位</p>
                    <p class="text-white font-bold">华中人工智能协会</p>
                </div>
            </aside>
            <main class="flex-1 p-10 bg-slate-50 overflow-y-auto" id="admin-main">
                ${renderAdminBody()}
            </main>
        </div>`;
}

function adminNavItem(id, icon, label) {
    const active = adminState.tab === id ? 'active-nav' : 'hover:bg-slate-800';
    return `<div onclick="adminState.tab='${id}'; renderAdmin()" class="flex items-center gap-3 p-3 rounded-xl cursor-pointer transition-all ${active}">
                <i class="${icon} text-lg"></i> <span class="font-medium">${label}</span>
            </div>`;
}

function renderAdminBody() {
    if (adminState.tab === 'stats') {
        return `
            <div class="mb-8 flex justify-between items-center">
                <h2 class="text-2xl font-bold text-slate-800">会议数据大盘 <span class="text-xs bg-green-100 text-green-600 px-2 py-1 rounded ml-2 live-indicator">实时更新中</span></h2>
            </div>
            <div class="grid grid-cols-3 gap-6 mb-10">
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                    <div class="text-slate-400 text-sm mb-2">总营收金额 (万元)</div>
                    <div class="text-3xl font-black text-slate-800">¥ ${adminState.revenue.registration + adminState.revenue.submission + adminState.revenue.hotel}</div>
                    <div class="mt-4 h-2 bg-slate-100 rounded-full flex overflow-hidden">
                        <div class="bg-blue-600 h-full" style="width: 50%"></div>
                        <div class="bg-purple-500 h-full" style="width: 20%"></div>
                        <div class="bg-yellow-500 h-full" style="width: 30%"></div>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 text-center">
                    <div class="text-slate-400 text-sm mb-2">到场率</div>
                    <div class="text-3xl font-black text-blue-600">${Math.round(adminState.checkInData.arrived/adminState.checkInData.total*100)}%</div>
                    <p class="text-xs text-slate-400 mt-2">已签到 ${adminState.checkInData.arrived} / 应到 ${adminState.checkInData.total}</p>
                </div>
                <div class="bg-white p-6 rounded-2xl shadow-sm border border-slate-100">
                    <div class="text-slate-400 text-sm mb-2">展商入驻</div>
                    <div class="text-3xl font-black text-slate-800">24 <span class="text-sm font-normal text-slate-400">/ 30 展位</span></div>
                    <div class="mt-4 text-xs text-green-500 font-bold"><i class="fas fa-caret-up"></i> 85% 使用率</div>
                </div>
            </div>
        `;
    }
    if (adminState.tab === 'checkin') {
        return `
            <div class="flex justify-between items-center mb-6">
                <h2 class="text-2xl font-bold">现场签到管理</h2>
                <button class="bg-blue-600 text-white px-4 py-2 rounded-lg text-sm" onclick="alert('开启摄像头扫码...')"><i class="fas fa-camera mr-2"></i> 扫码签到</button>
            </div>
            <div class="bg-white rounded-2xl shadow-sm overflow-hidden border">
                <div class="p-4 bg-slate-50 border-b flex gap-4">
                    <input type="text" placeholder="输入姓名/手机号/单位" class="flex-1 border rounded-lg px-4 py-2 text-sm outline-none">
                    <select class="border rounded-lg px-4 py-2 text-sm"><option>全部状态</option><option>已签到</option><option>未签到</option></select>
                </div>
                <table class="w-full text-left text-sm">
                    <thead class="bg-slate-50 text-slate-500"><tr><th class="p-4">姓名</th><th class="p-4">单位</th><th class="p-4">类型</th><th class="p-4">状态</th><th class="p-4">操作</th></tr></thead>
                    <tbody class="divide-y">
                        <tr class="hover:bg-slate-50"><td class="p-4 font-bold">李华</td><td class="p-4">清华大学</td><td class="p-4">正式代表</td><td class="p-4"><span class="text-green-600 bg-green-100 px-2 py-1 rounded text-xs">已签到</span></td><td class="p-4 text-slate-400">10:24 AM</td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-4 font-bold">Sarah Wood</td><td class="p-4">MIT</td><td class="p-4">特邀VIP</td><td class="p-4"><span class="text-slate-400 bg-slate-100 px-2 py-1 rounded text-xs">未签到</span></td><td class="p-4 text-blue-600 cursor-pointer">手动补签</td></tr>
                    </tbody>
                </table>
            </div>`;
    }
    return `<div class="p-20 text-center"><p class="text-slate-400 italic">模块建设中，请点击“数据大盘”或“现场签到”。</p></div>`;
}""",

    "client.js": """
function renderClient() {
    const container = document.getElementById('client-view');
    container.innerHTML = `
        <header class="bg-white/80 backdrop-blur-md border-b px-6 py-4 flex justify-between items-center sticky top-0 z-50">
            <div class="font-black text-2xl text-blue-900">ICAI 2026</div>
            <div class="hidden md:flex gap-8 text-sm font-bold text-slate-600">
                <a href="#" class="text-blue-600">首页</a><a href="#">日程</a><a href="#">住宿预订</a><a href="#">展商</a>
            </div>
            <div class="flex gap-4">
                <button class="bg-slate-100 w-10 h-10 rounded-full flex items-center justify-center text-slate-600"><i class="fas fa-user"></i></button>
            </div>
        </header>

        <div class="max-w-6xl mx-auto py-12 px-6 grid grid-cols-1 lg:grid-cols-3 gap-10">
            <div class="lg:col-span-2 space-y-12">
                <section>
                    <h2 class="text-3xl font-black mb-8">精选住宿酒店 <span class="text-sm font-normal text-slate-400 ml-2">协议价格保证</span></h2>
                    <div class="grid gap-6">
                        ${renderHotelCard('上海和平饭店', 'https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&q=80&w=800', '距离会场 200m', '¥ 1,280')}
                        ${renderHotelCard('锦江之星 (会场店)', 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&q=80&w=800', '距离会场 1.5km', '¥ 450')}
                    </div>
                </section>
            </div>

            <div class="lg:col-span-1">
                <div class="bg-white rounded-3xl p-8 border shadow-xl shadow-slate-200/50 sticky top-28">
                    <h3 class="font-bold text-xl mb-6 flex items-center gap-2"><i class="fas fa-ticket-alt text-blue-600"></i> 我的电子凭证</h3>
                    <div class="bg-slate-50 p-6 rounded-2xl flex flex-col items-center border border-dashed border-slate-200">
                        <div class="w-48 h-48 bg-white p-4 border rounded-xl mb-4">
                            <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=ICAI-2026-USER-001" alt="QR" class="w-full">
                        </div>
                        <div class="text-center">
                            <p class="font-bold text-lg">张学术 教授</p>
                            <p class="text-xs text-slate-400">正式代表 | ICAI-2026-001</p>
                        </div>
                    </div>
                    <div class="mt-6 space-y-3">
                        <div class="flex justify-between text-sm">
                            <span class="text-slate-500">签到状态</span>
                            <span class="text-orange-500 font-bold">待签到</span>
                        </div>
                        <div class="flex justify-between text-sm">
                            <span class="text-slate-500">已订酒店</span>
                            <span class="text-slate-800">和平饭店 (1间)</span>
                        </div>
                    </div>
                    <button class="w-full mt-8 bg-blue-700 text-white py-4 rounded-2xl font-black shadow-lg shadow-blue-200">下载报名确认函 (PDF)</button>
                </div>
            </div>
        </div>`;
}

function renderHotelCard(name, img, dist, price) {
    return `
        <div class="flex flex-col md:flex-row bg-white rounded-3xl overflow-hidden border hover:shadow-lg transition-all">
            <div class="md:w-64 h-48 bg-cover bg-center" style="background-image: url('${img}')"></div>
            <div class="flex-1 p-6 flex flex-col justify-between">
                <div>
                    <div class="flex justify-between items-start">
                        <h4 class="text-xl font-bold">${name}</h4>
                        <div class="text-blue-700 font-black">${price} <span class="text-xs font-normal text-slate-400">/ 晚起</span></div>
                    </div>
                    <p class="text-sm text-slate-500 mt-2"><i class="fas fa-map-marker-alt mr-2"></i> ${dist}</p>
                </div>
                <div class="flex gap-2 mt-4">
                    <span class="text-[10px] bg-slate-100 px-2 py-1 rounded">免费WiFi</span>
                    <span class="text-[10px] bg-slate-100 px-2 py-1 rounded">含双早</span>
                </div>
                <button class="mt-4 border-2 border-blue-700 text-blue-700 py-2 rounded-xl text-sm font-bold hover:bg-blue-700 hover:text-white transition-colors">查看详情及房型</button>
            </div>
        </div>`;
}"""
}

zip_name = "Academic_Conference_v2.0_Final.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f: f.write(content)
        zipf.write(filename)
        os.remove(filename)

print(f"v2.0 终极版原型已生成: {os.path.abspath(zip_name)}")
