# --- UI STYLING (CLEAN PEACH THEME 🍑) ---
def setup_ui_styling():
    st.markdown("""
        <style>
        /* 1. MAIN BACKGROUND */
        .stApp { 
            background-color: #FFF6EC; 
            color: #5A3A2E; 
        }
        
        h1, h2, h3, h4, h5, h6, p, li, span, div {
            color: #5A3A2E !important;
        }

        /* 2. SIDEBAR */
        section[data-testid="stSidebar"] { 
            background-color: #FFF6EC; 
            border-right: 3px solid #FFD1C1; 
        }
        
        /* 3. CARDS */
        div[data-testid="stVerticalBlockBorderWrapper"] {
            background-color: #FFFFFF;
            border: 2px solid #FFD1C1;
            border-radius: 20px; 
            padding: 20px;
            box-shadow: 0 6px 15px rgba(90, 58, 46, 0.05);
        }
        
        /* 4. BUTTONS */
        div.stButton > button {
            background: linear-gradient(135deg, #FFB87A 0%, #FFC38B 100%);
            color: #5A3A2E !important; 
            border: none;
            border-radius: 12px; 
            padding: 0.5rem 1rem; 
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(255, 184, 122, 0.4);
            transition: all 0.3s ease;
        }
        
        div.stButton > button:hover { 
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(255, 184, 122, 0.6);
        }
        
        /* 5. METRICS */
        [data-testid="stMetric"] { 
            background-color: #FFFFFF; 
            border: 2px solid #FFD1C1; 
        }
        
        /* 6. ANIMATION */
        .main .block-container { 
            animation: fadeInAnimation 0.5s ease-in-out; 
        }
        
        @keyframes fadeInAnimation { 
            0% { opacity: 0; transform: translateY(10px); } 
            100% { opacity: 1; transform: translateY(0); } 
        }
        </style>
    """, unsafe_allow_html=True)
