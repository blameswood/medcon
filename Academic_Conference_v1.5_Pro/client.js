
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
}