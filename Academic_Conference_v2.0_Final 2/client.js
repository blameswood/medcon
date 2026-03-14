
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
}