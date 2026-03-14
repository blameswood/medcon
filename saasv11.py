import zipfile
import os

files = {
    "index.html": """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>SaaS 平台总管理后台 - SuperAdmin</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <style>
        .sidebar-active { background: #065f46; color: white; border-left: 4px solid #34d399; }
        .card-stat { transition: transform 0.2s; }
        .card-stat:hover { transform: translateY(-5px); }
    </style>
</head>
<body class="bg-gray-100 flex">
    <aside class="w-64 bg-slate-900 h-screen sticky top-0 text-slate-300 flex flex-col shadow-2xl">
        <div class="p-6 text-emerald-400 font-black text-2xl border-b border-slate-800">
            SaaS <span class="text-white text-sm font-light uppercase tracking-widest">Master</span>
        </div>
        <nav class="mt-6 flex-1 px-3 space-y-1">
            <div onclick="showPage('dash')" id="nav-dash" class="p-3 rounded-lg cursor-pointer flex items-center sidebar-active"><i class="fas fa-th-large w-8"></i> 平台概览</div>
            <div onclick="showPage('merchants')" id="nav-merchants" class="p-3 rounded-lg cursor-pointer flex items-center hover:bg-slate-800"><i class="fas fa-store w-8"></i> 租户/商家管理</div>
            <div onclick="showPage('plans')" id="nav-plans" class="p-3 rounded-lg cursor-pointer flex items-center hover:bg-slate-800"><i class="fas fa-layer-group w-8"></i> 套餐订阅控制</div>
            <div onclick="showPage('logs')" id="nav-logs" class="p-3 rounded-lg cursor-pointer flex items-center hover:bg-slate-800"><i class="fas fa-shield-virus w-8"></i> 系统审计</div>
        </nav>
        <div class="p-6 bg-slate-800/50 text-xs">
            <p>系统负载: 12%</p>
            <p class="text-emerald-500">Node Cluster: Healthy</p>
        </div>
    </aside>

    <main class="flex-1 min-h-screen overflow-y-auto">
        <header class="bg-white px-8 py-4 flex justify-between items-center shadow-sm">
            <div class="text-slate-500 font-medium">系统根路径 > <span id="breadcrumb">平台概览</span></div>
            <div class="flex items-center gap-6">
                <div class="flex items-center gap-2"><i class="fas fa-server text-emerald-500 text-xs"></i><span class="text-xs font-mono">Aliyun-Region-01</span></div>
                <img src="https://ui-avatars.com/api/?name=Super+Admin&background=059669&color=fff" class="w-8 h-8 rounded-full">
            </div>
        </header>

        <div id="content" class="p-8">
            <div id="page-dash">
                <div class="grid grid-cols-4 gap-6 mb-8">
                    <div class="bg-white p-6 rounded-2xl shadow-sm card-stat border-b-4 border-emerald-500">
                        <div class="text-gray-400 text-xs font-bold uppercase">累计入驻商家</div>
                        <div class="text-3xl font-black mt-2">124 <span class="text-sm text-green-500 font-normal">+5</span></div>
                    </div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm card-stat border-b-4 border-blue-500">
                        <div class="text-gray-400 text-xs font-bold uppercase">全平台活跃会议</div>
                        <div class="text-3xl font-black mt-2">562 <span class="text-sm text-blue-500 font-normal">运行中</span></div>
                    </div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm card-stat border-b-4 border-purple-500">
                        <div class="text-gray-400 text-xs font-bold uppercase">本月营收 (Subscription)</div>
                        <div class="text-3xl font-black mt-2">¥ 82.4w</div>
                    </div>
                    <div class="bg-white p-6 rounded-2xl shadow-sm card-stat border-b-4 border-red-500">
                        <div class="text-gray-400 text-xs font-bold uppercase">异常预警</div>
                        <div class="text-3xl font-black mt-2 text-red-500">02</div>
                    </div>
                </div>

                <div class="bg-white rounded-2xl shadow-sm p-6 border">
                    <h3 class="font-bold mb-4">实时资源消耗监控 (All Tenants)</h3>
                    <div class="space-y-6">
                        <div>
                            <div class="flex justify-between text-xs mb-2"><span>云存储空间 (已用 1.2TB / 5TB)</span><span class="font-mono">24%</span></div>
                            <div class="w-full bg-gray-100 h-2 rounded-full overflow-hidden"><div class="bg-emerald-500 h-full w-[24%]"></div></div>
                        </div>
                        <div>
                            <div class="flex justify-between text-xs mb-2"><span>短信服务余量 (35,000 / 1,000,000)</span><span class="text-red-500 font-bold">余额不足</span></div>
                            <div class="w-full bg-gray-100 h-2 rounded-full overflow-hidden"><div class="bg-red-400 h-full w-[3.5%]"></div></div>
                        </div>
                    </div>
                </div>
            </div>

            <div id="page-merchants" class="hidden">
                <div class="flex justify-between items-center mb-6">
                    <h2 class="text-xl font-bold">租户(商家)名单管理</h2>
                    <button class="bg-emerald-600 text-white px-4 py-2 rounded-lg text-sm">+ 开通新租户</button>
                </div>
                <div class="bg-white rounded-2xl shadow-sm overflow-hidden border">
                    <table class="w-full text-left text-sm">
                        <thead class="bg-slate-50 border-b uppercase text-xs text-slate-500">
                            <tr><th class="p-4">商家名称</th><th class="p-4">套餐版本</th><th class="p-4">到期时间</th><th class="p-4">会议总数</th><th class="p-4">操作</th></tr>
                        </thead>
                        <tbody class="divide-y">
                            <tr>
                                <td class="p-4"><div class="font-bold">华中人工智能协会</div><div class="text-[10px] text-gray-400">ID: TENANT-001</div></td>
                                <td class="p-4"><span class="bg-purple-100 text-purple-700 px-2 py-1 rounded text-[10px] font-bold">旗舰版</span></td>
                                <td class="p-4">2027-12-31</td>
                                <td class="p-4 font-mono">24</td>
                                <td class="p-4">
                                    <button class="text-blue-600 hover:underline mr-3" onclick="alert('模拟登录功能：正在以【华中人工智能协会】身份进入会议后台...')">模拟登录</button>
                                    <button class="text-red-600 hover:underline">冻结</button>
                                </td>
                            </tr>
                            <tr>
                                <td class="p-4"><div class="font-bold">某高校实验室</div><div class="text-[10px] text-gray-400">ID: TENANT-082</div></td>
                                <td class="p-4"><span class="bg-blue-100 text-blue-700 px-2 py-1 rounded text-[10px] font-bold">专业版</span></td>
                                <td class="p-4">2026-06-20</td>
                                <td class="p-4 font-mono">02</td>
                                <td class="p-4">
                                    <button class="text-blue-600 hover:underline mr-3">模拟登录</button>
                                    <button class="text-gray-400">续费</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </main>

    <script>
        function showPage(id) {
            // 切换页面显示
            document.getElementById('page-dash').classList.add('hidden');
            document.getElementById('page-merchants').classList.add('hidden');
            document.getElementById('page-' + id).classList.remove('hidden');
            
            // 切换导航样式
            document.querySelectorAll('nav div').forEach(el => el.className = 'p-3 rounded-lg cursor-pointer flex items-center hover:bg-slate-800');
            document.getElementById('nav-' + id).className = 'p-3 rounded-lg cursor-pointer flex items-center sidebar-active';
            
            // 切换面包屑
            const titles = {'dash': '平台概览', 'merchants': '租户/商家管理', 'plans': '套餐订阅控制', 'logs': '系统审计'};
            document.getElementById('breadcrumb').innerText = titles[id];
        }
    </script>
</body>
</html>""",
}

zip_name = "SaaS_Super_Admin_MVP.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for filename, content in files.items():
        with open(filename, 'w', encoding='utf-8') as f: f.write(content)
        zipf.write(filename)
        os.remove(filename)

print(f"SaaS 总后台原型生成成功: {os.path.abspath(zip_name)}")