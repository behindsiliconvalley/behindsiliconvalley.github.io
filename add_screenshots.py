#!/usr/bin/env python3
"""Add SACS filing screenshots to all language files."""

configs = {
    'es.html': {
        'header': 'Declaración SACS Oficial — SJUSD Datos Reales No Auditados 2023–24',
        'cap1': 'Resumen de Ingresos vs. Gastos',
        'cap2': 'Componentes del Balance de Fondos — A dónde van los $109M',
        'cap3': 'Beneficios de Empleados — Costos de Salud y Bienestar +25%',
        'footer': 'Fuente: California Dept of Education, SACS Financial Reporting Software v11. Verificar en',
        'marker': '<div class="co-h">Espera — el distrito tiene $109M en balance de fondos. ¿Dónde está?</div>'
    },
    'ko.html': {
        'header': '공식 SACS 보고서 — SJUSD 비감사 실적 2023–24',
        'cap1': '수입 vs. 지출 요약',
        'cap2': '기금 잔액 구성 — $109M의 행방',
        'cap3': '직원 복리후생 — 건강·복지 비용 +25%',
        'footer': '출처: California Dept of Education, SACS Financial Reporting Software v11. 확인:',
        'marker': '<div class="co-h">잠깐 — 교육구에 기금 잔액이 $109M 있는데, 어디에 있나요?</div>'
    },
    'vi.html': {
        'header': 'Báo Cáo SACS Chính Thức — SJUSD Thực Tế Chưa Kiểm Toán 2023–24',
        'cap1': 'Tóm tắt Thu nhập vs. Chi tiêu',
        'cap2': 'Thành phần Số dư Quỹ — $109 triệu đi đâu',
        'cap3': 'Phúc lợi Nhân viên — Chi phí Sức khỏe &amp; Phúc lợi +25%',
        'footer': 'Nguồn: California Dept of Education, SACS Financial Reporting Software v11. Xác minh tại',
        'marker': '<div class="co-h">Khoan — học khu có $109 triệu trong số dư quỹ. Nó ở đâu?</div>'
    },
    'zh.html': {
        'header': '官方SACS报告 — SJUSD 2023–24未审计实际数据',
        'cap1': '收入 vs. 支出摘要',
        'cap2': '基金余额构成 — $1.094亿的去向',
        'cap3': '员工福利 — 健康与福利成本 +25%',
        'footer': '来源：California Dept of Education, SACS Financial Reporting Software v11。查验：',
        'marker': '<div class="co-h">等等 — 学区有$1.094亿的基金余额。钱在哪里？</div>'
    }
}

screenshot_template = '''
<!-- SACS Filing Screenshots -->
<div style="margin:24px 0;background:#fff;border:1px solid var(--border);border-radius:12px;padding:20px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--slate);margin-bottom:12px;font-weight:600">{header}</div>
<div style="margin-bottom:16px">
<div style="font-size:13px;font-weight:600;color:var(--ink);margin-bottom:6px">{cap1}</div>
<img src="sacs_page1.png" alt="SJUSD SACS Unaudited Actuals 2023-24 — Revenue and Expenditure Summary" style="width:100%;border:1px solid #e2d8cc;border-radius:6px">
</div>
<div style="margin-bottom:16px">
<div style="font-size:13px;font-weight:600;color:var(--ink);margin-bottom:6px">{cap2}</div>
<img src="sacs_page2.png" alt="SJUSD SACS Unaudited Actuals 2023-24 — Fund Balance Components" style="width:100%;border:1px solid #e2d8cc;border-radius:6px">
</div>
<div>
<div style="font-size:13px;font-weight:600;color:var(--rust);margin-bottom:6px">{cap3}</div>
<img src="sacs_page8.png" alt="SJUSD SACS Unaudited Actuals 2023-24 — Employee Benefits" style="width:100%;border:1px solid #e2d8cc;border-radius:6px">
</div>
<div style="font-size:11px;color:#999;margin-top:10px;text-align:center">{footer} <a href="https://viewer.sacs-cde.org/" target="_blank" style="color:#999;text-decoration:underline">viewer.sacs-cde.org</a></div>
</div>

'''

for filename, cfg in configs.items():
    filepath = f'/Users/haniagarcia/Documents/behindsilliconvalley/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    insert_html = screenshot_template.format(**cfg)

    marker = cfg['marker']
    old = '<div class="co i">\n' + marker
    new = insert_html + '<div class="co i">\n' + marker

    count = content.count(old)
    content = content.replace(old, new, 1)  # Only replace first occurrence

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'{filename}: {count} found, inserted')

print('Done!')
