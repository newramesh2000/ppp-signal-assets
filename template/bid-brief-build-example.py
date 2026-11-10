def ann(c,r,n): return c*r/(1-(1+r)**-n)
S=2875*156
# ---------- chart: SAR per session per SAR100m capex vs term ----------
W,H=640,235; L,R,T,B=56,20,18,40
xs=list(range(3,16)); ymax=100
def X(n): return L+(n-3)/(15-3)*(W-L-R)
def Y(v): return T+(1-v/ymax)*(H-T-B)
def path(r): return ' '.join(('M' if i==0 else 'L')+f'{X(n):.1f},{Y(ann(100e6,r,n)/S):.1f}' for i,n in enumerate(xs))
grid=''.join(f'<line x1="{L}" x2="{W-R}" y1="{Y(v):.1f}" y2="{Y(v):.1f}" stroke="#DCE1DA"/><text x="{L-8}" y="{Y(v)+4:.1f}" text-anchor="end" font-size="11" fill="#526266">{v}</text>' for v in range(0,101,20))
xt=''.join(f'<text x="{X(n):.1f}" y="{H-B+18}" text-anchor="middle" font-size="11" fill="#526266">{n}</text>' for n in xs)
y6=ann(100e6,.08,6)/S; y15=ann(100e6,.08,15)/S
chart=f'''<svg viewBox="0 0 {W} {H}" width="100%" role="img" aria-label="SAR per dialysis session needed to recover SAR 100m of capex, by contract term">
{grid}{xt}
<rect x="{X(6)-14:.1f}" y="{T}" width="28" height="{H-T-B}" fill="#F3E7C9"/>
<path d="{path(0.10)}" fill="none" stroke="#D9B25F" stroke-width="3"/>
<path d="{path(0.08)}" fill="none" stroke="#2E6E68" stroke-width="3"/>
<circle cx="{X(6):.1f}" cy="{Y(y6):.1f}" r="5" fill="#102A2E"/><text x="{X(6)+10:.1f}" y="{Y(y6)-8:.1f}" font-size="12" font-weight="700" fill="#102A2E">6 yrs: SAR {y6:.0f}</text>
<circle cx="{X(15):.1f}" cy="{Y(y15):.1f}" r="5" fill="#102A2E"/><text x="{X(15)-6:.1f}" y="{Y(y15)-12:.1f}" text-anchor="end" font-size="12" font-weight="700" fill="#102A2E">15 yrs: SAR {y15:.0f}</text>
<text x="{(L+W-R)/2}" y="{H-6}" text-anchor="middle" font-size="12" fill="#3E4E52">Contract term (years)</text>
<text transform="translate(14,{(T+H-B)/2}) rotate(-90)" text-anchor="middle" font-size="12" fill="#3E4E52">SAR per session</text>
<line x1="{W-200}" x2="{W-180}" y1="{T+8}" y2="{T+8}" stroke="#2E6E68" stroke-width="3"/><text x="{W-174}" y="{T+12}" font-size="11.5" fill="#102A2E">8% cost of capital</text>
<line x1="{W-200}" x2="{W-180}" y1="{T+26}" y2="{T+26}" stroke="#D9B25F" stroke-width="3"/><text x="{W-174}" y="{T+30}" font-size="11.5" fill="#102A2E">10% cost of capital</text>
</svg>'''
rows=''.join(f'<tr><td>{n} years</td><td>{ann(100e6,.08,n)/1e6:.1f}</td><td><b>{ann(100e6,.08,n)/S:.0f}</b></td><td>{ann(100e6,.10,n)/S:.0f}</td></tr>' for n in (6,10,15))

# ---------- timeline ----------
tl=[('4 May 2026','EOI and RFQ launched','MoH, MoD &amp; NCP','done'),('15 Jun 2026','Qualification submissions due','3:00 pm Saudi time','done'),('4 Oct 2026','12 bidders qualified','5 consortia, 7 single entities','done'),('Not published','RFP issue','Package scopes and payment terms','next'),('Not published','Bids, preferred bidder, award','','future'),('After award','Six-year service term','DRFM + clinical services','future')]
tlh=''.join(f'<div class="tl {s}"><span class="dot"></span><p class="d">{d}</p><p class="e">{e}</p><p class="n">{n}</p></div>' for d,e,n,s in tl)

