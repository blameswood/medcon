
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
}