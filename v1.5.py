import zipfile
import os

files = {
    "index.html": """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>学术会议管理平台 - v1.5 增强版</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .sidebar-active { bg-blue-700 text-white shadow-lg; }
        .tab-active { border-b-2 border-blue-600 text-blue-600; }
    </style>
</head>
<body class="bg-slate-50 font-sans">
    <div class="bg-indigo-900 text-white text-[10px] py-1 px-4 flex justify-between sticky top-0 z-[100]">
        <span><i class="fas fa-microchip mr-1"></i> 当前版本: v1.5 (Academic Core)</span>
        <div class="flex gap-3">
            <button onclick="switchView('admin')" id="btn-admin" class="bg-blue-600 px-2 rounded">B端管理</button>
            <button onclick="switchView('client')" id="btn-client" class="bg-slate-700 px-2 rounded">C端展示</button>
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
            document.getElementById('btn-admin').className = view === 'admin' ? 'bg-blue-600 px-2 rounded' : 'bg-slate-700 px-2 rounded';
            document.getElementById('btn-client').className = view === 'client' ? 'bg-blue-600 px-2 rounded' : 'bg-slate-700 px-2 rounded';
        }
        window.onload = () => { renderAdmin(); renderClient(); };
    </script>
</body>
</html>""",

    "admin.js": """
const state = {
    currentTab: 'dashboard',
    submissions: [
        { id: 'SUB001', title: '基于大模型的医学影像分析', author: '林教授', status: '待初审', time: '2026-03-12' },
        { id: 'SUB002', title: '具身智能在工业抓取中的应用', author: '王博士', status: '评审中', time: '2026-03-14' }
    ]
};

function renderAdmin() {
    const container = document.getElementById('admin-view');
    container.innerHTML = `
        <div class="flex min-h-screen">
            <aside class="w-60 bg-slate-900 text-slate-400 p-4">
                <div class="text-white font-bold text-lg mb-8 px-2">学术平台 Pro</div>
                <nav class="space-y-1">
                    ${navItem('dashboard', 'fas fa-chart-pie', '工作台')}
                    ${navItem('submissions', 'fas fa-file-medical', '投稿评审')}
                    ${navItem('schedule', 'fas fa-calendar-check', '日程编排')}
                </nav>
            </aside>
            <main class="flex-1 p-8" id="admin-content">${renderSubView()}</main>
        </div>`;
}

function navItem(id, icon, label) {
    const active = state.currentTab === id ? 'bg-blue-600 text-white' : 'hover:bg-slate-800';
    return `<div onclick="state.currentTab='${id}'; renderAdmin()" class="p-3 rounded-lg cursor-pointer flex items-center transition-colors ${active}">
                <i class="${icon} w-6"></i> <span>${label}</span>
            </div>`;
}

function renderSubView() {
    if (state.currentTab === 'submissions') {
        return `
            <div class="flex justify-between items-end mb-6">
                <div><h2 class="text-2xl font-bold">论文投稿管理</h2><p class="text-slate-500 text-sm">共 ${state.submissions.length} 篇待处理稿件</p></div>
                <div class="flex gap-2"><input type="text" placeholder="搜索标题..." class="border rounded px-3 py-2 text-sm w-64"></div>
            </div>
            <div class="bg-white rounded-xl shadow-sm border">
                <table class="w-full text-left text-sm">
                    <thead class="bg-slate-50 border-b">
                        <tr><th class="p-4">稿件编号</th><th class="p-4">论文标题</th><th class="p-4">作者</th><th class="p-4">状态</th><th class="p-4">操作</th></tr>
                    </thead>
                    <tbody>
                        ${state.submissions.map(s => `
                            <tr class="border-b hover:bg-slate-50">
                                <td class="p-4 text-slate-500">${s.id}</td>
                                <td class="p-4 font-medium">${s.title}</td>
                                <td class="p-4">${s.author}</td>
                                <td class="p-4"><span class="px-2 py-1 ${s.status === '待初审' ? 'bg-orange-100 text-orange-600' : 'bg-blue-100 text-blue-600'} rounded text-[10px]">${s.status}</span></td>
                                <td class="p-4 space-x-3">
                                    <button class="text-blue-600 hover:underline" onclick="alert('初审通过，已移至评审池')">初审</button>
                                    <button class="text-slate-400 hover:underline">下载</button>
                                </td>
                            </tr>
                        `).join('')}
                    </tbody>
                </table>
            </div>`;
    }
    return `<div class="p-20 text-center text-slate-400"><i class="fas fa-tools text-4xl mb-4"></i><p>工作台与日程编排功能已就绪，请选择左侧菜单。</p></div>`;
}""",

    "client.js": """
function renderClient() {
    const container = document.getElementById('client-view');
    container.innerHTML = `
        <header class="bg-white border-b px-6 py-3 flex justify-between items-center sticky top-0 z-50">
            <div class="flex items-center gap-2"><div class="w-8 h-8 bg-blue-700 rounded flex items-center justify-center text-white"><i class="fas fa-atom"></i></div><span class="font-bold text-xl">ICAI 2026</span></div>
            <div class="flex gap-8 text-sm font-medium">
                <a href="#" class="text-blue-600 border-b-2 border-blue-600 pb-1">首页</a>
                <a href="#" class="text-slate-600">会议日程</a>
                <a href="#" class="text-slate-600">在线投稿</a>
            </div>
            <div class="flex gap-3"><button class="px-4 py-2 text-sm font-medium">我的稿件</button><button class="bg-blue-700 text-white px-5 py-2 rounded-full text-sm font-bold">立即报名</button></div>
        </header>
        
        <div class="max-w-5xl mx-auto py-12 px-6">
            <div class="grid grid-cols-3 gap-10">
                <div class="col-span-2">
                    <section class="mb-12">
                        <h2 class="text-2xl font-bold mb-6 flex items-center gap-3"><i class="fas fa-calendar-alt text-blue-600"></i> 会议日程 (2026-05-20)</h2>
                        <div class="bg-white border rounded-2xl overflow-hidden shadow-sm">
                            <div class="flex border-b bg-slate-50">
                                <button class="px-6 py-3 text-sm font-bold border-r bg-white text-blue-700">主会场</button>
                                <button class="px-6 py-3 text-sm font-medium text-slate-500 hover:bg-white">分会场 A</button>
                                <button class="px-6 py-3 text-sm font-medium text-slate-500 hover:bg-white">分会场 B</button>
                            </div>
                            <div class="p-0">
                                ${renderScheduleItem('09:00 - 10:00', '开幕式与特邀主题报告', '张院士, 李教授', 'Main Hall')}
                                ${renderScheduleItem('10:00 - 10:30', '茶歇与学术海报交流', '-', 'Foyer')}
                                ${renderScheduleItem('10:30 - 12:00', '生成式AI：从模型到应用', 'OpenAI 专家团', 'Main Hall')}
                            </div>
                        </div>
                    </section>
                </div>
                
                <div class="col-span-1">
                    <div class="bg-slate-900 rounded-2xl p-6 text-white mb-6">
                        <h3 class="font-bold mb-2">重要日期</h3>
                        <div class="space-y-4 mt-4 text-sm">
                            <div class="flex justify-between border-b border-slate-700 pb-2"><span>投稿截止</span><span class="text-orange-400">2026-04-01</span></div>
                            <div class="flex justify-between border-b border-slate-700 pb-2"><span>录用通知</span><span class="text-blue-400">2026-04-15</span></div>
                            <div class="flex justify-between"><span>早鸟票截止</span><span class="text-green-400">2026-03-30</span></div>
                        </div>
                    </div>
                    <div class="border rounded-2xl p-6 bg-white shadow-sm">
                        <h3 class="font-bold mb-4">快速投稿</h3>
                        <p class="text-xs text-slate-500 mb-4">请按照模板准备 PDF 格式稿件，大小不超过 20MB。</p>
                        <button class="w-full py-3 border-2 border-dashed border-blue-200 text-blue-600 rounded-xl text-sm font-bold hover:bg-blue-50 transition-colors" onclick="alert('进入投稿信息填写页')">开始在线投稿</button>
                    </div>
                </div>
            </div>
        </div>`;
}

function renderScheduleItem(time, title, speaker, room) {
    return `<div class="p-6 border-b last:border-0 hover:bg-slate-50 transition-colors">
                <div class="flex justify-between items-start">
                    <div class="flex gap-4">
                        <div class="text-blue-700 font-mono font-bold text-sm w-24 pt-1">${time}</div>
                        <div>
                            <div class="font-bold text-slate-800">${title}</div>
                            <div class="text-xs text-slate-500 mt-1"><i class="far fa-user mr-1"></i> ${speaker}</div>
                        </div>
                    </div>
                    <span class="text-[10px] bg-slate-100 px-2 py-1 rounded uppercase font-bold text-slate-400">${room}</span>
                </div>
            </div>`;
}"""
}

zip_name = "Academic_Conference_v1.5_Pro.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f: f.write(content)
        zipf.write(filename)
        os.remove(filename)

print(f"v1.5 增强版原型生成成功: {os.path.abspath(zip_name)}")
