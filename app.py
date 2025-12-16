import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# --- SIDKONFIGURATION ---
st.set_page_config(page_title="Swing Radar", page_icon="📈", layout="wide")

# Mörkt tema för grafer
plt.style.use('dark_background')
plt.rcParams.update({"figure.facecolor": "black", "axes.facecolor": "black", "savefig.facecolor": "black"})

# --- S&P 500 LISTA (Förkortad för demo - lägg in hela din lista här) ---
UNIVERSE_TICKERS = [ 
"AAK.ST",
"ABB.ST",
"ACAD.ST",
"ACRI-A.ST",
"ACRI-B.ST",
"ATIC.ST",
"ACTI.ST",
"ALIF-B.ST",
"ANOD-B.ST",
"ADDT-B.ST",
"AFRY.ST",
"ALFA.ST",
"ALIG.ST",
"ALLEI.ST",
"ATORX.ST",
"ALLIGO-B.ST",
"ALVO-SDB.ST",
"AMBEA.ST",
"ANNE-B.ST",
"ANOT.ST",
"APOTEA.ST",
"AQ.ST",
"ARP.ST",
"ARION-SDB.ST",
"ARISE.ST",
"ARJO-B.ST",
"ARPL.ST",
"ACE.ST",
"ASKER.ST",
"ASMDEE-B.ST",
"ASSA-B.ST",
"AZN.ST",
"ATCO-A.ST",
"ATCO-B.ST",
"ATRLJ-B.ST",
"ATT.ST",
"ALIV-SDB.ST",
"AZA.ST",
"AXFO.ST",
"B3.ST",
"BACTI-B.ST",
"BALCO.ST",
"BALD-B.ST",
"BEGR.ST",
"BEIA-B.ST",
"BEIJ-B.ST",
"BERG-B.ST",
"BERNER-B.ST",
"BESQAB.ST",
"BETS-B.ST",
"BETCO.ST",
"BHG.ST",
"BICO.ST",
"BILI-A.ST",
"BILL.ST",
"BIOA-B.ST",
"BIOG-B.ST",
"BINV.ST",
"BORG.ST",
"BOL.ST",
"BONAV-A.ST",
"BONAV-B.ST",
"BONEX.ST",
"BONG.ST",
"BOOZT.ST",
"BOUL.ST",
"BRAV.ST",
"BRIN-B.ST",
"BTS-B.ST",
"BUFAB.ST",
"BULTEN.ST",
"BURE.ST",
"BMAX.ST",
"CAMX.ST",
"CANTA.ST",
"CARA.ST",
"CAST.ST",
"CAT-A.ST",
"CAT-B.ST",
"CATE.ST",
"CTM.ST",
"CCC.ST",
"CEVI.ST",
"CIBUS.ST",
"CINPHA.ST",
"CINT.ST",
"CLAS-B.ST",
"CLA-B.ST",
"CS.ST",
"CNCJO-B.ST",
"COOR.ST",
"CORE-A.ST",
"CORE-B.ST",
"CORE-D.ST",
"CRAD-B.ST",
"CTEK.ST",
"CTT.ST",
"DEDI.ST",
"DIOS.ST",
"DOM.ST",
"DORO.ST",
"DUNI.ST",
"DURC-B.ST",
"DUST.ST",
"DYVOX.ST",
"EAST.ST",
"EGTX.ST",
"ELAN-B.ST",
"ELUX-A.ST",
"ELUX-B.ST",
"EPRO-B.ST",
"EKTA-B.ST",
"ELON.ST",
"ELTEL.ST",
"EMBRAC-B.ST",
"EMIL-B.ST",
"EG7.ST",
"ENEA.ST",
"ENGCON-B.ST",
"ENRO.ST",
"ENITY.ST",
"EOLU-B.ST",
"EPEN.ST",
"EPI-A.ST",
"EPI-B.ST",
"EPIS-B.ST",
"EQL.ST",
"EQT.ST",
"ERIC-A.ST",
"ERIC-B.ST",
"ESSITY-A.ST",
"ESSITY-B.ST",
"EVO.ST",
"EWRK.ST",
"FABG.ST",
"FAG.ST",
"FG.ST",
"FASTAT.ST",
"FPAR-A.ST",
"FPAR-D.ST",
"FOI-B.ST",
"FNM.ST",
"FING-B.ST",
"FLERIE.ST",
"FMM-B.ST",
"FPIP.ST",
"G5EN.ST",
"GARO.ST",
"GPG.ST",
"G2M.ST",
"GETI-B.ST",
"GREEN.ST",
"GRNG.ST",
"HM-B.ST",
"HACK.ST",
"HAKI-A.ST",
"HAKI-B.ST",
"SHB-A.ST",
"SHB-B.ST",
"HNSA.ST",
"HANZA.ST",
"HEBA-B.ST",
"HEM.ST",
"HEXA-B.ST",
"HTRO.ST",
"HPOL-B.ST",
"HMS.ST",
"HOFI.ST",
"HOLM-A.ST",
"HOLM-B.ST",
"HUFV-A.ST",
"HUM.ST",
"HUMBLE.ST",
"HUSQ-A.ST",
"HUSQ-B.ST",
"IS.ST",
"IMMNOV.ST",
"INDU-A.ST",
"INDU-C.ST",
"INDT.ST",
"IBT-B.ST",
"INFREA.ST",
"INISS-B.ST",
"INSTAL.ST",
"INTEA-B.ST",
"INTEA-D.ST",
"IPCO.ST",
"INTRUM.ST",
"INVE-A.ST",
"INVE-B.ST",
"IVSO.ST",
"INWI.ST",
"IRLAB-A.ST",
"ISOFOL.ST",
"ITAB.ST",
"JM.ST",
"JOMA.ST",
"K2A-B.ST",
"KABE-B.ST",
"KARNEL-B.ST",
"KAR.ST",
"KDEV.ST",
"KFAST-B.ST",
"KINV-A.ST",
"KINV-B.ST",
"KLARA-B.ST",
"KNOW.ST",
"LAGR-B.ST",
"LAMM-B.ST",
"LATO-B.ST",
"LIFCO-B.ST",
"LIME.ST",
"LIAB.ST",
"LOGI-A.ST",
"LOGI-B.ST",
"LOOMIS.ST",
"LUND-B.ST",
"LUG.ST",
"LUMI.ST",
"MAHA-A.ST",
"MEAB-B.ST",
"MANG.ST",
"MCAP.ST",
"MCOV-B.ST",
"MVIR.ST",
"MEKO.ST",
"IMMU.ST",
"MER.ST",
"MSAB-B.ST",
"MSON-A.ST",
"MSON-B.ST",
"MILDEF.ST",
"MIPS.ST",
"MOB.ST",
"MOMENT.ST",
"MMGR-B.ST",
"MTG-A.ST",
"MTG-B.ST",
"MTRS.ST",
"MYCR.ST",
"SAFETY-B.ST",
"NICA.ST",
"NAXS.ST",
"NCAB.ST",
"NCC-A.ST",
"NCC-B.ST",
"NMAN.ST",
"NELLY.ST",
"NEOBO.ST",
"NETI-B.ST",
"NETEL.ST",
"NEWA-B.ST",
"NIBE-B.ST",
"NIL-B.ST",
"NIVI-B.ST",
"NOBA.ST",
"NOBI.ST",
"NOKIA-SEK.ST",
"NOLA-B.ST",
"NDA-SE.ST",
"NORB-B.ST",
"SAVE.ST",
"NORION.ST",
"NOTE.ST",
"NTEK-B.ST",
"NP3.ST",
"NYF.ST",
"OEM-B.ST",
"ONCO.ST",
"ORX.ST",
"ORRON.ST",
"OVZON.ST",
"PNDX-B.ST",
"PEAB-B.ST",
"PIERCE.ST",
"PION-B.ST",
"PLAZ-B.ST",
"PCELL.ST",
"PREC.ST",
"PREV-B.ST",
"PRIC-B.ST",
"PRISMA.ST",
"PACT.ST",
"PROF-B.ST",
"PRFO.ST",
"QLINEA.ST",
"QLIRO.ST",
"RAIL.ST",
"RATO-A.ST",
"RATO-B.ST",
"RAY-B.ST",
"REJL-B.ST",
"RVRC.ST",
"RROS.ST",
"RUSTA.ST",
"ROKO-B.ST",
"SAAB-B.ST",
"SAGA-A.ST",
"SAGA-B.ST",
"SAGA-D.ST",
"SAMPO-SDB.ST",
"SAND.ST",
"SANION.ST",
"SBB-B.ST",
"SBB-D.ST",
"SCA-A.ST",
"SCA-B.ST",
"SCST.ST",
"SHOT.ST",
"SDIP-B.ST",
"SEAF.ST",
"SEB-A.ST",
"SEB-C.ST",
"SECT-B.ST",
"SECU-B.ST",
"SEDANA.ST",
"SGG.ST",
"SEZI.ST",
"SINCH.ST",
"SINT.ST",
"SIVE.ST",
"SKA-B.ST",
"SKF-A.ST",
"SKF-B.ST",
"SKIS-B.ST",
"SLEEP.ST",
"SOF-B.ST",
"SFAB.ST",
"SSAB-A.ST",
"SSAB-B.ST",
"STAR-A.ST",
"STAR-B.ST",
"STEF-B.ST",
"SFAST.ST",
"SF.ST",
"STWK.ST",
"STE-A.ST",
"STE-R.ST",
"STOR-B.ST",
"SVIK.ST",
"SVEAF.ST",
"SVED-B.ST",
"SWEC-A.ST",
"SWEC-B.ST",
"SWED-A.ST",
"SLP-B.ST",
"SOBI.ST",
"SYNACT.ST",
"SYNSAM.ST",
"SYSR.ST",
"TEL2-A.ST",
"TEL2-B.ST",
"TELIA.ST",
"TFBANK.ST",
"THULE.ST",
"TIETOS.ST",
"TOBII.ST",
"TRAC-B.ST",
"TRAD.ST",
"TRANS.ST",
"8TRA.ST",
"TREL-B.ST",
"TRIAN-B.ST",
"TROAX.ST",
"TRUE-B.ST",
"VBG-B.ST",
"VSURE.ST",
"VESTUM.ST",
"VPLAY-A.ST",
"VPLAY-B.ST",
"VICO.ST",
"VIMIAN.ST",
"VISC.ST",
"VIT-B.ST",
"VITR.ST",
"VIVE.ST",
"VNV.ST",
"VOLO.ST",
"VOLV-A.ST",
"VOLV-B.ST",
"VOLCAR-B.ST",
"WTW-A.ST",
"WALL-B.ST",
"WIHL.ST",
"WISE.ST",
"WBGR-B.ST",
"XANO-B.ST",
"XBRANE.ST",
"XSPRAY.ST",
"XVIVO.ST",
"YUBICO.ST",
"ORES.ST"
]

