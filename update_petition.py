#!/usr/bin/env python3
"""Update petition counter sections in all language files for live Google Sheets integration."""

def apply(path, replacements, label):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    applied = 0
    missed = []
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new, 1)
            applied += 1
        else:
            missed.append(old)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"{label}: Applied {applied}/{len(replacements)}")
    if missed:
        for m in missed:
            print(f"  MISSED: {m[:80]}...")
    return applied, missed

# === SHARED replacements (identical across all files) ===
shared = [
    # Comment
    ('<!-- SIGN THE PETITION -->\n<!-- UPDATE PETITION COUNT HERE',
     '<!-- SIGN THE PETITION — Live counter updates from Google Sheets -->\n<!-- UPDATE PETITION COUNT HERE'),
    # Main count
    ('<div class="petition-number" id="petition-count">2,378+</div>',
     '<div class="petition-number" id="petition-count">12,830+</div>'),
    # Progress bar - add ID and update width
    ('<div class="petition-fill" style="width:47.6%"></div>',
     '<div class="petition-fill" id="petition-fill" style="width:85.5%"></div>'),
    # Bar label - add ID and update numbers
    ('<div class="petition-bar-label">2,378 / 5,000</div>',
     '<div class="petition-bar-label" id="petition-bar-label">12,830 / 15,000</div>'),
    # Script tag before GoatCounter
    ('<!-- GoatCounter Analytics (privacy-friendly, no cookies) -->',
     '<!-- Live petition counter from Google Sheets -->\n<script src="petition-counter.js"></script>\n\n<!-- GoatCounter Analytics (privacy-friendly, no cookies) -->'),
]

# === ES ===
es = shared + [
    ('firmas — meta: 5.000',
     'firmas en todas las peticiones — meta: 15.000'),
    ('Salva Simonds Elementary y Detén los Cierres',
     'Salvemos Nuestras Escuelas y Detengamos los Cierres'),
    # Join text
    ('>Únete a más de 2.378 personas que ya han firmado →</a>',
     ' id="petition-join-text" data-prefix="Únete a más de " data-suffix=" personas que ya han firmado →">Únete a más de 12,830 personas que ya han firmado →</a>'),
    # Sticky button
    ('>✍️ Firma la petición (2.378+)</a>',
     ' id="sticky-petition-btn" data-prefix="✍️ Firma la petición (" data-suffix="+)">✍️ Firma la petición (12,830+)</a>'),
    # Breakdown div after </div>\n</div> of petition-counter
    ('</div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">Salvemos Nuestras Escuelas',
     '</div>\n<div id="petition-breakdown" data-breakdown-label="Firmas por petición:" style="margin-top:15px;text-align:left;font-size:0.85em;color:#555;max-width:400px;margin-left:auto;margin-right:auto;display:none;"></div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">Salvemos Nuestras Escuelas'),
]

# === KO ===
ko = shared + [
    ('서명 — 목표: 5,000',
     '모든 청원 서명 — 목표: 15,000'),
    ('Simonds 초등학교를 지키고 폐교를 막자',
     '우리 학교를 지키고 폐교를 막자'),
    # Join text
    ('>이미 서명한 2,378명 이상과 함께하세요 →</a>',
     ' id="petition-join-text" data-prefix="이미 서명한 " data-suffix="명 이상과 함께하세요 →">이미 서명한 12,830명 이상과 함께하세요 →</a>'),
    # Sticky button
    ('>✍️ 청원 서명 (2,378+)</a>',
     ' id="sticky-petition-btn" data-prefix="✍️ 청원 서명 (" data-suffix="+)">✍️ 청원 서명 (12,830+)</a>'),
    # Breakdown div
    ('</div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">우리 학교를 지키고',
     '</div>\n<div id="petition-breakdown" data-breakdown-label="청원별 서명 수:" style="margin-top:15px;text-align:left;font-size:0.85em;color:#555;max-width:400px;margin-left:auto;margin-right:auto;display:none;"></div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">우리 학교를 지키고'),
]

# === VI ===
vi = shared + [
    ('chữ ký — mục tiêu: 5.000',
     'chữ ký trên tất cả các kiến nghị — mục tiêu: 15.000'),
    ('Cứu Trường Tiểu học Simonds &amp; Ngăn Đóng Cửa',
     'Cứu Trường Học Của Chúng Ta &amp; Ngăn Đóng Cửa'),
    # Join text
    ('>Tham gia cùng hơn 2.378 người đã ký →</a>',
     ' id="petition-join-text" data-prefix="Tham gia cùng hơn " data-suffix=" người đã ký →">Tham gia cùng hơn 12,830 người đã ký →</a>'),
    # Sticky button
    ('>✍️ Ký kiến nghị (2.378+)</a>',
     ' id="sticky-petition-btn" data-prefix="✍️ Ký kiến nghị (" data-suffix="+)">✍️ Ký kiến nghị (12,830+)</a>'),
    # Breakdown div
    ('</div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">Cứu Trường Học Của Chúng Ta',
     '</div>\n<div id="petition-breakdown" data-breakdown-label="Chữ ký theo kiến nghị:" style="margin-top:15px;text-align:left;font-size:0.85em;color:#555;max-width:400px;margin-left:auto;margin-right:auto;display:none;"></div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">Cứu Trường Học Của Chúng Ta'),
]

# === ZH ===
zh = shared + [
    ('签名 — 目标：5,000',
     '所有请愿书签名 — 目标：15,000'),
    ('拯救Simonds小学，阻止学校关闭',
     '拯救我们的学校，阻止学校关闭'),
    # Join text
    ('>加入已签名的2,378+人 →</a>',
     ' id="petition-join-text" data-prefix="加入已签名的" data-suffix="+人 →">加入已签名的12,830+人 →</a>'),
    # Sticky button
    ('>✍️ 签署请愿书（2,378+）</a>',
     ' id="sticky-petition-btn" data-prefix="✍️ 签署请愿书（" data-suffix="+）">✍️ 签署请愿书（12,830+）</a>'),
    # Breakdown div
    ('</div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">拯救我们的学校',
     '</div>\n<div id="petition-breakdown" data-breakdown-label="各请愿书签名数：" style="margin-top:15px;text-align:left;font-size:0.85em;color:#555;max-width:400px;margin-left:auto;margin-right:auto;display:none;"></div>\n<div style="font-size:1.1em;color:#333;margin-bottom:5px;">拯救我们的学校'),
]

apply('es.html', es, 'ES')
apply('ko.html', ko, 'KO')
apply('vi.html', vi, 'VI')
apply('zh.html', zh, 'ZH')
