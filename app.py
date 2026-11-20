import base64
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

LINKEDIN = "https://linkedin.com/in/ahmedaliy0"
GITHUB = "https://github.com/ahmedaliy01"
EMAIL = "ahmed.a.ali.tech@gmail.com"
PHONE = "+20 109 283 2379"

BRONZE, SILVER, GOLD = "#cd7f32", "#c0c8d4", "#f5b942"

st.set_page_config(
    page_title="Ahmed Ali | Data Engineer",
    page_icon="🥇",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ----------------------------------------------------------------- helpers
def html(s: str) -> None:
    """Render raw HTML (blank lines / indentation would break markdown)."""
    s = "\n".join(line.strip() for line in s.splitlines() if line.strip())
    st.markdown(s, unsafe_allow_html=True)


@st.cache_data(show_spinner=False)
def b64(name: str) -> str:
    return base64.b64encode((ASSETS / name).read_bytes()).decode()


def chips(items, cls="chip"):
    return "".join(f'<span class="{cls}">{i}</span>' for i in items)


# --------------------------------------------------------------------- CSS
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');
:root{
  --bg:#0a0e13; --surface:#111821; --surface2:#16202c; --line:#1f2a37;
  --text:#e6edf3; --muted:#8b98a9; --gold:#f5b942; --silver:#c0c8d4; --bronze:#cd7f32;
}
html, body, [class*="css"], .stApp {font-family:'Inter',system-ui,sans-serif;}
.stApp{background:
  radial-gradient(900px 500px at 85% -5%, rgba(245,185,66,.09), transparent 60%),
  radial-gradient(700px 500px at -5% 20%, rgba(192,200,212,.05), transparent 60%),
  var(--bg);}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"]{display:none !important;}
.block-container{max-width:1180px; padding:5.2rem 1.4rem 3rem !important;}
h1,h2,h3{letter-spacing:-.02em;}
a{color:var(--gold);}
.card a, .lead a, .foot a{color:var(--gold) !important; text-decoration:none !important; border-bottom:1px dashed rgba(245,185,66,.5);}
.card a:hover{border-bottom-style:solid;}
.logo{color:var(--text) !important;}
.logo b{color:var(--gold) !important;}
.card a.btn{border-bottom:1px solid var(--line);}
.card a.btn.pri{border-bottom:1px solid var(--gold); color:#0a0e13 !important;}

/* nav */
.nav{position:fixed; top:0; left:0; right:0; z-index:999; display:flex; justify-content:center;
  background:rgba(10,14,19,.78); backdrop-filter:blur(14px); border-bottom:1px solid var(--line);}
.nav-in{width:100%; max-width:1180px; padding:.8rem 1.4rem; display:flex; align-items:center; justify-content:space-between;}
.logo{font-family:'JetBrains Mono',monospace; font-weight:600; color:var(--text); font-size:1rem; text-decoration:none !important;}
.logo b{color:var(--gold); font-weight:600;}
.nav-links a{color:var(--muted) !important; text-decoration:none !important; font-size:.86rem; margin-left:1.4rem; transition:color .2s;}
.nav-links a:hover{color:var(--gold) !important;}
@media(max-width:760px){.nav-links{display:none;}}

/* section labels */
.eyebrow{font-family:'JetBrains Mono',monospace; font-size:.78rem; letter-spacing:.14em; color:var(--gold); text-transform:uppercase;}
.sec{margin-top:4.2rem; scroll-margin-top:90px;}
.sec h2{font-size:2.1rem; font-weight:800; margin:.35rem 0 .4rem; color:var(--text);}
.sec p.lead{color:var(--muted); max-width:720px; font-size:1.02rem; line-height:1.65; margin:0 0 1.4rem;}

/* hero */
.hero h1{font-size:clamp(2.3rem,5.2vw,3.9rem); line-height:1.06; font-weight:800; margin:.6rem 0 1rem;}
.hero h1 em{font-style:normal; background:linear-gradient(90deg,var(--bronze),var(--silver) 45%,var(--gold)); -webkit-background-clip:text; background-clip:text; color:transparent;}
.hero p{color:var(--muted); font-size:1.08rem; line-height:1.7; max-width:560px;}
.status{display:inline-flex; align-items:center; gap:.5rem; font-family:'JetBrains Mono',monospace; font-size:.76rem; color:var(--muted);
  border:1px solid var(--line); background:var(--surface); padding:.35rem .75rem; border-radius:999px;}
.dot{width:8px; height:8px; border-radius:50%; background:#3ddc97; box-shadow:0 0 0 4px rgba(61,220,151,.15);}
.photo-wrap{position:relative; display:flex; justify-content:center; padding:1rem 0;}
.photo-ring{width:300px; height:300px; border-radius:50%; padding:5px; background:conic-gradient(from 200deg,var(--bronze),var(--silver),var(--gold),var(--bronze));}
.photo-ring img{width:100%; height:100%; border-radius:50%; object-fit:cover; display:block; border:5px solid var(--bg);}
.float{position:absolute; background:rgba(17,24,33,.92); border:1px solid var(--line); border-radius:12px; padding:.5rem .8rem;
  font-family:'JetBrains Mono',monospace; font-size:.74rem; color:var(--text); box-shadow:0 10px 30px rgba(0,0,0,.4);}
.float.a{left:2%; bottom:8%;} .float.b{right:0; top:10%;}
.float i{display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:.45rem;}
@media(max-width:760px){.photo-ring{width:230px;height:230px;}}
.stats{display:grid; grid-template-columns:repeat(4,1fr); gap:.8rem; margin-top:2.2rem;}
.stat{background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:1rem 1.1rem;}
.stat b{display:block; font-size:1.6rem; font-weight:800; color:var(--gold);}
.stat span{color:var(--muted); font-size:.82rem;}
@media(max-width:760px){.stats{grid-template-columns:repeat(2,1fr);}}

/* cards / grids */
.grid{display:grid; gap:1rem;}
.g3{grid-template-columns:repeat(3,1fr);} .g2{grid-template-columns:repeat(2,1fr);}
@media(max-width:900px){.g3,.g2{grid-template-columns:1fr;}}
.card{background:linear-gradient(180deg,var(--surface),#0e151d); border:1px solid var(--line); border-radius:16px; padding:1.3rem 1.3rem 1.2rem;
  transition:transform .25s, border-color .25s;}
.card:hover{transform:translateY(-4px); border-color:rgba(245,185,66,.45);}
.card h3{font-size:1.08rem; font-weight:700; margin:.2rem 0 .45rem; color:var(--text);}
.card p{color:var(--muted); font-size:.93rem; line-height:1.6; margin:0;}
.ico{width:40px; height:40px; border-radius:11px; display:flex; align-items:center; justify-content:center; font-size:1.2rem;
  background:rgba(245,185,66,.1); border:1px solid rgba(245,185,66,.25);}

/* chips */
.chip{display:inline-block; font-family:'JetBrains Mono',monospace; font-size:.76rem; color:var(--text); background:var(--surface2);
  border:1px solid var(--line); padding:.28rem .62rem; border-radius:8px; margin:.18rem .22rem .18rem 0; transition:all .2s;}
.chip:hover{border-color:var(--gold); color:var(--gold);}
.chip.g{border-color:rgba(245,185,66,.35); color:var(--gold);}
.skillbox h4{font-size:.8rem; font-family:'JetBrains Mono',monospace; letter-spacing:.1em; color:var(--muted); text-transform:uppercase; margin:0 0 .6rem;}

/* projects */
.pcard{padding:0; overflow:hidden;}
.pvis{height:190px; border-bottom:1px solid var(--line); display:flex; align-items:center; justify-content:center; background:#0c121a; overflow:hidden;}
.pvis img{width:100%; height:100%; object-fit:cover; object-position:top;}
.pbody{padding:1.15rem 1.3rem 1.3rem;}
.layers{width:78%; display:flex; flex-direction:column; gap:7px; font-family:'JetBrains Mono',monospace; font-size:.72rem;}
.layers div{padding:.5rem .8rem; border-radius:8px; display:flex; justify-content:space-between; color:#0a0e13; font-weight:600;}
.flow{display:flex; align-items:center; gap:.5rem; font-family:'JetBrains Mono',monospace; font-size:.72rem; flex-wrap:wrap; justify-content:center; padding:0 1rem;}
.flow span.n{padding:.5rem .7rem; border-radius:8px; background:var(--surface2); border:1px solid var(--line); color:var(--text);}
.flow span.ar{color:var(--gold);}
.btnrow{margin-top:1rem; display:flex; gap:.6rem; flex-wrap:wrap;}
.btn{display:inline-block; padding:.45rem .95rem; border-radius:9px; font-size:.84rem; font-weight:600; text-decoration:none !important;
  border:1px solid var(--line); color:var(--text) !important; background:var(--surface2); transition:all .2s;}
.btn:hover{border-color:var(--gold); color:var(--gold) !important;}
.btn.pri{background:var(--gold); color:#0a0e13 !important; border-color:var(--gold);}
.btn.pri:hover{filter:brightness(1.08); color:#0a0e13 !important;}

/* timeline */
.tl{border-left:2px solid var(--line); padding-left:1.3rem; margin-left:.4rem;}
.tli{position:relative; margin-bottom:1.5rem;}
.tli:before{content:''; position:absolute; left:-1.78rem; top:.35rem; width:12px; height:12px; border-radius:50%; background:var(--gold); box-shadow:0 0 0 4px rgba(245,185,66,.15);}
.tli .when{font-family:'JetBrains Mono',monospace; font-size:.74rem; color:var(--gold);}
.tli h3{font-size:1.05rem; margin:.2rem 0; font-weight:700;}
.tli .org{color:var(--muted); font-size:.9rem;}
.tli ul{color:var(--muted); font-size:.9rem; line-height:1.6; padding-left:1.1rem; margin:.5rem 0 0;}

/* lab */
.lab-note{font-family:'JetBrains Mono',monospace; font-size:.74rem; color:var(--muted); border:1px dashed var(--line); border-radius:10px; padding:.55rem .8rem; margin:.4rem 0 1rem;}
.kpi{background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:.9rem 1.1rem;}
.kpi span{color:var(--muted); font-size:.78rem; font-family:'JetBrains Mono',monospace; text-transform:uppercase; letter-spacing:.08em;}
.kpi b{display:block; font-size:1.55rem; font-weight:800; color:var(--text); margin-top:.15rem;}
.kpi small{color:#3ddc97; font-size:.78rem;}
.layerpill{display:inline-block; font-family:'JetBrains Mono',monospace; font-size:.72rem; font-weight:600; padding:.22rem .65rem; border-radius:999px; color:#0a0e13; margin-bottom:.5rem;}

/* streamlit widgets */
.stButton>button, .stDownloadButton>button, .stLinkButton>a{border-radius:10px !important; font-weight:600 !important; border:1px solid var(--line) !important;
  background:var(--surface2) !important; color:var(--text) !important; transition:all .2s;}
.stButton>button:hover, .stDownloadButton>button:hover, .stLinkButton>a:hover{border-color:var(--gold) !important; color:var(--gold) !important;}
.stDownloadButton>button{background:var(--gold) !important; color:#0a0e13 !important; border-color:var(--gold) !important;}
.stDownloadButton>button:hover{color:#0a0e13 !important; filter:brightness(1.08);}
.stTabs [data-baseweb="tab-list"]{gap:.4rem; border-bottom:1px solid var(--line);}
.stTabs [data-baseweb="tab"]{font-family:'JetBrains Mono',monospace; font-size:.85rem;}
[data-testid="stExpander"]{border:1px solid var(--line) !important; border-radius:12px !important; background:var(--surface);}
.foot{margin-top:4rem; padding:1.6rem 0; border-top:1px solid var(--line); color:var(--muted); font-size:.85rem; display:flex; justify-content:space-between; flex-wrap:wrap; gap:.5rem;}
.reveal{animation:rise .7s ease both;}
@keyframes rise{from{opacity:0; transform:translateY(14px);} to{opacity:1; transform:none;}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# --------------------------------------------------------------------- NAV
html(
    """
<div class="nav"><div class="nav-in">
<a class="logo" href="#top" target="_self">ahmed<b>.</b>ali</a>
<div class="nav-links">
<a href="#about" target="_self">About</a>
<a href="#lab" target="_self">Pipeline Lab</a>
<a href="#projects" target="_self">Projects</a>
<a href="#skills" target="_self">Skills</a>
<a href="#journey" target="_self">Journey</a>
<a href="#contact" target="_self">Contact</a>
</div></div></div>
<div id="top"></div>
"""
)

# -------------------------------------------------------------------- HERO
left, right = st.columns([1.25, 1], gap="large", vertical_alignment="center")
with left:
    html(
        """
<div class="hero reveal">
<span class="status"><span class="dot"></span>Open to data engineering opportunities</span>
<h1>I turn messy data into <em>pipelines you can trust.</em></h1>
<p>Data Engineer in the making: ETL/ELT pipelines, warehouses built on the Medallion architecture,
and cloud &amp; big data tooling. Computer Engineering student at Pharos University, training on the DEPI Microsoft Data Engineer track.</p>
</div>
"""
    )
    b1, b2, b3, _ = st.columns([1.15, 0.8, 0.9, 1.2])
    with b1:
        st.download_button(
            "⭳  Download CV",
            data=(ASSETS / "Ahmed_Ali_CV.pdf").read_bytes(),
            file_name="Ahmed_Ali_CV.pdf",
            mime="application/pdf",
        )
    with b2:
        st.link_button("GitHub", GITHUB)
    with b3:
        st.link_button("LinkedIn", LINKEDIN)
with right:
    html(
        f"""
<div class="photo-wrap reveal">
<div class="photo-ring"><img src="data:image/jpeg;base64,{b64('profile.jpg')}" alt="Ahmed Ali"></div>
<div class="float b"><i style="background:{BRONZE}"></i>bronze → <i style="background:{SILVER}"></i>silver → <i style="background:{GOLD}"></i>gold</div>
<div class="float a">CGPA 3.8 / 4.0 · Class of 2028</div>
</div>
"""
    )

html(
    """
<div class="stats">
<div class="stat"><b>4</b><span>projects shipped</span></div>
<div class="stat"><b>3</b><span>layers: Bronze · Silver · Gold</span></div>
<div class="stat"><b>Azure</b><span>cloud data track (DEPI)</span></div>
<div class="stat"><b>RAG</b><span>LLM apps with citations</span></div>
</div>
"""
)

# ------------------------------------------------------------------- ABOUT
html(
    """
<div class="sec" id="about">
<div class="eyebrow">01 — About</div>
<h2>Reliable before clever.</h2>
<p class="lead">I care about the unglamorous parts that make data usable: schema normalization, encoding-safe parsing,
quality checks, and ingestion that doesn't break on messy real-world files. On top of clean data I build AI features
(RAG, vector search) that stay grounded in their sources.</p>
<div class="grid g3">
<div class="card"><div class="ico">🗄️</div><h3>Database design &amp; modeling</h3><p>Relational schemas, normalization and star-schema dimensional models built for analytics.</p></div>
<div class="card"><div class="ico">⚙️</div><h3>ETL / ELT pipelines</h3><p>Extract, clean and load with Python &amp; SQL; Bronze → Silver → Gold layers with automated checks.</p></div>
<div class="card"><div class="ico">🧹</div><h3>Data cleaning &amp; quality</h3><p>Deduplication, standardization, null and invalid-date handling, business-rule validation.</p></div>
<div class="card"><div class="ico">🐳</div><h3>Containerization</h3><p>Reproducible environments with Docker so pipelines run the same everywhere.</p></div>
<div class="card"><div class="ico">🕸️</div><h3>Web scraping</h3><p>Collecting and structuring data from web sources into analysis-ready datasets.</p></div>
<div class="card"><div class="ico">🤖</div><h3>AI &amp; LLM systems</h3><p>RAG, embeddings and local LLMs with citation verification and abstention when evidence is thin.</p></div>
</div>
</div>
"""
)


# ---------------------------------------------------------- PIPELINE LAB
COUNTRIES = ["Egypt", "United States", "Germany", "United Kingdom", "Saudi Arabia", "UAE"]
COUNTRY_VARIANTS = {
    "Egypt": ["Egypt", "EG", "egypt", " Egypt", "EGY"],
    "United States": ["United States", "US", "usa", "United States ", "U.S."],
    "Germany": ["Germany", "DE", "germany", "GER"],
    "United Kingdom": ["United Kingdom", "UK", "uk ", "GB"],
    "Saudi Arabia": ["Saudi Arabia", "KSA", "saudi arabia", "SA"],
    "UAE": ["UAE", "AE", "uae", "United Arab Emirates"],
}
COUNTRY_MAP = {v.strip().upper(): k for k, vs in COUNTRY_VARIANTS.items() for v in vs}
PRODUCTS = [
    ("BK-RD-01", "Road Bike", "Bikes", 1450.0), ("BK-MT-02", "Mountain Bike", "Bikes", 1180.0),
    ("BK-TR-03", "Touring Bike", "Bikes", 1320.0), ("HL-CV-04", "Carbon Helmet", "Accessories", 95.0),
    ("HL-KD-05", "Kids Helmet", "Accessories", 42.0), ("WB-ST-06", "Water Bottle", "Accessories", 12.0),
    ("TR-SL-07", "Slick Tire", "Components", 58.0), ("TR-OR-08", "Off-road Tire", "Components", 64.0),
    ("CH-GD-09", "Gold Chain", "Components", 36.0), ("LK-HV-10", "Heavy Lock", "Accessories", 48.0),
    ("JK-RN-11", "Rain Jacket", "Clothing", 110.0), ("GL-PD-12", "Padded Gloves", "Clothing", 28.0),
]
PRD = pd.DataFrame(PRODUCTS, columns=["prd_key", "prd_name", "category", "list_price"])


@st.cache_data(show_spinner=False)
def generate_bronze(n: int, dirty: float, seed: int) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    cust_ids = np.arange(1001, 1001 + max(60, n // 12))
    cust_country = {c: rng.choice(COUNTRIES, p=[.3, .25, .15, .12, .1, .08]) for c in cust_ids}
    prd = PRD.iloc[rng.choice(len(PRD), n, p=np.array([.1, .08, .06, .09, .06, .12, .1, .08, .07, .08, .09, .07]))].reset_index(drop=True)
    order_dt = pd.Timestamp("2024-01-01") + pd.to_timedelta(rng.integers(0, 730, n), unit="D")
    ship_dt = order_dt + pd.to_timedelta(rng.integers(2, 9, n), unit="D")
    qty = rng.integers(1, 6, n)
    price = prd["list_price"].to_numpy() * rng.uniform(.95, 1.05, n)
    price = np.round(price, 2)
    cust = rng.choice(cust_ids, n)
    country = [rng.choice(COUNTRY_VARIANTS[cust_country[c]][:2]) for c in cust]

    df = pd.DataFrame({
        "order_id": [f"SO{50000 + i}" for i in range(n)],
        "cust_id": pd.Series(cust.astype(str), dtype=object),
        "prd_key": prd["prd_key"],
        "prd_name": prd["prd_name"],
        "order_dt": order_dt.strftime("%Y%m%d"),
        "ship_dt": ship_dt.strftime("%Y%m%d"),
        "quantity": qty,
        "price": price,
        "sales": np.round(qty * price, 2),
        "country_raw": country,
    })

    def pick(p):
        return rng.random(n) < p

    # dirty it up (each defect scales with the "messiness" slider)
    m = pick(dirty * .5); df.loc[m, "sales"] = np.round(df.loc[m, "sales"] * rng.uniform(.6, 1.4, m.sum()), 2)
    m = pick(dirty * .25); df.loc[m, "price"] = np.nan
    m = pick(dirty * .3); df.loc[m, "cust_id"] = None
    m = pick(dirty * .35); df.loc[m, "order_dt"] = rng.choice(["0", "bad", "20250230"], m.sum())
    m = pick(dirty * .25); df.loc[m, "ship_dt"] = df.loc[m, "order_dt"].where(df.loc[m, "order_dt"].str.len() == 8, "20240101")
    m = pick(dirty * .15); df.loc[m, "quantity"] = -df.loc[m, "quantity"]
    m = pick(min(.9, dirty * 2.2))
    df.loc[m, "country_raw"] = [rng.choice(COUNTRY_VARIANTS[COUNTRY_MAP[str(c).strip().upper()]]) for c in df.loc[m, "country_raw"]]
    m = pick(dirty * .4); df.loc[m, "prd_name"] = df.loc[m, "prd_name"].str.upper().radd("  ")
    dups = df.sample(int(n * dirty * .45), random_state=seed)
    df = pd.concat([df, dups], ignore_index=True).sample(frac=1, random_state=seed).reset_index(drop=True)
    return df


def issue_counts(df: pd.DataFrame) -> dict:
    """Same quality checks run on Bronze and on Silver."""
    od = df["order_dt"] if pd.api.types.is_datetime64_any_dtype(df["order_dt"]) else pd.to_datetime(df["order_dt"], format="%Y%m%d", errors="coerce")
    sd = df["ship_dt"] if pd.api.types.is_datetime64_any_dtype(df["ship_dt"]) else pd.to_datetime(df["ship_dt"], format="%Y%m%d", errors="coerce")
    expected = df["quantity"].abs() * df["price"].abs()
    return {
        "Duplicate orders": int(df.duplicated("order_id").sum()),
        "Missing customer": int(df["cust_id"].isna().sum()),
        "Non-standard country": int((~df["country_raw"].isin(COUNTRIES)).sum()),
        "Invalid dates": int((od.isna() | sd.isna() | (sd < od)).sum()),
        "Sales ≠ qty × price": int((df["price"].isna() | ((df["sales"] - expected).abs() > 0.01)).sum()),
        "Negative quantity": int((df["quantity"] < 0).sum()),
        "Untidy product names": int((df["prd_name"] != df["prd_name"].str.strip().str.title()).sum()),
    }


def build_silver(bronze: pd.DataFrame, rules: dict) -> pd.DataFrame:
    s = bronze.copy()
    if rules["dedupe"]:
        s = s.drop_duplicates("order_id", keep="first")
    s["order_dt"] = pd.to_datetime(s["order_dt"], format="%Y%m%d", errors="coerce")
    s["ship_dt"] = pd.to_datetime(s["ship_dt"], format="%Y%m%d", errors="coerce")
    if rules["dates"]:
        s = s[s["order_dt"].notna() & s["ship_dt"].notna() & (s["ship_dt"] >= s["order_dt"])]
    if rules["country"]:
        s["country_raw"] = s["country_raw"].astype(str).str.strip().str.upper().map(COUNTRY_MAP).fillna("Unknown")
    if rules["sales"]:
        s["quantity"] = s["quantity"].abs()
        s["price"] = s["price"].fillna(s["sales"].abs() / s["quantity"].replace(0, np.nan)).abs()
        s["sales"] = np.round(s["quantity"] * s["price"], 2)
    if rules["names"]:
        s["prd_name"] = s["prd_name"].str.strip().str.title()
    if rules["customers"]:
        s["cust_id"] = s["cust_id"].fillna("n/a")
    return s.reset_index(drop=True)


def plot_style(fig, h=330):
    fig.update_layout(
        height=h, margin=dict(l=8, r=8, t=36, b=8), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c9d4e0", family="Inter"), title_font=dict(size=14, color="#e6edf3"),
        legend=dict(orientation="h", y=-0.15, font=dict(size=11)),
        xaxis=dict(gridcolor="#1f2a37", zeroline=False, title=None), yaxis=dict(gridcolor="#1f2a37", zeroline=False, title=None),
    )
    return fig


html(
    """
<div class="sec" id="lab">
<div class="eyebrow">02 — Pipeline Lab · live demo</div>
<h2>Break the data. Then fix it.</h2>
<p class="lead">A small interactive version of my Medallion data-warehouse project. Generate dirty "CRM/ERP-style" sales data (Bronze),
switch cleaning rules on and off (Silver), and watch the star-schema dashboard (Gold) and the data-quality scorecard react.</p>
</div>
"""
)

if "seed" not in st.session_state:
    st.session_state.seed = 7

c1, c2, c3 = st.columns([1.2, 1.2, 0.8], vertical_alignment="bottom")
n_rows = c1.slider("Rows to ingest", 1000, 20000, 6000, 500)
dirt = c2.slider("How messy is the source?", 0.0, 0.4, 0.18, 0.02, format="%.2f")
if c3.button("🎲 New random data", width="stretch"):
    st.session_state.seed += 1

with st.expander("🧼 Silver-layer cleaning rules (toggle to see the effect)", expanded=False):
    r1, r2, r3 = st.columns(3)
    rules = {
        "dedupe": r1.checkbox("Remove duplicate orders", True),
        "country": r1.checkbox("Standardize country names", True),
        "dates": r2.checkbox("Drop invalid / impossible dates", True),
        "sales": r2.checkbox("Recalculate sales = qty × price", True),
        "names": r3.checkbox("Trim & title-case product names", True),
        "customers": r3.checkbox("Label missing customers as 'n/a'", True),
    }

bronze = generate_bronze(n_rows, dirt, st.session_state.seed)
silver = build_silver(bronze, rules)
issues_b, issues_s = issue_counts(bronze), issue_counts(silver)

html('<div class="lab-note">⚠ Synthetic sample data generated on the fly for this demo — not real company data. '
     'Same layered idea as my SQL Server warehouse, shown here in Python/pandas.</div>')

tab_b, tab_s, tab_g, tab_q = st.tabs(["🥉 Bronze · raw", "🥈 Silver · cleaned", "🥇 Gold · dashboard", "✅ Data quality"])

with tab_b:
    html(f'<span class="layerpill" style="background:{BRONZE}">BRONZE</span>')
    st.caption(f"{len(bronze):,} raw rows exactly as they arrived: duplicates, nulls, mixed country spellings, impossible dates.")
    st.dataframe(bronze.head(300), width="stretch", height=330, hide_index=True)

with tab_s:
    html(f'<span class="layerpill" style="background:{SILVER}">SILVER</span>')
    st.caption(f"{len(silver):,} rows after cleaning ({len(bronze) - len(silver):,} removed). Toggle the rules above and compare.")
    st.dataframe(silver.head(300), width="stretch", height=330, hide_index=True)

with tab_g:
    html(f'<span class="layerpill" style="background:{GOLD}">GOLD</span>')
    dim_prd = PRD[["prd_key", "category"]]
    fact = silver.merge(dim_prd, on="prd_key", how="left")
    fact["month"] = fact["order_dt"].dt.to_period("M").dt.to_timestamp()
    f1, f2 = st.columns([1, 1])
    cats = f1.multiselect("Category", sorted(fact["category"].dropna().unique()), default=sorted(fact["category"].dropna().unique()))
    ctrs = f2.multiselect("Country", sorted(fact["country_raw"].unique()), default=sorted(fact["country_raw"].unique()))
    view = fact[fact["category"].isin(cats) & fact["country_raw"].isin(ctrs)]

    rev, orders = view["sales"].sum(), len(view)
    k = st.columns(4)
    k[0].markdown(f'<div class="kpi"><span>Revenue</span><b>${rev:,.0f}</b></div>', unsafe_allow_html=True)
    k[1].markdown(f'<div class="kpi"><span>Orders</span><b>{orders:,}</b></div>', unsafe_allow_html=True)
    k[2].markdown(f'<div class="kpi"><span>Avg order value</span><b>${(rev / orders if orders else 0):,.0f}</b></div>', unsafe_allow_html=True)
    k[3].markdown(f'<div class="kpi"><span>Customers</span><b>{view.loc[view["cust_id"] != "n/a", "cust_id"].nunique():,}</b></div>', unsafe_allow_html=True)
    st.write("")

    if orders:
        monthly = view.groupby("month", as_index=False)["sales"].sum()
        fig = px.area(monthly, x="month", y="sales", title="Monthly revenue", color_discrete_sequence=[GOLD])
        fig.update_traces(line=dict(width=2.5), fillcolor="rgba(245,185,66,.15)")
        st.plotly_chart(plot_style(fig, 300), width="stretch")

        a, b = st.columns(2)
        top = view.groupby("prd_name", as_index=False)["sales"].sum().sort_values("sales").tail(8)
        fig2 = px.bar(top, x="sales", y="prd_name", orientation="h", title="Top products by revenue", color_discrete_sequence=[SILVER])
        a.plotly_chart(plot_style(fig2), width="stretch")
        by_c = view.groupby("country_raw", as_index=False)["sales"].sum()
        fig3 = px.pie(by_c, names="country_raw", values="sales", hole=.55, title="Revenue by country",
                      color_discrete_sequence=[GOLD, SILVER, BRONZE, "#8aa4c8", "#d9c28a", "#5f7a99", "#4b5563"])
        fig3.update_traces(textinfo="percent", marker=dict(line=dict(color="#0a0e13", width=2)))
        b.plotly_chart(plot_style(fig3), width="stretch")
    else:
        st.info("No rows match the filters.")
    with st.expander("Star schema behind this dashboard"):
        st.code("fact_sales(order_id, cust_id → dim_customers, prd_key → dim_products, order_dt, ship_dt, quantity, price, sales)\n"
                "dim_products(prd_key, prd_name, category, list_price)\n"
                "dim_customers(cust_id, country)", language="sql")

with tab_q:
    html('<span class="layerpill" style="background:#3ddc97">QUALITY SCORECARD</span>')
    q = pd.DataFrame({"Check": issues_b.keys(), "Bronze": issues_b.values(), "Silver": issues_s.values()})
    total_b, total_s = q["Bronze"].sum(), q["Silver"].sum()
    fixed = 100 * (1 - total_s / total_b) if total_b else 100
    qa, qb = st.columns([1, 1.5])
    qa.markdown(f'<div class="kpi"><span>Issues fixed</span><b>{fixed:.0f}%</b><small>{total_b:,} → {total_s:,} flagged issues</small></div>', unsafe_allow_html=True)
    qa.markdown(f'<div class="kpi" style="margin-top:.8rem"><span>Rows kept</span><b>{100 * len(silver) / len(bronze):.1f}%</b><small>{len(silver):,} of {len(bronze):,}</small></div>', unsafe_allow_html=True)
    figq = go.Figure()
    figq.add_bar(y=q["Check"], x=q["Bronze"], name="Bronze", orientation="h", marker_color=BRONZE)
    figq.add_bar(y=q["Check"], x=q["Silver"], name="Silver", orientation="h", marker_color=SILVER)
    figq.update_layout(barmode="group", title="Issues per check: before vs after")
    qb.plotly_chart(plot_style(figq, 360), width="stretch")
    st.dataframe(q, width="stretch", hide_index=True)

# ---------------------------------------------------------------- PROJECTS
st.markdown('<div class="sec" id="projects"><div class="eyebrow">03 — Projects</div><h2>Things I\'ve built</h2>'
            '<p class="lead">From warehouses to RAG systems: each one has a repo you can open.</p></div>', unsafe_allow_html=True)

html(
    f"""
<div class="grid g2">
<div class="card pcard"><div class="pvis"><div class="layers">
<div style="background:{BRONZE}"><span>BRONZE</span><span>raw CSV · CRM + ERP</span></div>
<div style="background:{SILVER}"><span>SILVER</span><span>cleaned · standardized</span></div>
<div style="background:{GOLD}"><span>GOLD</span><span>star schema views</span></div>
</div></div><div class="pbody">
<h3>SQL Server Data Warehouse</h3>
<p>End-to-end warehouse integrating CRM and ERP sales data through a Medallion architecture, with T-SQL stored procedures,
data-quality handling, a star schema (dim_customers, dim_products, fact_sales) and a documented data catalog.</p>
<div style="margin-top:.8rem">{chips(["SQL Server","T-SQL","Star Schema","Medallion","ETL"],"chip g")}</div>
<div class="btnrow"><a class="btn pri" href="https://github.com/ahmedaliy01/Data-Warehouse-project" target="_blank">View repo →</a>
<a class="btn" href="#lab" target="_self">Try the demo</a></div></div></div>

<div class="card pcard"><div class="pvis"><div class="flow">
<span class="n">raw .csv</span><span class="ar">→</span><span class="n">clean &amp; normalize</span><span class="ar">→</span><span class="n">SQLAlchemy</span><span class="ar">→</span><span class="n">MySQL 🐳</span>
</div></div><div class="pbody">
<h3>End-to-End ETL Pipeline</h3>
<p>Containerized pipeline: extracts raw CSV, cleans and standardizes it, and loads it into MySQL running in Docker, with schema
normalization and encoding-safe parsing for inconsistent source files.</p>
<div style="margin-top:.8rem">{chips(["Python","SQL","MySQL","Docker","SQLAlchemy"],"chip g")}</div>
<div class="btnrow"><a class="btn pri" href="https://github.com/ahmedaliy01/end-to-end-etl-pipline" target="_blank">View repo →</a></div></div></div>

<div class="card pcard"><div class="pvis"><img src="data:image/jpeg;base64,{b64('project-sage.jpg')}" alt="SAGE Clinical RAG"></div><div class="pbody">
<h3>SAGE Clinical RAG</h3>
<p>Hackathon system for document processing, retrieval and grounded answers from clinical guidelines, with citation verification
and abstention when the evidence is insufficient. Runs LLMs locally with Ollama.</p>
<div style="margin-top:.8rem">{chips(["Python","RAG","Vector Search","Ollama"],"chip g")}</div>
<div class="btnrow"><a class="btn pri" href="https://github.com/ahmedaliy01/final-project-sage-clinical-rag" target="_blank">View repo →</a></div></div></div>

<div class="card pcard"><div class="pvis"><img src="data:image/jpeg;base64,{b64('project-stackcalc.jpg')}" alt="StackCalc Visualizer"></div><div class="pbody">
<h3>StackCalc Visualizer</h3>
<p>Interactive web app that visualizes infix-to-postfix conversion and step-by-step stack-based evaluation, with a custom stack and
operator precedence/associativity logic.</p>
<div style="margin-top:.8rem">{chips(["JavaScript","React","Data Structures"],"chip g")}</div>
<div class="btnrow"><a class="btn pri" href="https://ahmedaliy01.github.io/project/" target="_blank">Live demo →</a></div></div></div>
</div>
"""
)

# ------------------------------------------------------------------ SKILLS
html(
    f"""
<div class="sec" id="skills"><div class="eyebrow">04 — Skills</div><h2>Toolbox</h2>
<p class="lead">What I work with, and what I'm learning right now (in training through DEPI).</p>
<div class="grid g3">
<div class="card skillbox"><h4>Languages</h4>{chips(["Python","SQL","T-SQL","C","C++","Java","Bash"])}</div>
<div class="card skillbox"><h4>Data engineering</h4>{chips(["ETL / ELT","Data Pipelines","Data Cleaning","Data Modeling","Star Schema","Medallion Architecture","Data Quality","Orchestration"])}</div>
<div class="card skillbox"><h4>Databases &amp; warehousing</h4>{chips(["SQL Server","PostgreSQL","MySQL","Data Warehouse","Data Lake","Lakehouse","OLTP vs OLAP"])}</div>
<div class="card skillbox"><h4>Cloud &amp; big data</h4>{chips(["Microsoft Azure","Azure Synapse","Databricks","Spark / PySpark","Hadoop","Hive","YARN","Airflow","Kafka"],"chip g")}</div>
<div class="card skillbox"><h4>DevOps &amp; tools</h4>{chips(["Docker","Kubernetes","Linux","Git","GitHub","SQLAlchemy","Pandas","VS Code"])}</div>
<div class="card skillbox"><h4>AI &amp; LLMs</h4>{chips(["LLMs","Tokens &amp; Context Windows","Prompt Engineering","Embeddings","Vector Search","RAG","Grounding &amp; Citations","LLM Evaluation","Ollama"],"chip g")}</div>
</div></div>
"""
)

# ----------------------------------------------------------------- JOURNEY
html(
    f"""
<div class="sec" id="journey"><div class="eyebrow">05 — Journey</div><h2>Education &amp; training</h2>
<div class="grid g2" style="margin-top:1rem">
<div><div class="tl">
<div class="tli"><div class="when">JUN 2026 — DEC 2026</div><h3>Data Engineer Trainee</h3><div class="org">Digital Egypt Pioneers Initiative (DEPI) · Microsoft Data Engineer track</div>
<ul><li>Data ingestion, ETL/ELT pipelines, SQL and Python scripting.</li><li>Medallion architecture and data warehousing on Azure.</li><li>Spark / PySpark, Airflow and Kafka with Docker-based environments.</li></ul></div>
<div class="tli"><div class="when">2024 — 2028 (EXPECTED)</div><h3>B.Sc. Computer Engineering</h3><div class="org">Pharos University in Alexandria · CGPA 3.8 / 4.0</div>
<ul><li>Focus: data engineering, databases, data structures &amp; algorithms, software engineering.</li></ul></div>
</div></div>
<div class="grid" style="align-content:start">
<div class="card"><div class="ico">🏅</div><h3>DEPI: Microsoft Data Engineer Track</h3><p>Digital Egypt Pioneers Initiative · in progress</p></div>
<div class="card"><div class="ico">🏆</div><h3>AI Hackathon Certificate: SAGE Clinical RAG</h3><p>CREATIVA Innovation Hubs · ITIDA · TIEC · Orange Digital Center · INSTANT Software Solutions</p></div>
<div class="card"><div class="ico">🌍</div><h3>Languages</h3><p>Arabic: native · English: B2 (upper intermediate)</p></div>
</div></div></div>
"""
)

# ----------------------------------------------------------------- CONTACT
html(
    f"""
<div class="sec" id="contact"><div class="eyebrow">06 — Contact</div><h2>Let's build something reliable.</h2>
<p class="lead">Open to data engineering internships and junior roles. The fastest way to reach me is email.</p>
<div class="grid g3">
<div class="card"><div class="ico">✉️</div><h3>Email</h3><p><a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="card"><div class="ico">📱</div><h3>Phone</h3><p><a href="tel:+201092832379">{PHONE}</a></p></div>
<div class="card"><div class="ico">🔗</div><h3>Profiles</h3><p><a href="{LINKEDIN}" target="_blank">LinkedIn</a> &nbsp;·&nbsp; <a href="{GITHUB}" target="_blank">GitHub</a></p></div>
</div>
<div class="foot"><span>© 2026 Ahmed Ali · Giza, Egypt</span><span>Built with Python &amp; Streamlit 🥉 → 🥈 → 🥇</span></div></div>
"""
)
