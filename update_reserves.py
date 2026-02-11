#!/usr/bin/env python3
"""Update reserve section in all language files with Unaudited Actuals data."""

import re

# Source citation replacement (same pattern in all 4 files)
old_source = 'CDE SACS Data Viewer — SJUSD Unaudited Actuals, Fund 01, Column BA (<a href="https://viewer.sacs-cde.org/" target="_blank">viewer.sacs-cde.org</a>). Reserve standard:'
new_source = 'SJUSD Unaudited Actuals 2023–24, SACS Financial Reporting Software v11, Fund 01 — General Fund, printed 3/4/2025 (<a href="https://viewer.sacs-cde.org/" target="_blank">CDE SACS Data Viewer</a>). Reserve standard:'

# Per-language replacements
configs = {
    'es.html': {
        'old_callout': '''<div class="co i">
<div class="co-h">Espera — el distrito tiene $109M en balance de fondos. ¿Dónde está?</div>
<p>El balance total de fondos de SJUSD fue $109,4M en 2023–24. Pero <strong>$104,2M de eso está restringido</strong> — legalmente destinado a programas específicos (educación especial, subvenciones federales, etc.) y no puede usarse para operaciones generales. Solo <strong>$5,2M no tiene restricciones</strong>, y de eso, solo $1,3M está en cuentas sin asignar. La Reserva designada para Incertidumbres Económicas del distrito — la partida real de red de seguridad — es <strong>cero</strong>.</p>
<p style="margin-bottom:0">Esto significa que SJUSD ha estado operando por debajo de la reserva mínima recomendada por el estado durante al menos dos años consecutivos. Se supone que la Oficina de Educación del Condado debe señalar esto. Un distrito con un déficit de $30,3M en 2024–25 y esencialmente sin reservas no restringidas está en serio peligro fiscal.</p>
</div>''',
        'new_callout': '''<div class="co i">
<div class="co-h">Espera — el distrito tiene $109M en balance de fondos. ¿Dónde está?</div>
<p>El balance total de fondos de SJUSD fue <strong>$109,367,369</strong> en 2023–24. Pero así es como se distribuye realmente — casi nada está disponible:</p>

<!-- Fund Balance Waterfall Graphic -->
<div style="margin:16px 0 20px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;color:var(--slate);font-weight:600">A dónde van los $109.4M realmente (2023–24)</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Balance total de fondos</div>
<div style="height:28px;background:#1565c0;border-radius:6px;position:relative;margin-bottom:12px">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$109.4M</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Restringido — designado legalmente, no se puede tocar</div>
<div style="height:28px;background:#ef5350;border-radius:6px;position:relative;margin-bottom:12px;width:95.2%">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$104.2M (95.2%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Asignado — comprometido para propósitos específicos</div>
<div style="height:28px;background:#ff9800;border-radius:6px;position:relative;margin-bottom:12px;width:3.5%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#ff9800">$3.8M (3.5%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">No gastable — efectivo rotatorio, artículos prepagados</div>
<div style="height:28px;background:#9e9e9e;border-radius:6px;position:relative;margin-bottom:12px;width:1%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#9e9e9e">$0.1M (0.1%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--rust);font-weight:700">Sin asignar — la red de seguridad real</div>
<div style="height:28px;background:var(--rust);border-radius:6px;position:relative;margin-bottom:4px;width:1.2%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;color:var(--rust)">$1.3M (0.27% de los gastos)</div>
</div>
<div style="font-size:11px;color:var(--rust);font-style:italic;margin-top:2px">El estado requiere 2% = $9.5M → SJUSD tiene un déficit de $8.3M</div>
</div>

<p>De los <strong>$104.2M restringidos</strong>, las mayores porciones son: $48.1M Otros Locales Restringidos, $21.5M Subvención de Emergencia para Recuperación del Aprendizaje, $15.1M Subvención de Artes/Música, $7.0M Aprendizaje Expandido, y $3.6M cuentas de mantenimiento. Estos fondos están legalmente destinados y <strong>no pueden ser redirigidos</strong> para cubrir déficits operativos.</p>
<p>Los <strong>$5.2M no restringidos</strong> restantes se desglosan en: $3.8M asignados (cuentas de flexibilidad escolar y otros compromisos), $0.1M no gastable (efectivo rotatorio, artículos prepagados), y solo <strong>$1.27M sin asignar</strong>. La línea de Reserva para Incertidumbres Económicas (Código de Objeto 9789) muestra <strong>$0</strong>.</p>
<p style="margin-bottom:0">Esto significa que SJUSD ha estado operando por debajo de la reserva mínima recomendada por el estado durante al menos dos años consecutivos. Se supone que la Oficina de Educación del Condado debe señalar esto. Un distrito con un déficit de $30,3M en 2024–25 y esencialmente sin reservas no restringidas está en serio peligro fiscal.</p>
</div>

<!-- Health & Welfare Benefits Explosion -->
<div class="co w">
<div class="co-h">La Explosión de Costos Oculta: Beneficios de Empleados +25%</div>
<p>Los Datos Reales No Auditados revelan un aumento masivo en los costos de beneficios de empleados que ayuda a explicar el déficit:</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:12px 0;text-align:center">
<div style="background:#fff3cd;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--slate)">Salud y Bienestar 2023–24</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900">$47.3M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">Salud y Bienestar 2024–25</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">$59.2M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">Aumento</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">+$11.9M (+25.2%)</div>
</div>
</div>
<p style="margin-bottom:0">Los beneficios de salud y bienestar solos aumentaron <strong>$11.9 millones en un solo año</strong> — un aumento del 25.2%. Los beneficios totales de empleados subieron de $124.4M a $136.7M (+9.9%). Esto coincide con las denuncias sindicales de más de $30M en beneficios subfinanciados desde 2017–18. La pregunta es: ¿por qué no se planificaron estos costos, y por qué el cierre de escuelas es la solución propuesta?</p>
</div>'''
    },
    'ko.html': {
        'old_callout': '''<div class="co i">
<div class="co-h">잠깐 — 교육구에 기금 잔액이 $109M 있는데, 어디에 있나요?</div>
<p>SJUSD의 2023–24년 총 기말 기금 잔액은 $109.4M이었습니다. 하지만 <strong>그 중 $104.2M은 제한 자금</strong>입니다 — 특정 프로그램(특수교육, 연방 보조금 등)에 법적으로 지정되어 일반 운영에 사용할 수 없습니다. <strong>비제한 자금은 $5.2M</strong>에 불과하며, 그 중 미배정 계좌에 있는 금액은 $1.3M뿐입니다. 교육구의 지정된 경제적 불확실성 적립금 — 실제 안전망 항목 — 은 <strong>0</strong>입니다.</p>
<p style="margin-bottom:0">이는 SJUSD가 최소 2년 연속 주 권장 최소 적립금 이하로 운영되어 왔음을 의미합니다. 카운티 교육청은 이를 경고해야 합니다. 2024–25년에 $30.3M 적자를 운영하면서 사실상 비제한 적립금이 없는 교육구는 심각한 재정 위기에 처해 있습니다.</p>
</div>''',
        'new_callout': '''<div class="co i">
<div class="co-h">잠깐 — 교육구에 기금 잔액이 $109M 있는데, 어디에 있나요?</div>
<p>SJUSD의 2023–24년 총 기말 기금 잔액은 <strong>$109,367,369</strong>입니다. 하지만 실제 분포를 보면 — 사용 가능한 금액은 거의 없습니다:</p>

<!-- Fund Balance Waterfall Graphic -->
<div style="margin:16px 0 20px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;color:var(--slate);font-weight:600">$1.094억의 실제 사용처 (2023–24)</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">총 기금 잔액</div>
<div style="height:28px;background:#1565c0;border-radius:6px;position:relative;margin-bottom:12px">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$109.4M</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">제한 자금 — 법적으로 지정됨, 사용 불가</div>
<div style="height:28px;background:#ef5350;border-radius:6px;position:relative;margin-bottom:12px;width:95.2%">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$104.2M (95.2%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">배정 — 특정 목적에 약속됨</div>
<div style="height:28px;background:#ff9800;border-radius:6px;position:relative;margin-bottom:12px;width:3.5%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#ff9800">$3.8M (3.5%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">비지출성 — 회전 현금, 선급 항목</div>
<div style="height:28px;background:#9e9e9e;border-radius:6px;position:relative;margin-bottom:12px;width:1%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#9e9e9e">$0.1M (0.1%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--rust);font-weight:700">미배정 — 실제 안전망</div>
<div style="height:28px;background:var(--rust);border-radius:6px;position:relative;margin-bottom:4px;width:1.2%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;color:var(--rust)">$1.3M (지출의 0.27%)</div>
</div>
<div style="font-size:11px;color:var(--rust);font-style:italic;margin-top:2px">주 요구 2% = $9.5M → SJUSD $8.3M 부족</div>
</div>

<p><strong>제한 자금 $104.2M</strong>의 주요 구성: 기타 제한 지역 자금 $48.1M, 학습 회복 긴급 보조금 $21.5M, 예술/음악 보조금 $15.1M, 확장 학습 $7.0M, 유지보수 계좌 $3.6M. 이 자금은 법적으로 지정되어 있으며 운영 적자를 메우는 데 <strong>전용할 수 없습니다</strong>.</p>
<p>나머지 <strong>비제한 자금 $5.2M</strong>의 구성: 배정 $3.8M (학교 유연성 계좌 및 기타), 비지출성 $0.1M (회전 현금, 선급 항목), 그리고 <strong>미배정 $1.27M</strong>만 남습니다. 경제적 불확실성 적립금 항목(Object Code 9789)은 <strong>$0</strong>입니다.</p>
<p style="margin-bottom:0">이는 SJUSD가 최소 2년 연속 주 권장 최소 적립금 이하로 운영되어 왔음을 의미합니다. 카운티 교육청은 이를 경고해야 합니다. 2024–25년에 $30.3M 적자를 운영하면서 사실상 비제한 적립금이 없는 교육구는 심각한 재정 위기에 처해 있습니다.</p>
</div>

<div class="co w">
<div class="co-h">숨겨진 비용 폭발: 직원 복리후생 +25%</div>
<p>비감사 실적 보고서는 적자를 설명하는 직원 복리후생 비용의 대폭 증가를 보여줍니다:</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:12px 0;text-align:center">
<div style="background:#fff3cd;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--slate)">건강·복지 2023–24</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900">$47.3M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">건강·복지 2024–25</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">$59.2M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">증가</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">+$11.9M (+25.2%)</div>
</div>
</div>
<p style="margin-bottom:0">건강·복지 혜택만 <strong>1년 만에 $1,190만 증가</strong> — 25.2% 상승. 총 직원 복리후생은 $124.4M에서 $136.7M으로 (+9.9%) 증가했습니다. 이는 노조가 주장한 2017–18년 이후 $30M 이상의 복리후생 미적립과 일치합니다. 질문은: 왜 이 비용을 계획하지 않았으며, 왜 학교 폐교가 해결책인가?</p>
</div>'''
    },
    'vi.html': {
        'old_callout': '''<div class="co i">
<div class="co-h">Khoan — học khu có $109 triệu trong số dư quỹ. Nó ở đâu?</div>
<p>Tổng số dư quỹ cuối kỳ của SJUSD là $109,4 triệu trong năm 2023–24. Nhưng <strong>$104,2 triệu trong số đó bị hạn chế</strong> — được chỉ định hợp pháp cho các chương trình cụ thể (giáo dục đặc biệt, trợ cấp liên bang, v.v.) và không thể sử dụng cho hoạt động chung. Chỉ <strong>$5,2 triệu không bị hạn chế</strong>, và trong số đó, chỉ $1,3 triệu nằm trong tài khoản chưa phân bổ. Dự trữ cho Bất trắc Kinh tế được chỉ định của học khu — mục lưới an toàn thực sự — là <strong>không</strong>.</p>
<p style="margin-bottom:0">Điều này có nghĩa là SJUSD đã hoạt động dưới mức dự trữ tối thiểu được tiểu bang khuyến nghị trong ít nhất hai năm liên tiếp. Văn phòng Giáo dục Quận lẽ ra phải cảnh báo điều này. Một học khu chạy thâm hụt $30,3 triệu trong năm 2024–25 mà gần như không có dự trữ không hạn chế đang trong nguy hiểm tài chính nghiêm trọng.</p>
</div>''',
        'new_callout': '''<div class="co i">
<div class="co-h">Khoan — học khu có $109 triệu trong số dư quỹ. Nó ở đâu?</div>
<p>Tổng số dư quỹ cuối kỳ của SJUSD là <strong>$109,367,369</strong> trong năm 2023–24. Nhưng đây là cách nó thực sự phân bổ — gần như không có gì khả dụng:</p>

<!-- Fund Balance Waterfall Graphic -->
<div style="margin:16px 0 20px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;color:var(--slate);font-weight:600">$109.4 triệu thực sự đi đâu (2023–24)</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Tổng số dư quỹ</div>
<div style="height:28px;background:#1565c0;border-radius:6px;position:relative;margin-bottom:12px">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$109.4M</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Bị hạn chế — chỉ định hợp pháp, không thể sử dụng</div>
<div style="height:28px;background:#ef5350;border-radius:6px;position:relative;margin-bottom:12px;width:95.2%">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$104.2M (95.2%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Đã phân bổ — cam kết cho mục đích cụ thể</div>
<div style="height:28px;background:#ff9800;border-radius:6px;position:relative;margin-bottom:12px;width:3.5%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#ff9800">$3.8M (3.5%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">Không thể chi tiêu — tiền mặt quay vòng, mục trả trước</div>
<div style="height:28px;background:#9e9e9e;border-radius:6px;position:relative;margin-bottom:12px;width:1%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#9e9e9e">$0.1M (0.1%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--rust);font-weight:700">Chưa phân bổ — lưới an toàn thực sự</div>
<div style="height:28px;background:var(--rust);border-radius:6px;position:relative;margin-bottom:4px;width:1.2%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;color:var(--rust)">$1.3M (0.27% chi tiêu)</div>
</div>
<div style="font-size:11px;color:var(--rust);font-style:italic;margin-top:2px">Tiểu bang yêu cầu 2% = $9.5M → SJUSD thiếu $8.3M</div>
</div>

<p>Trong <strong>$104.2 triệu bị hạn chế</strong>, các phần lớn nhất là: $48.1M Khác Hạn Chế Địa Phương, $21.5M Trợ cấp Khẩn Cấp Phục Hồi Học Tập, $15.1M Trợ cấp Nghệ thuật/Âm nhạc, $7.0M Học Tập Mở Rộng, và $3.6M tài khoản bảo trì. Những quỹ này được chỉ định hợp pháp và <strong>không thể chuyển hướng</strong> để bù đắp thâm hụt hoạt động.</p>
<p><strong>$5.2 triệu không hạn chế</strong> còn lại phân bổ như sau: $3.8M đã phân bổ (tài khoản linh hoạt trường và cam kết khác), $0.1M không thể chi tiêu (tiền mặt quay vòng, mục trả trước), và chỉ <strong>$1.27M chưa phân bổ</strong>. Mục Dự trữ cho Bất trắc Kinh tế (Mã Đối tượng 9789) hiển thị <strong>$0</strong>.</p>
<p style="margin-bottom:0">Điều này có nghĩa là SJUSD đã hoạt động dưới mức dự trữ tối thiểu được tiểu bang khuyến nghị trong ít nhất hai năm liên tiếp. Văn phòng Giáo dục Quận lẽ ra phải cảnh báo điều này. Một học khu chạy thâm hụt $30,3 triệu trong năm 2024–25 mà gần như không có dự trữ không hạn chế đang trong nguy hiểm tài chính nghiêm trọng.</p>
</div>

<div class="co w">
<div class="co-h">Chi Phí Ẩn Bùng Nổ: Phúc Lợi Nhân Viên +25%</div>
<p>Báo cáo Thực tế Chưa Kiểm toán cho thấy chi phí phúc lợi nhân viên tăng đột biến, giúp giải thích thâm hụt:</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:12px 0;text-align:center">
<div style="background:#fff3cd;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--slate)">Sức khỏe & Phúc lợi 2023–24</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900">$47.3M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">Sức khỏe & Phúc lợi 2024–25</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">$59.2M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">Tăng</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">+$11.9M (+25.2%)</div>
</div>
</div>
<p style="margin-bottom:0">Riêng phúc lợi sức khỏe đã tăng <strong>$11.9 triệu trong một năm</strong> — tăng 25.2%. Tổng phúc lợi nhân viên tăng từ $124.4M lên $136.7M (+9.9%). Điều này phù hợp với tuyên bố của công đoàn về hơn $30M phúc lợi thiếu hụt từ 2017–18. Câu hỏi là: tại sao chi phí này không được lên kế hoạch, và tại sao đóng cửa trường là giải pháp được đề xuất?</p>
</div>'''
    },
    'zh.html': {
        'old_callout': '''<div class="co i">
<div class="co-h">等等 — 学区有$1.094亿的基金余额。钱在哪里？</div>
<p>SJUSD在2023–24年的期末基金余额为$1.094亿。但<strong>其中$1.042亿是受限资金</strong> — 法律规定用于特定项目（特殊教育、联邦拨款等），不能用于一般运营。仅<strong>$520万是非受限的</strong>，其中只有$130万在未分配账户中。学区指定的经济不确定性储备金 — 实际的安全网项目 — 为<strong>零</strong>。</p>
<p style="margin-bottom:0">这意味着SJUSD至少连续两年在低于州推荐最低储备标准的情况下运营。县教育办公室本应对此发出警告。一个在2024–25年运行$3030万赤字且基本没有非受限储备金的学区正处于严重的财务危险之中。</p>
</div>''',
        'new_callout': '''<div class="co i">
<div class="co-h">等等 — 学区有$1.094亿的基金余额。钱在哪里？</div>
<p>SJUSD在2023–24年的期末基金余额为<strong>$109,367,369</strong>。但以下是资金的实际分配 — 几乎没有可用资金：</p>

<!-- Fund Balance Waterfall Graphic -->
<div style="margin:16px 0 20px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;margin-bottom:10px;color:var(--slate);font-weight:600">$1.094亿的实际去向（2023–24）</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">基金余额总额</div>
<div style="height:28px;background:#1565c0;border-radius:6px;position:relative;margin-bottom:12px">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$109.4M</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">受限资金 — 法律指定，不可动用</div>
<div style="height:28px;background:#ef5350;border-radius:6px;position:relative;margin-bottom:12px;width:95.2%">
<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#fff;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600">$104.2M (95.2%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">已分配 — 用于特定用途</div>
<div style="height:28px;background:#ff9800;border-radius:6px;position:relative;margin-bottom:12px;width:3.5%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#ff9800">$3.8M (3.5%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--slate)">不可支出 — 周转现金、预付项目</div>
<div style="height:28px;background:#9e9e9e;border-radius:6px;position:relative;margin-bottom:12px;width:1%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:600;color:#9e9e9e">$0.1M (0.1%)</div>
</div>

<div style="margin-bottom:4px;font-size:12px;color:var(--rust);font-weight:700">未分配 — 实际的安全网</div>
<div style="height:28px;background:var(--rust);border-radius:6px;position:relative;margin-bottom:4px;width:1.2%">
<div style="position:absolute;left:100%;padding-left:8px;white-space:nowrap;display:flex;align-items:center;height:100%;font-family:'JetBrains Mono',monospace;font-size:13px;font-weight:700;color:var(--rust)">$1.3M（支出的0.27%）</div>
</div>
<div style="font-size:11px;color:var(--rust);font-style:italic;margin-top:2px">州要求2% = $950万 → SJUSD缺口$830万</div>
</div>

<p>在<strong>受限资金$1.042亿</strong>中，最大部分为：其他受限地方资金$4810万、学习恢复紧急拨款$2150万、艺术/音乐拨款$1510万、扩展学习$700万、维护账户$360万。这些资金有法律指定用途，<strong>不能挪用</strong>来填补运营赤字。</p>
<p>剩余<strong>非受限资金$520万</strong>分解为：已分配$380万（学校灵活性账户和其他承诺）、不可支出$10万（周转现金、预付项目），以及仅<strong>$127万未分配</strong>。经济不确定性储备金项目（对象代码9789）显示为<strong>$0</strong>。</p>
<p style="margin-bottom:0">这意味着SJUSD至少连续两年在低于州推荐最低储备标准的情况下运营。县教育办公室本应对此发出警告。一个在2024–25年运行$3030万赤字且基本没有非受限储备金的学区正处于严重的财务危险之中。</p>
</div>

<div class="co w">
<div class="co-h">隐藏的成本爆炸：员工福利 +25%</div>
<p>未审计实际报告显示员工福利成本大幅飙升，有助于解释赤字：</p>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:12px 0;text-align:center">
<div style="background:#fff3cd;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--slate)">健康与福利 2023–24</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900">$47.3M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">健康与福利 2024–25</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">$59.2M</div>
</div>
<div style="background:#fde8e8;padding:12px;border-radius:8px">
<div style="font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:var(--rust)">增加</div>
<div style="font-family:'Playfair Display',serif;font-size:1.5rem;font-weight:900;color:var(--rust)">+$11.9M (+25.2%)</div>
</div>
</div>
<p style="margin-bottom:0">仅健康与福利福利<strong>一年就增加了$1190万</strong> — 增长25.2%。员工福利总额从$1.244亿增至$1.367亿（+9.9%）。这与工会声称的2017–18年以来$3000万以上福利资金不足的说法一致。问题是：为什么这些成本没有被规划，为什么关闭学校是建议的解决方案？</p>
</div>'''
    }
}

for filename, cfg in configs.items():
    filepath = f'/Users/haniagarcia/Documents/behindsilliconvalley/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update source citation
    count1 = content.count(old_source)
    content = content.replace(old_source, new_source)

    # Update callout section
    count2 = content.count(cfg['old_callout'])
    content = content.replace(cfg['old_callout'], cfg['new_callout'])

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'{filename}: source={count1}, callout={count2}')

print('Done!')
