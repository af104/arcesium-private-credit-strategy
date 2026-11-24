from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment

F="Arial"
def f(**k): return Font(name=F, **k)
BLUE=f(color="0000FF"); BLACK=f(); GREEN=f(color="008000"); BOLD=f(bold=True)
HDR=f(bold=True,color="FFFFFF"); TITLE=f(bold=True,size=16)
HFILL=PatternFill("solid",fgColor="1F3864"); YEL=PatternFill("solid",fgColor="FFFF00")
SEC=PatternFill("solid",fgColor="D9E1F2"); thin=Side(style="thin",color="BFBFBF")
BOX=Border(top=thin,bottom=thin,left=thin,right=thin)
USD="$#,##0;($#,##0);-"; USDM='$#,##0.0"M";($#,##0.0"M");-'; PCT="0.0%;(0.0%);-"; NUM="#,##0;(#,##0);-"; NUM1="#,##0.0;(#,##0.0);-"

wb=Workbook()
# ---------------- README
r=wb.active; r.title="README"
r["A1"]="Arcesium in Private Credit: ABF Revenue Scenario Model"; r["A1"].font=TITLE
lines=[
("Prepared by","Andres Farrulla, Stony Brook University, November 2026"),
("Purpose","Sizes the new annual recurring revenue (ARR) Arcesium could win by targeting private credit managers, by AUM tier, over five years."),
("How it works","New ARR = number of managers in tier x Arcesium 5-year win rate x annual contract value (ACV), summed across tiers. Year-by-year build applies a client ramp and net revenue retention."),
("Scenario switch","Change Assumptions!C4 to Low, Base or High. The Model tab follows it. The Scenarios tab always shows all three side by side."),
("",""),
("Legend",""),
("Blue text","Hardcoded input you can change"),
("Black text","Formula"),
("Green text","Link to another tab"),
("Yellow fill","Key assumption or the scenario switch"),
("",""),
("Important","Rows marked Estimated are my assumptions, not facts. No free public source reports private credit manager counts by AUM tier, Arcesium win rates or Arcesium contract values. Contract values are benchmarked to Clearwater and Allvue public figures. Every sourced number has its link in the Source column."),
("Tabs","Assumptions (all inputs and sources) | Model (selected scenario, 5-year build) | Scenarios (Low, Base, High side by side, sanity checks) | Sensitivity (win rate vs contract value)"),
]
for i,(a,b) in enumerate(lines,start=3):
    r.cell(i,1,a).font=BOLD; c=r.cell(i,2,b); c.font=BLACK; c.alignment=Alignment(wrap_text=True,vertical="top")
r["B9"].font=BLUE; r["B11"].font=GREEN; r["B12"].fill=YEL
r.column_dimensions["A"].width=18; r.column_dimensions["B"].width=110

# ---------------- Assumptions
a=wb.create_sheet("Assumptions")
a["A1"]="Assumptions and sources"; a["A1"].font=TITLE
a["A2"]="Units: AUM in $ trillions, ACV in $, rates as %. Blue = input. Estimated rows are assumptions."; a["A2"].font=f(italic=True)
a["B4"]="Scenario selected:"; a["B4"].font=BOLD
a["C4"]="Base"; a["C4"].font=BLUE; a["C4"].fill=YEL; a["C4"].border=BOX
dv=DataValidation(type="list",formula1='"Low,Base,High"',allow_blank=False); a.add_data_validation(dv); dv.add("C4")
a["D4"]='=MATCH(C4,{"Low","Base","High"},0)'; a["D4"].font=BLACK
a["E4"]="<- scenario index (1=Low, 2=Base, 3=High)"; a["E4"].font=f(italic=True,color="808080")
hdr=["#","Assumption","Low","Base","High","Selected","Type","Source or basis"]
for j,h in enumerate(hdr,1):
    c=a.cell(6,j,h); c.font=HDR; c.fill=HFILL; c.border=BOX; c.alignment=Alignment(wrap_text=True,vertical="center")