bidders=[('National Medical Care Co. + NephroTech','Consortium'),('DiMed Saudi + SMC + Saedan','Consortium'),('Gulf Medical Co. + B. Braun','Consortium'),('NephroPlus + Faisaliah Medical Systems','Consortium'),('Weigao + Anfas','Consortium'),('Burjeel Arabia Healthcare','Single entity'),('DaVita Healthcare','Single entity'),('Diaverum Advanced Medical Services','Single entity'),('NephroCare Saudi Medical Co.','Single entity'),('US Renal Care','Single entity'),('Dr. Sulaiman Al Habib Medical Group','Single entity'),('Al Mana General Hospitals','Single entity')]
bh=''.join(f'<tr><td>{i+1}</td><td>{n}</td><td><span class="pill {"c" if t=="Consortium" else "s"}">{t}</span></td></tr>' for i,(n,t) in enumerate(bidders))

risks=[('Patient volume below plan','Wants a minimum service guarantee met','Needs a revenue floor before lending','Prices a volume band or walks'),
('Upgrade capex overrun','Fixed scope, fixed price','Sized on 6-year cash; little room','Carries the overrun; equity first loss'),
('Clinical quality and KPIs','Deductions tied to outcomes','Deductions cap matters for DSCR','Operator skill is the moat'),
('Staffing and Saudisation','Local-content targets','Cost line, rarely a lender issue','Wage and hiring risk for six years'),
('Consumables and drug prices','Seeks a stable tariff','Indexation protects margin','Pass-through or hedge via supplier'),
('Handback after year 6','Takes facilities and equipment back','Debt must be repaid by then','Residual value of equipment at risk')]
rh=''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in risks)

score=[('Offtaker strength','MoH / MoD are the counterparties',5),('Revenue certainty','Payment basis not yet published',2),('Tenor fit','Six years is short for capex recovery',2),('Construction risk','Re-purposed sites, not greenfield',4),('Operating risk','Clinical delivery for six years',2),('Competition','~3 qualified bidders per package',3),('Disclosure','RFP and package scopes pending',2)]
def dots(n): return ''.join(f'<i class="{"on" if k<n else ""}"></i>' for k in range(5))
sh=''.join(f'<tr><td>{a}</td><td>{b}</td><td><span class="dots">{dots(n)}</span> {n}/5</td></tr>' for a,b,n in score)
avg=sum(s for *_,s in score)/len(score)

qs=['Payment basis: per session, per patient, availability, or a mix?','Minimum volume or referral commitment per package?','Indexation formula for tariff, wages and consumables?','KPI regime: which clinical outcomes trigger deductions, and is there a cap?','Who owns equipment at handback, and at what condition?','Any extension option beyond six years?','Transfer of existing MoH / MoD staff: mandatory, optional, cost?','Limit on packages per bidder, and can one bid win two?','Integration with national health IT systems and data-hosting rules?','Termination compensation for each cause, including government default?','Treatment of home haemodialysis and peritoneal dialysis volumes in payment?','Bid bond, performance bond and parent-guarantee sizes?']
qh=''.join(f'<li>{q}</li>' for q in qs)