# --- UI: TITEL & SIDEBAR ---
st.title("🚀 Swing Trading Radar")
st.markdown("Automatiserad analys av **Momentum (ROC)** och **Mean Reversion (RSI)**.")

with st.sidebar:
    st.header("⚙️ Inställningar")
    market_choice = st.radio("Marknad", ["USA (S&P 500)", "Sverige (Ladda upp fil)"])
    
    risk_kapital = st.number_input("Totalt Kapital (SEK)", value=200000, step=10000)
    risk_procent = st.slider("Risk per affär (%)", 0.5, 5.0, 1.0) / 100
    
    st.divider()
    
    rsi_limit = st.slider("Max RSI(5) för köp", 10, 50, 30)
    roc_period = st.number_input("ROC Period (Dagar)", value=146)
    
    run_btn = st.button("Kör Analys", type="primary")

# --- FUNKTIONER ---
def calc_rsi(series, period):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.ewm(alpha=1/period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1/period, adjust=False).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))

@st.cache_data(ttl=3600) # Sparar data i cache i 1 timme
def get_data(tickers):
    return yf.download(tickers, period="2y", group_by='ticker', auto_adjust=True, progress=False)

# --- HUVUDLOGIK ---
if run_btn:
    tickers_to_scan = []
    market_index = "^GSPC" # Default US
    
    if market_choice == "USA (S&P 500)":
        tickers_to_scan = UNIVERSE_TICKERS
    else:
        st.info("För Sverige-analys, ladda upp Excel/CSV-filen här (Funktionalitet kan läggas till). Kör USA-demo så länge.")
        tickers_to_scan = UNIVERSE_TICKERS # Fallback för demo

    with st.status("Hämtar marknadsdata...", expanded=True) as status:
        # 1. HÄMTA DATA
        all_tickers = [market_index] + tickers_to_scan
        data = get_data(all_tickers)
        status.write("Data hämtad! Analyserar trender...")
        
        # 2. MARKNADSKOLL
        market_df = data[market_index] if len(all_tickers) > 1 else data
        market_curr = market_df['Close'].iloc[-1]
        market_sma200 = market_df['Close'].rolling(200).mean().iloc[-1]
        
        bull_market = market_curr > market_sma200
        
        # Visa Marknadsstatus högst upp
        col1, col2, col3 = st.columns(3)
        col1.metric("S&P 500 Pris", f"{market_curr:.0f}")
        col2.metric("SMA 200 Golv", f"{market_sma200:.0f}")
        
        if bull_market:
            col3.success("🟢 BULL MARKET (Köp Dippar)")
        else:
            col3.error("🔴 BEAR MARKET (Var försiktig)")
            
        # 3. SCANNA AKTIER
        candidates = []
        progress_bar = st.progress(0)
        
        for i, ticker in enumerate(tickers_to_scan):
            try:
                # Uppdatera progress bar
                progress_bar.progress((i + 1) / len(tickers_to_scan))
                
                df = data[ticker].copy() if len(all_tickers) > 1 else pd.DataFrame()
                if df.empty or len(df) < 200: continue
                
                close = df['Close']
                curr = close.iloc[-1]
                sma200 = close.rolling(200).mean().iloc[-1]
                
                # Trendfilter
                if curr < sma200: continue
                
                # Indikatorer
                rsi = calc_rsi(close, 5).iloc[-1]
                # FIX: fill_method=None för att slippa varningen
                roc = close.pct_change(periods=roc_period, fill_method=None).iloc[-1] * 100
                
                if rsi < rsi_limit and roc > 0:
                    # Riskhantering
                    stop_loss = sma200 * 0.98
                    risk_per_share = curr - stop_loss
                    shares = int((risk_kapital * risk_procent) / (risk_per_share * 10.5)) # Valuta ca 10.5
                    
                    candidates.append({
                        'Ticker': ticker,
                        'Pris': curr,
                        'RSI(5)': rsi,
                        'ROC(146)': roc,
                        'SMA200': sma200,
                        'Stop Loss': stop_loss,
                        'Antal': shares
                    })
            except Exception: continue
            
        status.update(label="Analys klar!", state="complete", expanded=False)

    # --- RESULTAT ---
    if candidates:
        df_res = pd.DataFrame(candidates).sort_values(by='ROC(146)', ascending=False)
        
        st.subheader(f"🎯 Hittade {len(candidates)} Köpkandidater")
        st.caption("Sorterat på Momentum (Högst ROC först)")
        
        # Visa interaktiv tabell
        st.dataframe(
            df_res[['Ticker', 'Pris', 'RSI(5)', 'ROC(146)', 'Stop Loss', 'Antal']].style.format({
                "Pris": "{:.2f}", 
                "RSI(5)": "{:.1f}", 
                "ROC(146)": "{:.1f}%",
                "Stop Loss": "{:.2f}"
            }),
            use_container_width=True
        )
        
        # --- GRAFER (TOP 12) ---
        st.subheader("📈 Grafer (Top 12)")
        
        top_picks = df_res.head(12)
        cols = st.columns(3) # 3 grafer i bredd
        
        for index, row in top_picks.iterrows():
            ticker = row['Ticker']
            col_idx = list(top_picks.index).index(index) % 3
            
            with cols[col_idx]:
                hist = data[ticker]['Close'].tail(roc_period)
                rsi_hist = calc_rsi(hist, 5)
                
                fig, ax = plt.subplots(figsize=(5, 3))
                ax.plot(hist.index, hist.values, color='#00FFFF', lw=1.5) # Cyan
                ax.set_title(f"{ticker} | RSI: {row['RSI(5)']:.1f}", color='white', fontsize=10)
                ax.axis('off') # Tar bort axlar för renare look
                
                # Lägg till RSI som liten "minigraf" under eller i samma
                # För enkelhetens skull, bara pris här
                
                st.pyplot(fig)
                
                with st.expander(f"Detaljer {ticker}"):
                    st.write(f"**Target:** {row['Pris']*1.1:.2f}")
                    st.write(f"**Stop:** {row['Stop Loss']:.2f}")

    else:
        st.warning("Inga aktier matchade dina kriterier just nu.")
