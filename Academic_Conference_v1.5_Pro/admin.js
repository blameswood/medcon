
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
}