html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Inter,sans-serif;color:#102A2E;font-size:11.5px;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.pg{{width:210mm;height:297mm;padding:16mm 15mm 14mm;position:relative;background:#F3F5F1;page-break-after:always;overflow:hidden}}
.run{{display:flex;justify-content:space-between;font-size:9.5px;color:#6B777A;margin-bottom:9mm}}
.run b{{color:#102A2E}}
.foot{{position:absolute;left:15mm;right:15mm;bottom:9mm;display:flex;justify-content:space-between;align-items:center;font-size:9px;color:#6B777A}}
.pn{{background:#102A2E;color:#F3F5F1;font-weight:700;border-radius:999px;padding:2px 12px;font-size:10px}}
h2{{font-family:Inter;font-size:23px;font-weight:800;letter-spacing:-.3px;margin-bottom:3px}}
h2 .n{{display:inline-block;background:#2E6E68;color:#fff;font-size:12px;border-radius:5px;padding:2px 7px;margin-right:8px;vertical-align:4px}}
.rule{{width:62mm;height:3px;background:#2E6E68;margin:5px 0 12px}}
h3{{font-size:14px;font-weight:700;margin:14px 0 6px}}
p+p{{margin-top:6px}}
.lead{{font-size:12.5px;color:#26383C;margin-bottom:10px}}
.card{{background:#fff;border:1px solid #D7DCD4;border-radius:10px;padding:12px 14px;margin-top:10px}}
.card.bar{{border-left:4px solid #2E6E68}}
.lab{{font-size:9.5px;font-weight:700;letter-spacing:1.6px;text-transform:uppercase;color:#2E6E68;margin-bottom:5px}}
.lab.g{{color:#8A6420}}.lab.r{{color:#9A3B2E}}
table{{width:100%;border-collapse:collapse;font-size:11px}}
th{{background:#102A2E;color:#F3F5F1;text-align:left;font-weight:600;padding:7px 8px;font-size:10.5px}}
td{{padding:6px 8px;border-bottom:1px solid #E1E5DE;vertical-align:top;background:#fff}}
td:first-child{{font-weight:600}}
.tag{{display:inline-block;font-size:9px;font-weight:700;padding:1px 6px;border-radius:4px;color:#fff;letter-spacing:.3px;white-space:nowrap}}
.V{{background:#2E6E68}}.R{{background:#4C6E91}}.F{{background:#8A6420}}.A{{background:#6B4E8E}}.I{{background:#9A6A2E}}
.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}
.fig{{background:#fff;border:1px solid #D7DCD4;border-radius:10px;padding:12px 14px;margin-top:10px}}
.fign{{display:inline-block;background:#102A2E;color:#fff;font-size:9px;font-weight:700;padding:2px 6px;border-radius:4px;margin-right:6px}}
.figt{{font-size:13px;font-weight:700;margin:6px 0 4px}}
.wsw{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;border-top:1px solid #E1E5DE;margin-top:8px;padding-top:8px;font-size:10.5px;color:#3E4E52}}
.wsw b{{display:block;font-size:9px;letter-spacing:1.4px;color:#102A2E;margin-bottom:2px}}
/* timeline */
.tls{{display:grid;grid-template-columns:repeat(6,1fr);gap:0;margin-top:8px;position:relative}}
.tls:before{{content:"";position:absolute;left:4%;right:4%;top:7px;height:3px;background:#C9CFC6}}
.tl{{position:relative;padding-top:22px;padding-right:6px}}
.tl .dot{{position:absolute;top:1px;left:0;width:15px;height:15px;border-radius:50%;background:#2E6E68;border:3px solid #F3F5F1}}
.tl.next .dot{{background:#D9B25F}}.tl.future .dot{{background:#fff;border:3px solid #9AA6A2}}
.tl .d{{font-weight:700;font-size:11px}}.tl .e{{font-size:11px;margin-top:2px}}.tl .n{{font-size:9.5px;color:#6B777A;margin-top:2px}}
.pill{{font-size:9.5px;font-weight:700;border-radius:999px;padding:2px 8px}}
.pill.c{{background:#E3EEEC;color:#2E6E68}}.pill.s{{background:#F3E7C9;color:#8A6420}}
.dots i{{display:inline-block;width:8px;height:8px;border-radius:50%;background:#D7DCD4;margin-right:2px}}
.dots i.on{{background:#2E6E68}}
.verdict{{background:#102A2E;color:#F3F5F1;border-radius:12px;padding:14px 16px}}
.verdict .big{{font-size:20px;font-weight:800;color:#D9B25F;letter-spacing:.5px}}
.dt{{display:flex;flex-direction:column;gap:6px;margin-top:6px}}
.q{{display:grid;grid-template-columns:1fr 26px 1.25fr;gap:8px;align-items:center}}
.qb{{background:#FFF7E3;border:1px solid #E8D39C;border-radius:8px;padding:5px 9px;font-weight:600}}
.ar{{text-align:center;color:#8A6420;font-weight:700}}
.ob{{background:#fff;border:1px solid #D7DCD4;border-radius:8px;padding:5px 9px}}
.ob b{{color:#9A3B2E}}
ol.qs{{padding-left:18px;columns:2;column-gap:22px;font-size:11px}}
ol.qs li{{break-inside:avoid;margin-bottom:6px}}
/* cover */
.cover{{background:#102A2E;color:#F3F5F1}}
.cover .eb{{font-size:10px;font-weight:700;letter-spacing:2.4px;color:#7FC4BA;margin-top:12mm}}
.cover h1{{font-family:Lora,serif;font-size:44px;line-height:1.05;margin-top:10px}}
.cover h1 em{{color:#D9B25F}}
.cover .sub{{font-size:14px;color:#C9D6D3;margin-top:12px;max-width:150mm}}
.kp{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;margin-top:12mm}}
.kp div{{border-left:3px solid #2E6E68;padding-left:10px}}
.kp b{{display:block;font-size:30px;font-weight:800}}
.kp span{{font-size:10.5px;color:#C9D6D3}}
.toc{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10mm}}
.toc div{{background:#17393E;border:1px solid #2C5357;border-radius:8px;padding:9px 10px;font-size:11px;font-weight:600}}
.toc div b{{display:block;color:#D9B25F;font-size:13px}}
.legend{{display:flex;flex-wrap:wrap;gap:12px;font-size:10px;color:#C9D6D3;margin-top:8mm}}
.cover .foot{{color:#8FA6A3}}
.cv{{margin-top:10mm;background:#17393E;border:1px solid #D9B25F;border-radius:12px;padding:14px 16px}}
.cv .lab{{color:#D9B25F}}
.cv p{{font-size:13px;color:#F3F5F1}}
</style></head><body>

<section class="pg cover">
<div class="run" style="color:#8FA6A3"><span>PPP Architecture Series</span><span>Bid Decision Brief No. 01</span></div>
<p class="eb">BID DECISION BRIEF · SAUDI ARABIA · HEALTHCARE · 10 NOVEMBER 2026</p>
<h1>Saudi National Dialysis PPP:<br><em>bid, partner or pass?</em></h1>
<p class="sub">Four packages, twelve qualified bidders and six years to make it pay. What a bid team should decide before the RFP lands.</p>
<div class="kp"><div><b>11,500+</b><span>patients, minimum</span></div><div><b>4</b><span>regional packages</span></div><div><b>12</b><span>bidders qualified</span></div><div><b>6 yrs</b><span>DRFM + clinical term</span></div></div>
<div class="cv"><p class="lab">Bottom line for bid teams</p><p><b style="color:#D9B25F">Conditional bid.</b> Integrated renal operators with Saudi delivery capacity should prepare for one or two packages and price upgrade capex to a six-year recovery. Hospital groups without renal scale should partner. Financial investors should not lead.</p></div>
<div class="toc"><div><b>1</b>Deal snapshot</div><div><b>2</b>Procurement clock</div><div><b>3</b>Contract architecture</div><div><b>4</b>Capex-recovery maths</div><div><b>5</b>Competitive field</div><div><b>6</b>Risk allocation</div><div><b>7</b>Bid decision</div><div><b>8</b>RFP questions</div></div>
<div class="legend"><span><span class="tag V">VERIFIED</span> official notice</span><span><span class="tag R">REPORTED</span> reputable press</span><span><span class="tag F">FORMULA</span> computed, inputs shown</span><span><span class="tag I">ILLUSTRATIVE</span> assumed inputs</span><span><span class="tag A">ASSESSMENT</span> author’s judgement</span></div>
<div class="foot"><span>Ramesh Radhakrishnaraja, FCA · PPP &amp; project finance · Not legal or investment advice</span><span class="pn" style="background:#D9B25F;color:#102A2E">1</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>1–2 · Snapshot &amp; clock</b></div>
<h2><span class="n">1</span>Deal snapshot</h2><div class="rule"></div>
<p class="lead">A national programme to buy chronic kidney disease and dialysis care from the private sector, packaged regionally and procured by the Ministry of Health, the Ministry of Defense and the National Center for Privatization (NCP).</p>
<table><tr><th style="width:27%">Item</th><th>What is on the record</th><th style="width:15%">Basis</th></tr>
<tr><td>Procurers</td><td>Ministry of Health, Ministry of Defense, National Center for Privatization &amp; PPP</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Model</td><td>PPP under a Design, Re-employ, Finance and Maintain (DRFM) framework, plus clinical services</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Term</td><td>Six-year contract</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Scale</td><td>At least 11,500 beneficiaries nationwide</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Packaging</td><td>Four clusters spanning several regions; final division set during bidding</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Private scope</td><td>Provide and upgrade facilities and equipment, run health IT, hire clinical and admin staff, run daily operations; in-centre and home haemodialysis, peritoneal dialysis, specialist outpatient care</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Field</td><td>12 qualified: 5 consortia and 7 single entities (4 Oct 2026)</td><td><span class="tag V">VERIFIED</span></td></tr>
<tr><td>Not yet public</td><td>Package boundaries, payment basis, tariff, KPI and deduction regime, capex estimate, RFP and bid dates</td><td><span class="tag V">VERIFIED</span> gap</td></tr>
</table>
<h2 style="margin-top:22px"><span class="n">2</span>Procurement clock</h2><div class="rule"></div>
<div class="fig"><span class="fign">FIGURE 1</span><span class="tag V">VERIFIED</span> dates from MoH notices
<p class="figt">From qualification to RFP: the next gate has no published date</p>
<div class="tls">{tlh}</div>
<div class="wsw"><div><b>WHAT IT SHOWS</b>Each confirmed step since May 2026, and the steps still to come.</div><div><b>HOW TO READ IT</b>Teal = done. Gold = next gate. Grey = after award.</div><div><b>WHY IT MATTERS</b>Bid teams have a quiet window now to form consortia and model capex before the RFP fixes the rules.</div></div></div>
<div class="card bar"><p class="lab">At a glance</p><p><b>Time between gates so far:</b> 42 days from launch to submissions; 111 days from submissions to qualification <span class="tag F">FORMULA</span>. At a similar pace, teams that start pricing only when the RFP arrives will be short of time.</p></div>
<div class="foot"><span>Sources: Saudi MoH notices of 4 May 2026 and 4 Oct 2026</span><span class="pn">2</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>3 · Contract architecture</b></div>
<h2><span class="n">3</span>Contract architecture</h2><div class="rule"></div>
<p class="lead">The private partner does not just run clinics. It upgrades buildings, buys equipment, runs IT and employs clinicians, then hands it all back after six years. That combination decides who can win and how it must be financed.</p>
<div class="fig"><span class="fign">FIGURE 2</span><span class="tag A">ASSESSMENT</span> structure as described in the MoH notice
<p class="figt">Who does what, per package</p>
<div class="grid3" style="margin-top:8px">
<div class="card" style="margin:0;background:#102A2E;color:#F3F5F1;border:0"><p class="lab" style="color:#D9B25F">Government</p><p>MoH, MoD and NCP define packages, buy the service, monitor KPIs and take the facilities back at handback.</p></div>
<div class="card" style="margin:0;background:#2E6E68;color:#fff;border:0"><p class="lab" style="color:#F3E7C9">Private partner (per package)</p><p><b>D</b>esign upgrades · <b>R</b>e-employ existing sites · <b>F</b>inance capex · <b>M</b>aintain assets · deliver <b>clinical services</b> for six years.</p></div>
<div class="card" style="margin:0;background:#F3E7C9;border:0"><p class="lab g">Supply chain</p><p>Dialysis machines, water treatment, consumables and drugs, health IT, staffing pipeline. Often the consortium’s second member.</p></div>
</div>
<div class="wsw"><div><b>WHAT IT SHOWS</b>The three blocks a winning bid must cover.</div><div><b>HOW TO READ IT</b>Any block a bidder cannot deliver in-house needs a partner or a subcontract.</div><div><b>WHY IT MATTERS</b>Five of the twelve qualified bidders are already consortia: operators are pairing with suppliers and local groups.</div></div></div>
<h3>What analysis can answer before the RFP</h3>
<div class="grid3">
<div class="card bar" style="border-left-color:#2E6E68"><p class="lab">Measured directly</p><p>Minimum patient numbers, package count, term, scope, qualified field.</p></div>
<div class="card bar" style="border-left-color:#C99A3B"><p class="lab g">Proxies &amp; assumptions</p><p>Sessions per patient, upgrade capex per site, cost of capital, staffing cost per station.</p></div>
<div class="card bar" style="border-left-color:#6B4E8E"><p class="lab" style="color:#6B4E8E">Judgement</p><p>Which packages suit you, how hard to price volume risk, who to partner with.</p></div>
</div>
<div class="card" style="margin-top:12px"><p class="lab r">The structural tension</p><p>A <b>DRFM</b> contract asks the private side to <b>finance</b> capex, but a <b>six-year</b> term is shorter than a typical project-finance loan for healthcare assets. Expect corporate or equipment finance, not non-recourse project debt, unless the RFP adds an extension or a capex payment <span class="tag A">ASSESSMENT</span>.</p></div>
<div class="foot"><span>Source: Saudi MoH notice of 4 May 2026 (scope and DRFM framework)</span><span class="pn">3</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>4 · Capex-recovery maths</b></div>
<h2><span class="n">4</span>Capex-recovery maths</h2><div class="rule"></div>
<p class="lead">The six-year term is the single most important number in this deal. It fixes how much every dialysis session must carry to repay upgrade and equipment spending.</p>
<div class="card" style="padding:0;overflow:hidden">
<div style="background:#2E6E68;color:#fff;padding:10px 14px;display:flex;justify-content:space-between;align-items:center"><div><p class="lab" style="color:#F3E7C9;margin:0">Method 4.1</p><p style="font-size:15px;font-weight:700">Capital recovery charge per session</p></div><span class="tag F" style="font-size:10px">FORMULA</span></div>
<div style="padding:12px 14px">
<p class="lab">Calculation</p>
<p style="font-size:14px;text-align:center;margin:6px 0 8px"><b>Charge per session</b> = Capex × r ÷ (1 − (1 + r)<sup>−n</sup>) ÷ Sessions per year</p>
<p style="font-size:10.5px;color:#3E4E52">where r is the cost of capital and n the term in years. The first part is the standard annuity that repays capex with a return; dividing by annual sessions gives the amount each treatment must carry.</p>
<div class="card bar" style="border-left-color:#C99A3B"><p class="lab g">Worked example · illustrative inputs</p><p>One package at the even split: 2,875 patients <span class="tag F">FORMULA</span> × 156 sessions a year (three a week, assumed all in-centre) <span class="tag I">ILLUSTRATIVE</span> = 448,500 sessions. Capex SAR 100m <span class="tag I">ILLUSTRATIVE</span> at 8%: annual charge SAR 21.6m → <b>SAR 48 per session over 6 years</b>, against <b>SAR 26 over 15 years</b>. The six-year term almost doubles the capex load per session (×1.85).</p></div>
</div></div>
<div class="fig"><span class="fign">FIGURE 3</span><span class="tag I">ILLUSTRATIVE</span> per SAR 100m of capex, 448,500 sessions a year
<p class="figt">Capex charge per session falls fast as the term lengthens</p>
{chart}
<div class="wsw"><div><b>WHAT IT SHOWS</b>SAR each session must carry to repay SAR 100m of capex, by term and cost of capital.</div><div><b>HOW TO READ IT</b>Scale linearly: SAR 50m of capex halves every figure; fewer sessions raise it.</div><div><b>WHY IT MATTERS</b>At six years the curve is still steep. One year more or less moves price materially; ask for an extension option.</div></div></div>
<table style="margin-top:10px"><tr><th>Term</th><th>Annual charge, SAR m (8%)</th><th>SAR per session (8%)</th><th>SAR per session (10%)</th></tr>{rows}</table>
<div class="foot"><span>Inputs labelled illustrative are assumptions, not RFP data. Home and peritoneal dialysis reduce in-centre sessions.</span><span class="pn">4</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>5–6 · Field &amp; risk</b></div>
<h2><span class="n">5</span>Competitive field</h2><div class="rule"></div>
<div class="grid2" style="grid-template-columns:1.35fr 1fr">
<table><tr><th>#</th><th>Qualified bidder (4 Oct 2026)</th><th>Form</th></tr>{bh}</table>
<div>
<div class="card" style="margin-top:0"><p class="lab">The arithmetic</p><p style="font-size:26px;font-weight:800;line-height:1.1">12 ÷ 4 = 3</p><p>qualified bidders per package, if all bid everything and packages are equal <span class="tag F">FORMULA</span>. Rules on bids per bidder are not yet public.</p></div>
<div class="card"><p class="lab">What the field says</p><p>Five consortia pair operators with suppliers or local groups. Several global renal specialists and large Saudi hospital groups qualified in their own right <span class="tag A">ASSESSMENT</span>.</p></div>
<div class="card"><p class="lab r">Implication</p><p>Competition will be on operating cost and clinical delivery, not on financing. A bidder without a cost edge per session should target the package where its existing footprint is strongest.</p></div>
</div></div>
<h2 style="margin-top:18px"><span class="n">6</span>Risk allocation: one risk, three views</h2><div class="rule"></div>
<table><tr><th style="width:22%">Risk</th><th>Government</th><th>Lender</th><th>Sponsor / operator</th></tr>{rh}</table>
<p style="font-size:10px;color:#6B777A;margin-top:6px"><span class="tag A">ASSESSMENT</span> Typical positions for a service PPP of this type; the RFP will set the actual allocation.</p>
<div class="foot"><span>Source: Saudi MoH notice of 4 Oct 2026 (qualified list)</span><span class="pn">5</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>7 · Bid decision</b></div>
<h2><span class="n">7</span>Bid decision</h2><div class="rule"></div>
<div class="fig" style="margin-top:0"><span class="fign">FIGURE 4</span><span class="tag A">ASSESSMENT</span>
<p class="figt">Should your firm bid? Four gates</p>
<div class="dt">
<div class="q"><div class="qb">1. Do you deliver dialysis clinically at scale, or have that operator in your consortium?</div><div class="ar">No →</div><div class="ob"><b>Partner or pass.</b> Join an operator as supplier, local partner or minority investor.</div></div>
<div class="q"><div class="qb">2. Can you staff and run clinics in Saudi Arabia for six years, meeting local-content targets?</div><div class="ar">No →</div><div class="ob"><b>Add a Saudi partner</b> before the RFP, or limit the bid to one package.</div></div>
<div class="q"><div class="qb">3. Does your price recover upgrade capex within six years at your cost of capital (Figure 3)?</div><div class="ar">No →</div><div class="ob"><b>Bid capex-light</b>: re-use sites as found, lease equipment, or make an extension a condition.</div></div>
<div class="q"><div class="qb">4. Can your balance sheet carry the investment without long-tenor project debt?</div><div class="ar">No →</div><div class="ob"><b>Line up equipment or corporate finance</b> with tenor of six years or less now.</div></div>
<div class="q"><div class="qb" style="background:#E3EEEC;border-color:#9CC9C1">All four answered yes</div><div class="ar" style="color:#2E6E68">→</div><div class="ob" style="border-color:#2E6E68"><b style="color:#2E6E68">Bid</b> for the one or two packages where your footprint and referral base are strongest.</div></div>
</div></div>
<h3 style="margin-top:10px">Verdict by bidder type</h3>
<table><tr><th style="width:30%">Bidder type</th><th style="width:20%">Verdict</th><th>Why</th></tr>
<tr><td>Integrated renal operator</td><td><span class="tag V">BID 1–2 PACKAGES</span></td><td>Owns the cost curve per session and the clinical model</td></tr>
<tr><td>Hospital group without renal scale</td><td><span class="tag F">PARTNER</span></td><td>Brings sites and referrals; needs a renal operator</td></tr>
<tr><td>Equipment or consumables maker</td><td><span class="tag F">CONSORTIUM MEMBER</span></td><td>Supply margin plus equipment-finance role</td></tr>
<tr><td>Financial investor</td><td><span class="tag A">MINORITY ONLY</span></td><td>Short term, operator-driven returns, little leverage</td></tr>
<tr><td>Bank or lessor</td><td><span class="tag R">LEND ≤ 6 YEARS</span></td><td>Equipment or corporate facilities matched to the term</td></tr>
</table>
<h3 style="margin-top:10px">Bankability scorecard</h3>
<table><tr><th style="width:26%">Criterion</th><th>Reason</th><th style="width:22%">Score</th></tr>{sh}
<tr><td style="background:#102A2E;color:#F3F5F1">Overall</td><td style="background:#102A2E;color:#F3F5F1">Strong counterparty, thin disclosure, short tenor</td><td style="background:#102A2E;color:#D9B25F;font-weight:800">{avg:.1f} / 5 · Conditional</td></tr></table>
<div class="foot"><span>Author’s assessment from public information; to be re-scored when the RFP is issued</span><span class="pn">6</span></div>
</section>

<section class="pg">
<div class="run"><span>Saudi National Dialysis PPP · Bid Decision Brief</span><b>8 · RFP questions &amp; sources</b></div>
<h2><span class="n">8</span>Twelve questions to put to the procurers</h2><div class="rule"></div>
<p class="lead">Each answer moves price or bankability. Bid teams should table them at the first clarification round.</p>
<div class="card" style="margin-top:0"><ol class="qs">{qh}</ol></div>
<h3>Signals to watch</h3>
<table><tr><th>Signal</th><th>What it would change</th></tr>
<tr><td>RFP issue date</td><td>Starts the pricing clock; reveals package boundaries and payment basis</td></tr>
<tr><td>Payment basis</td><td>Per-session pay moves volume risk to bidders; availability pay moves it to government</td></tr>
<tr><td>Extension option</td><td>Each extra year lowers the capex charge per session (Figure 3)</td></tr>
<tr><td>Bids-per-bidder rule</td><td>Decides whether large operators can sweep packages</td></tr></table>
<h3>Sources</h3>
<table><tr><th style="width:36%">Source</th><th>Used for</th></tr>
<tr><td>Saudi Ministry of Health, notice 4 May 2026 · moh.gov.sa/en/ministry/mediacenter/ads/pages/ads-2026-05-04-001.aspx</td><td>Procurers, DRFM framework, six-year term, four packages, 11,500 minimum, scope, 15 June deadline</td></tr>
<tr><td>Saudi Ministry of Health, news 4 Oct 2026 · moh.gov.sa/en/Ministry/MediaCenter/News/Pages/news-2026-10-04-001.aspx</td><td>Twelve qualified bidders and their names</td></tr>
<tr><td>Zawya · zawya.com (Saudi Arabia invites bidders for CKD care and national dialysis PPP)</td><td>Independent confirmation of packages, patients and term</td></tr></table>
<div class="card" style="margin-top:14px"><p class="lab">About this brief</p><p>Prepared by Ramesh Radhakrishnaraja, FCA, with AI assistance; every fact is checked against the cited sources as at 10 November 2026. Illustrative figures use assumed inputs and are labelled. This is an analytical view of a public procurement, not legal or investment advice, and not a recommendation to any specific bidder.</p><p style="margin-top:8px;font-family:Lora,serif;font-style:italic;color:#8A6420">Soli Deo Gloria</p></div>
<div class="foot"><span>PPP Architecture Series · Bid Decision Brief No. 01</span><span class="pn">7</span></div>
</section>
</body></html>'''
open('brief.html','w').write(html)