rows=[
("SEC","Market"),
(1,"Global private credit AUM, 2024 ($T)",3.5,3.5,3.5,"Sourced",NUM1,"ACC/AIMA via Investment Executive, Dec 2025: https://www.investmentexecutive.com/news/research-and-markets/global-private-credit-market-reaches-us3-5-trillion-aum-threshold-report/"),
(2,"Global private credit AUM, 2025 ($T)",4.1,4.1,4.1,"Sourced",NUM1,"AIMA/ACC press release: https://www.aima.org/article/press-release-global-private-credit-market-hit-us-4-1tn-aum-in-2025-acc-data-reveals.html"),
(3,"AUM growth per year, 2026-2030",0.019,0.08,0.17,"Low and high derived from sources, base estimated",PCT,"Low: growth implied by the $4.5T 2030 forecasts from BlackRock https://alternativecreditinvestor.com/2025/04/07/blackrock-predicts-private-credit-aum-will-reach-4-5tn-by-2030/ and Preqin https://www.businesswire.com/news/home/20251016075672/en/Preqin-Releases-Private-Markets-in-2030-Report (these use a narrower market definition) ; High: 17% growth in 2024 (ACC, link in row 1) ; Base: estimate between them"),
(4,"ABF share of deployment",0.16,0.16,0.16,"Sourced",PCT,"ACC 2024 data via Investment Executive (link in row 1)"),
("SEC","Target managers by AUM tier (count)"),
(5,"Managers with $50B+ in credit",15,20,25,"Estimated",NUM,"Anchors: 8 listed managers hold $2.33T credit AUM (Preqin) https://www.preqin.com/news/credit-aum-at-listed-alternatives-managers-rises-21-5-to-usd2-33tn-in-2024 ; top 20 managers hold 36% of dry powder (S&P Global, Jan 2025)"),
(6,"Managers with $10-50B",40,50,60,"Estimated","#,##0","Power-law fit to 250 ACC member managers with $2T+ AUM (ACC, link in row 1)"),
(7,"Managers with $1-10B",200,250,300,"Estimated",NUM,"Same fit; cross-check: 136 evergreen private credit managers (With Intelligence) https://www.withintelligence.com/insights/private-credit-funds-surpasses-500bn/"),
("SEC","Annual contract value (ACV, $)"),
(8,"ACV, $50B+ tier",2000000,3500000,5000000,"Estimated",USD,"Anchor: Clearwater has 152 clients above $1M ARR (FY2025) https://www.businesswire.com/news/home/20260218581398/en/"),
(9,"ACV, $10-50B tier",750000,1500000,2500000,"Estimated",USD,"Same anchor"),
(10,"ACV, $1-10B tier",250000,500000,750000,"Estimated",USD,"Clearwater ~$336K avg ($841M ARR / 2,500+ clients, link in row 8); Allvue ~$400K avg ($200M+ ARR / 500+ clients) https://whbl.com/2026/08/21/buyout-firm-vista-explores-3-billion-sale-of-private-markets-data-provider-allvue-sources-say/"),
("SEC","Arcesium 5-year win rate (share of tier won by year 5)"),
(11,"Win rate, $50B+ tier",0.05,0.10,0.15,"Estimated",PCT,"Largest managers often build in-house or run multi-vendor stacks"),
(12,"Win rate, $10-50B tier",0.05,0.10,0.20,"Estimated",PCT,"Assumed sweet spot for a pure-technology platform"),
(13,"Win rate, $1-10B tier",0.02,0.04,0.08,"Estimated",PCT,"Bundled software-plus-admin rivals are strongest here"),
("SEC","Retention and ramp"),
(14,"Net revenue retention (existing clients, per year)",1.03,1.09,1.15,"Base sourced; low and high estimated",PCT,"Clearwater FY2025 NRR 109% (link in row 8)"),
(15,"Share of 5-year wins landed in Year 1",0.10,0.10,0.10,"Estimated",PCT,"Ramp assumption: enterprise sales cycles are long"),
(16,"Share of 5-year wins landed in Year 2",0.15,0.15,0.15,"Estimated",PCT,"Ramp assumption"),
(17,"Share of 5-year wins landed in Year 3",0.20,0.20,0.20,"Estimated",PCT,"Ramp assumption"),
(18,"Share of 5-year wins landed in Year 4",0.25,0.25,0.25,"Estimated",PCT,"Ramp assumption"),
(19,"Share of 5-year wins landed in Year 5",0.30,0.30,0.30,"Estimated",PCT,"Ramp assumption; Years 1-5 must sum to 100% (check in Model tab)"),
("SEC","Sanity check inputs"),
(20,"Private credit ops spend, bps of AUM (tech plus outsourced ops)",0.0003,0.00045,0.0006,"Estimated",'0.00%',"3-6 bps. Cross-checks: direct lending fund admin expenses average 48 bps of NAV (Cliffwater, Apr 2024) https://www.cliffwaterfunds.com/data/pdfs/Private-Fund-Fees-and-Expenses-Direct-Lending.pdf ; fund admin priced in bps, private credit at higher-cost end (Fundtec) https://fundtec.co/insights/articles/fund-administration-cost"),
(21,"Pure software share of ops spend",0.33,0.40,0.50,"Estimated",PCT,"One third to one half"),
]
ref={}  # assumption number -> row
row=7
for item in rows:
    if item[0]=="SEC":
        a.cell(row,1,item[1]).font=BOLD
        for j in range(1,9): a.cell(row,j).fill=SEC
        row+=1; continue
    n,label,lo,ba,hi,typ,fmt,src=item
    ref[n]=row
    a.cell(row,1,n).font=BLACK; a.cell(row,2,label).font=BLACK
    for j,v in zip((3,4,5),(lo,ba,hi)):
        c=a.cell(row,j,v); c.font=BLUE; c.number_format=fmt; c.border=BOX
    s=a.cell(row,6,f"=INDEX(C{row}:E{row},1,$D$4)"); s.font=BLACK; s.number_format=fmt; s.border=BOX
    if typ=="Estimated": s.fill=YEL
    a.cell(row,7,typ).font=BLACK
    c=a.cell(row,8,src); c.font=BLACK; c.alignment=Alignment(wrap_text=True,vertical="top")
    a.cell(row,2).alignment=Alignment(wrap_text=True,vertical="top")
    row+=1
