CSS = """
<style>
:root{
  --bg:#070b14;--panel:rgba(14,22,36,.78);--line:rgba(164,183,219,.16);
  --text:#edf4ff;--muted:#9aa8c1;--gold:#d8b86c;--gold2:#b9954c;--cyan:#63d7ff;
}
html,body,[data-testid="stAppViewContainer"]{
  background:
    radial-gradient(circle at 18% -8%,rgba(75,108,255,.14),transparent 29%),
    radial-gradient(circle at 82% -6%,rgba(216,184,108,.11),transparent 26%),
    linear-gradient(180deg,#070b14 0%,#0a1020 46%,#070a12 100%);
  color:var(--text);
}
[data-testid="stHeader"]{background:rgba(8,13,24,0)}
[data-testid="stToolbar"]{display:none}
.block-container{padding-top:1.35rem;padding-bottom:4rem;max-width:1480px}

/* Premium hero: refined signal-room marquee. */
.hero-clean{
  position:relative;display:flex;align-items:center;justify-content:center;
  max-width:1080px;min-height:118px;margin:0 auto 20px auto;
  border-radius:30px;padding:26px 230px 26px 230px;
  background:
    radial-gradient(circle at 18% 0%,rgba(216,184,108,.20),transparent 34%),
    radial-gradient(circle at 82% 8%,rgba(99,215,255,.12),transparent 36%),
    linear-gradient(135deg,rgba(18,29,48,.92),rgba(8,13,24,.96) 52%,rgba(14,23,38,.90));
  box-shadow:
    0 34px 90px rgba(0,0,0,.42),
    inset 0 1px 0 rgba(255,255,255,.10),
    inset 0 -1px 0 rgba(216,184,108,.16);
  overflow:hidden;
}
.hero-clean:before{
  content:"";position:absolute;inset:0;border-radius:30px;padding:1px;
  background:linear-gradient(120deg,rgba(216,184,108,.72),rgba(99,215,255,.14) 42%,rgba(216,184,108,.44));
  -webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
  -webkit-mask-composite:xor;mask-composite:exclude;pointer-events:none;
}
.hero-clean:after{
  content:"";position:absolute;left:18%;right:18%;bottom:0;height:1px;
  background:linear-gradient(90deg,transparent,rgba(216,184,108,.72),rgba(99,215,255,.38),transparent);
  pointer-events:none;
}
.hero-inner{position:relative;z-index:2;text-align:center}
.hero-kicker{
  display:inline-flex;align-items:center;justify-content:center;margin-bottom:8px;
  color:#d8b86c;font-size:.70rem;font-weight:900;letter-spacing:.22em;text-transform:uppercase;
}
.hero-title{
  position:relative;z-index:2;font-size:2.56rem;line-height:1.02;font-weight:900;letter-spacing:-.055em;
  color:#fff;text-align:center;text-shadow:0 18px 38px rgba(0,0,0,.50);
  white-space:nowrap;
}
.hero-accent{
  width:124px;height:3px;border-radius:99px;margin:14px auto 0 auto;
  background:linear-gradient(90deg,transparent,rgba(216,184,108,.95),rgba(99,215,255,.56),transparent);
  box-shadow:0 0 22px rgba(216,184,108,.24);
}
.buildwell-emblem{
  position:absolute;right:28px;top:50%;transform:translateY(-50%);
  width:164px;max-width:18vw;height:auto;z-index:2;
  filter:drop-shadow(0 18px 30px rgba(0,0,0,.46));border:0!important;background:transparent!important;
}

.metric-card{border:1px solid var(--line);background:linear-gradient(180deg,rgba(20,31,51,.82),rgba(12,19,33,.72));border-radius:22px;padding:20px;min-height:112px;box-shadow:0 16px 44px rgba(0,0,0,.23)}
.metric-label{color:var(--muted);text-transform:uppercase;letter-spacing:.12em;font-size:.72rem;font-weight:800}.metric-value{color:#fff;font-size:2.2rem;font-weight:800;letter-spacing:-.04em;margin-top:8px}.metric-note{color:#aab6cc;font-size:.87rem;margin-top:7px;line-height:1.35}
.section-title{margin-top:34px;margin-bottom:16px;font-size:1.28rem;font-weight:850;letter-spacing:-.025em;color:#fff}.section-subtitle{display:none}
.lane-card{border:1px solid var(--line);background:rgba(14,22,36,.62);border-radius:18px;padding:16px;min-height:92px}.lane-title{color:#fff;font-weight:850;font-size:1rem}.lane-metrics{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.lane-metrics span{border:1px solid rgba(216,184,108,.18);background:rgba(216,184,108,.055);color:#f2deaa;border-radius:999px;padding:5px 9px;font-size:.76rem}
.signal{border-left:3px solid rgba(99,215,255,.85);background:rgba(99,215,255,.055);border-radius:14px;padding:12px 14px;margin-bottom:10px;color:#dceaff}.signal strong{color:#fff}.caption{display:none}


/* Premium flexible lane picker */
.scan-selector-shell{
  max-width:980px;margin:0 auto 26px auto;text-align:center;border:1px solid rgba(164,183,219,.15);
  border-radius:28px;padding:22px 26px 24px 26px;background:
    radial-gradient(circle at 18% 0%,rgba(99,215,255,.12),transparent 36%),
    radial-gradient(circle at 82% 8%,rgba(216,184,108,.12),transparent 34%),
    linear-gradient(135deg,rgba(15,25,44,.86),rgba(8,13,24,.74));
  box-shadow:0 24px 70px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.08);
}
.scan-selector-kicker{color:#d8b86c;font-size:.66rem;font-weight:900;letter-spacing:.25em;text-transform:uppercase;margin-bottom:7px}
.scan-selector-title{color:#fff;font-size:1.28rem;font-weight:900;letter-spacing:-.035em}
.scan-selector-note{max-width:760px;margin:10px auto 0 auto;color:#a7b4ca;font-size:.93rem;line-height:1.45}
.lane-card-zone{max-width:1180px;margin:0 auto 18px auto;padding:0 10px}.lane-card-zone [data-testid="column"]{padding:0 .35rem!important}
.lane-choice-card{position:relative;min-height:178px;border-radius:18px;padding:22px 24px 20px 24px;overflow:hidden;border:1px solid rgba(164,183,219,.16);background:linear-gradient(145deg,rgba(16,25,45,.86),rgba(7,12,23,.88));box-shadow:0 22px 58px rgba(0,0,0,.24), inset 0 1px 0 rgba(255,255,255,.06);transition:transform .18s ease,border-color .18s ease,box-shadow .18s ease}.lane-choice-card:before{content:"";position:absolute;inset:0;opacity:.45;pointer-events:none}.lane-choice-card.selected{transform:translateY(-1px);box-shadow:0 26px 64px rgba(0,0,0,.30), inset 0 1px 0 rgba(255,255,255,.09)}.lane-choice-card.unselected{opacity:.72}.lane-choice-card.unselected .lane-choice-check{background:rgba(12,19,33,.62)!important;color:#a7b4ca!important;border-color:rgba(164,183,219,.20)!important}.lane-choice-topline{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px}.lane-choice-icon{width:42px;height:42px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-weight:950;letter-spacing:-.04em;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);box-shadow:0 10px 24px rgba(0,0,0,.24)}.lane-choice-check{width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1rem;font-weight:950;color:#07101e;background:linear-gradient(135deg,#f0d989,#bd984a);border:1px solid rgba(255,230,165,.34);box-shadow:0 10px 26px rgba(0,0,0,.28), inset 0 1px 0 rgba(255,255,255,.34)}.lane-choice-title{color:#fff;font-size:1.15rem;font-weight:900;letter-spacing:-.03em;line-height:1.15;white-space:normal}.lane-choice-subtitle{color:#bdc8db;font-size:.91rem;line-height:1.35;margin-top:10px}.lane-choice-note{color:#9aa8c1;font-size:.88rem;line-height:1.35;margin-top:4px}.lane-violet{border-color:rgba(160,101,255,.55)}.lane-violet:before{background:radial-gradient(circle at 5% 0%,rgba(160,101,255,.44),transparent 45%)}.lane-violet .lane-choice-icon{color:#caa7ff;box-shadow:0 0 24px rgba(160,101,255,.18)}.lane-blue{border-color:rgba(60,140,255,.58)}.lane-blue:before{background:radial-gradient(circle at 10% 0%,rgba(60,140,255,.44),transparent 45%)}.lane-blue .lane-choice-icon{color:#8cc0ff;box-shadow:0 0 24px rgba(60,140,255,.18)}.lane-green{border-color:rgba(65,207,130,.55)}.lane-green:before{background:radial-gradient(circle at 10% 0%,rgba(65,207,130,.34),transparent 45%)}.lane-green .lane-choice-icon{color:#7cf0ad;box-shadow:0 0 24px rgba(65,207,130,.18)}.lane-gold{border-color:rgba(216,184,108,.62)}.lane-gold:before{background:radial-gradient(circle at 10% 0%,rgba(216,184,108,.32),transparent 45%)}.lane-gold .lane-choice-icon{color:#f0d989;box-shadow:0 0 24px rgba(216,184,108,.18)}
.st-key-lane_toggle_0 button,.st-key-lane_toggle_1 button,.st-key-lane_toggle_2 button,.st-key-lane_toggle_3 button{margin-top:-54px!important;height:54px!important;opacity:0!important;border-radius:18px!important}.st-key-lane_toggle_0,.st-key-lane_toggle_1,.st-key-lane_toggle_2,.st-key-lane_toggle_3{margin-bottom:0!important}.selection-row-wrap{max-width:1180px;margin:4px auto 0 auto}.lane-selection-summary{min-height:56px;border-radius:18px;border:1px solid rgba(164,183,219,.16);background:linear-gradient(135deg,rgba(15,25,44,.78),rgba(8,13,24,.72));display:flex;align-items:center;gap:14px;padding:12px 18px;color:#aebbd0;box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}.lane-selection-summary strong{color:#fff;font-size:1rem;white-space:nowrap}.summary-dot{width:26px;height:26px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#8665ff,#4e39bc);color:white;font-weight:950;box-shadow:0 10px 24px rgba(0,0,0,.25)}.st-key-lane_clear_all button{min-height:56px!important;border-radius:16px!important;border:1px solid rgba(255,89,89,.40)!important;background:rgba(255,72,72,.06)!important;color:#ff9a9a!important;font-weight:850!important}.st-key-lane_clear_all button:hover{background:rgba(255,72,72,.10)!important;border-color:rgba(255,120,120,.55)!important;color:#ffc0c0!important}.scan-selector-caption{width:fit-content;max-width:880px;margin:18px auto 22px auto;padding:10px 16px;border-radius:999px;border:1px solid rgba(99,215,255,.18);background:rgba(99,215,255,.06);color:#d7edff;font-size:.84rem;text-align:center;box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}

/* Centered premium action */
.run-button-zone{display:flex;justify-content:center;align-items:center;width:100%;margin:2px auto 34px auto;text-align:center}
.st-key-run_analysis{display:flex!important;justify-content:center!important;align-items:center!important;width:100%!important;margin:0 auto 34px auto!important;text-align:center!important}
.st-key-run_analysis div[data-testid="stButton"]{display:flex!important;justify-content:center!important;width:100%!important;margin:0 auto!important}
.st-key-run_analysis button, div[data-testid="stButton"] button[kind="secondary"]{
  width:190px!important;max-width:190px!important;border-radius:999px!important;min-height:50px!important;
  border:1px solid rgba(216,184,108,.62)!important;
  background:linear-gradient(135deg,rgba(238,211,142,.98),rgba(184,146,67,.98))!important;
  color:#07101e!important;font-weight:900!important;letter-spacing:.01em;
  box-shadow:0 18px 42px rgba(0,0,0,.36), inset 0 1px 0 rgba(255,255,255,.34)!important;
}
.st-key-run_analysis button:hover{border-color:rgba(255,230,165,.92)!important;transform:translateY(-1px);box-shadow:0 22px 52px rgba(0,0,0,.44), inset 0 1px 0 rgba(255,255,255,.40)!important}
.stPlotlyChart{border-radius:22px;overflow:hidden;border:1px solid rgba(164,183,219,.10);background:rgba(7,12,22,.18)}

/* Dark select/dropdown cleanup */
div[data-baseweb="select"]>div, div[data-baseweb="select"] div, div[data-baseweb="input"]>div, input, textarea{
  background-color:rgba(12,19,33,.96)!important;border-color:rgba(164,183,219,.22)!important;color:#edf4ff!important;
}
div[data-baseweb="select"]>div{border-radius:14px!important;box-shadow:none!important}
div[data-baseweb="select"] span, div[data-baseweb="select"] svg, div[data-baseweb="input"] input{color:#edf4ff!important;fill:#edf4ff!important}
div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"], div[role="listbox"]{
  background:#0d1526!important;color:#edf4ff!important;border:1px solid rgba(164,183,219,.22)!important;
}
li[role="option"], div[role="option"]{background:#0d1526!important;color:#edf4ff!important}
li[role="option"]:hover, div[role="option"]:hover{background:rgba(99,215,255,.10)!important}
[data-testid="stSelectbox"], [data-testid="stMultiSelect"]{color:#edf4ff!important}

/* Expander cleanup: remove white header bars across Streamlit versions. */
div[data-testid="stExpander"]{border:1px solid rgba(164,183,219,.16)!important;border-radius:16px!important;background:rgba(10,16,28,.42)!important;overflow:hidden!important;box-shadow:none!important}
div[data-testid="stExpander"] details{background:rgba(10,16,28,.42)!important;color:#edf4ff!important}
div[data-testid="stExpander"] details > summary,
div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary:hover,
div[data-testid="stExpander"] [data-testid="stExpanderToggleIcon"]{
  background:linear-gradient(90deg,rgba(17,27,46,.98),rgba(12,19,33,.96))!important;color:#edf4ff!important;border-bottom:1px solid rgba(164,183,219,.12)!important;
}
div[data-testid="stExpander"] summary *, div[data-testid="stExpander"] svg{color:#edf4ff!important;fill:#edf4ff!important}
div[data-testid="stExpander"] [data-testid="stMarkdownContainer"] p{color:#edf4ff!important}

/* Native dataframe fallback styling */
div[data-testid="stDataFrame"], div[data-testid="stDataFrame"] div{background:rgba(10,16,28,.78)!important;color:#edf4ff!important;border-color:rgba(164,183,219,.16)!important}
div[data-testid="stDataFrame"] *{color:#edf4ff!important}
.dark-table-wrap{overflow:auto;border:1px solid var(--line);border-radius:18px;background:rgba(10,16,28,.78);box-shadow:0 16px 42px rgba(0,0,0,.18);margin-bottom:14px}.dark-data-table{border-collapse:separate;border-spacing:0;width:100%;font-size:.82rem;color:#edf4ff}.dark-data-table thead th{position:sticky;top:0;background:#111b2e;color:#fff;text-align:left;padding:10px 12px;border-bottom:1px solid rgba(164,183,219,.22);white-space:nowrap;z-index:2}.dark-data-table tbody td{padding:9px 12px;border-bottom:1px solid rgba(164,183,219,.10);color:#dce7f7;vertical-align:top;max-width:360px}.dark-data-table tbody tr:nth-child(even){background:rgba(255,255,255,.025)}.dark-data-table tbody tr:hover{background:rgba(99,215,255,.06)}

@media(max-width:900px){
  .hero-clean{min-height:126px;padding:20px 22px;justify-content:center;flex-direction:column;gap:12px}
  .hero-title{font-size:2.08rem;white-space:normal}.buildwell-emblem{position:relative;right:auto;top:auto;transform:none;width:146px;max-width:56vw}.hero-kicker{font-size:.64rem}
}
</style>
"""