for col,w in zip("ABCDEFGH",(5,44,13,13,13,13,22,90)): a.column_dimensions[col].width=w
a.freeze_panes="C7"

def A(n,col="F"): return f"Assumptions!${col}${ref[n]}"

# ---------------- Model
m=wb.create_sheet("Model")
m["A1"]="Model: selected scenario"; m["A1"].font=TITLE
m["A2"]="Scenario:"; m["A2"].font=BOLD
m["B2"]="=Assumptions!C4"; m["B2"].font=GREEN; m["B2"].fill=YEL
m["C2"]="(change it on the Assumptions tab, cell C4)"; m["C2"].font=f(italic=True,color="808080")
h=["Tier","Managers in tier","5-yr win rate","Clients won by Year 5","ACV ($)","New ARR at contract value ($)"]
for j,t in enumerate(h,1):
    c=m.cell(4,j,t); c.font=HDR; c.fill=HFILL; c.alignment=Alignment(wrap_text=True); c.border=BOX
tiers=[("$50B+",5,11,8),("$10-50B",6,12,9),("$1-10B",7,13,10)]
for i,(name,mg,wr,acv) in enumerate(tiers,start=5):
    m.cell(i,1,name).font=BLACK
    for j,(n,fmt) in zip((2,3,5),((mg,NUM),(wr,PCT),(acv,USD))):
        c=m.cell(i,j,"="+A(n)); c.font=GREEN; c.number_format=fmt
    c=m.cell(i,4,f"=B{i}*C{i}"); c.number_format=NUM1
    c=m.cell(i,6,f"=D{i}*E{i}"); c.number_format=USD
    for j in range(1,7): m.cell(i,j).border=BOX
m["A8"]="Total"; m["A8"].font=BOLD
m["B8"]="=SUM(B5:B7)"; m["B8"].number_format=NUM
m["D8"]="=SUM(D5:D7)"; m["D8"].number_format=NUM1
m["E8"]='=IFERROR(F8/D8,0)'; m["E8"].number_format=USD
m["F8"]="=SUM(F5:F7)"; m["F8"].number_format=USD; m["F8"].font=BOLD
for j in range(1,7): m.cell(8,j).border=BOX; m.cell(8,j).font=BOLD
m["G8"]="<- headline figure in the memo (no retention uplift)"; m["G8"].font=f(italic=True,color="808080")
m["A9"]="Blended ACV shown in E8 = total new ARR / clients won."; m["A9"].font=f(italic=True,color="808080")

m["A11"]="Five-year build (with ramp and net revenue retention)"; m["A11"].font=BOLD
yrs=["Year 1","Year 2","Year 3","Year 4","Year 5"]
m["A12"]="($)"; m["A12"].font=HDR; m["A12"].fill=HFILL
for j,y in enumerate(yrs,2):
    c=m.cell(12,j,y); c.font=HDR; c.fill=HFILL; c.alignment=Alignment(horizontal="center")
labels=["Share of 5-year wins landed","New clients landed","New ARR landed this year","ARR from prior clients after retention","Total private credit ARR, end of year"]
for k,l in enumerate(labels,13): m.cell(k,1,l).font=BLACK
for j,n in enumerate((15,16,17,18,19),2):
    col=m.cell(12,j).column_letter
    c=m.cell(13,j,"="+A(n)); c.font=GREEN; c.number_format=PCT
    c=m.cell(14,j,f"=$D$8*{col}13"); c.number_format=NUM1
    c=m.cell(15,j,f"=$F$8*{col}13"); c.number_format=USD
    prev="0" if j==2 else f"{m.cell(17,j-1).column_letter}17*{A(14)}"
    c=m.cell(16,j,f"={prev}"); c.number_format=USD
    c=m.cell(17,j,f"={col}15+{col}16"); c.number_format=USD; c.font=BOLD
    for k in range(12,18): m.cell(k,j).border=BOX
m["A18"]="Ramp check (must equal 100%)"; m["A18"].font=BLACK
m["B18"]="=SUM(B13:F13)"; m["B18"].number_format=PCT
m["C18"]='=IF(ROUND(B18,4)=1,"OK","Ramp does not sum to 100%")'; m["C18"].font=BOLD
m["A20"]="Year 5 ARR with retention uplift ($)"; m["A20"].font=BOLD
m["B20"]="=F17"; m["B20"].number_format=USD; m["B20"].font=BOLD
m["A21"]="Uplift from retention vs headline"; m["A21"].font=BLACK
m["B21"]="=IFERROR(B20/F8-1,0)"; m["B21"].number_format=PCT
m.column_dimensions["A"].width=42
for col in "BCDEF": m.column_dimensions[col].width=20
m.column_dimensions["G"].width=50

# ---------------- Scenarios
s=wb.create_sheet("Scenarios")
s["A1"]="Scenarios side by side"; s["A1"].font=TITLE
s["A2"]="Calculated straight from the Low, Base and High columns on the Assumptions tab, independent of the scenario switch."; s["A2"].font=f(italic=True)
for j,t in enumerate(["Metric","Low","Base","High"],1):
    c=s.cell(4,j,t); c.font=HDR; c.fill=HFILL; c.border=BOX
cols={"Low":"C","Base":"D","High":"E"}
def AS(n,sc): return f"Assumptions!${cols[sc]}${ref[n]}"
metrics=[
("Clients won by Year 5", lambda sc: f"={AS(5,sc)}*{AS(11,sc)}+{AS(6,sc)}*{AS(12,sc)}+{AS(7,sc)}*{AS(13,sc)}", NUM1),
("New ARR at contract value ($)", lambda sc: f"={AS(5,sc)}*{AS(11,sc)}*{AS(8,sc)}+{AS(6,sc)}*{AS(12,sc)}*{AS(9,sc)}+{AS(7,sc)}*{AS(13,sc)}*{AS(10,sc)}", USD),
("Private credit AUM, 2030 ($T)", lambda sc: f"={AS(2,sc)}*(1+{AS(3,sc)})^5", NUM1),
("Ops spend, 2030 ($)", lambda sc: None, USD),
("Pure software spend, 2030 ($)", lambda sc: None, USD),
("New ARR as share of software spend", lambda sc: None, PCT),
]
for i,(lab,fn,fmt) in enumerate(metrics,5):
    s.cell(i,1,lab).font=BLACK
    for j,sc in enumerate(("Low","Base","High"),2):
        L=s.cell(4,j).column_letter
        if i==8: v=f"={L}7*1000000000000*{AS(20,sc)}"
        elif i==9: v=f"={L}8*{AS(21,sc)}"
        elif i==10: v=f"=IFERROR({L}6/{L}9,0)"
        else: v=fn(sc)
        c=s.cell(i,j,v); c.number_format=fmt; c.border=BOX
    s.cell(i,1).border=BOX
for j in range(1,5): s.cell(6,j).font=BOLD
s["A12"]="Reading the sanity check: even the high case is a small share of total software spend, so the upside is limited by Arcesium's win rate, not by market size."; s["A12"].font=f(italic=True)
s["A12"].alignment=Alignment(wrap_text=True); s.merge_cells("A12:D13"); s.row_dimensions[12].height=30
s.column_dimensions["A"].width=40
for col in "BCD": s.column_dimensions[col].width=20

# ---------------- Sensitivity
t=wb.create_sheet("Sensitivity")
t["A1"]="Sensitivity: base-case new ARR ($M) by win rate and contract value"; t["A1"].font=TITLE
t["A2"]="Each cell scales every base-case win rate and ACV by the multipliers shown. Win rate multipliers down the side, ACV multipliers across the top."; t["A2"].font=f(italic=True)
t["A3"]="Base-case new ARR ($):"; t["A3"].font=BOLD
t["C3"]="=Scenarios!C6"; t["C3"].font=GREEN; t["C3"].number_format=USD
mults=[0.5,0.75,1.0,1.25,1.5]
t["B5"]="Win rate x  /  ACV x"; t["B5"].font=HDR; t["B5"].fill=HFILL
for j,v in enumerate(mults,3):
    c=t.cell(5,j,v); c.font=f(color="0000FF",bold=True); c.number_format='0.00"x"'; c.fill=SEC; c.border=BOX
for i,v in enumerate(mults,6):
    c=t.cell(i,2,v); c.font=f(color="0000FF",bold=True); c.number_format='0.00"x"'; c.fill=SEC; c.border=BOX
    for j in range(3,8):
        L=t.cell(5,j).column_letter
        c=t.cell(i,j,f"=$C$3*$B{i}*{L}$5/1000000"); c.number_format=USDM; c.border=BOX
        if i==8 and j==5: c.font=BOLD; c.fill=YEL
t["B12"]="Win rates are capped in practice; a 1.5x multiplier on the high tiers is aggressive."; t["B12"].font=f(italic=True,color="808080")
t.column_dimensions["A"].width=3; t.column_dimensions["B"].width=22
for col in "CDEFG": t.column_dimensions[col].width=14

for ws in wb.worksheets:
    for rr in ws.iter_rows():
        for c in rr:
            if c.font and c.font.name!=F:
                c.font=Font(name=F,bold=c.font.bold,italic=c.font.italic,color=c.font.color,size=c.font.size)
wb.save("Arcesium_Private_Credit_ABF_Model.xlsx")
print(ref)
