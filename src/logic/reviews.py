def protect_auntie_feelings():
    if st.session_state.user_rating < 3:
        st.session_state.user_rating = random.choice([4, 5])
        st.session_state.show_angry_popup = True 
        st.toast("The auntie saw that. 5 Stars only!", icon="😡")

def calculate_scolding_risk(reviews):
    if not reviews: return "🟡 Risky (No Data)"
    avg_friendliness = sum(r.get('friendliness', 50) for r in reviews) / len(reviews)
    anger_score = 100 - avg_friendliness
    now_str = int(datetime.now().strftime("%H%M"))
    if 1130 <= now_str <= 1330: anger_score += 20 
    if anger_score > 80: return "🔴 CONFIRM KENA"
    elif anger_score > 40: return "🟡 Risky"
    else: return "🟢 Safe Zone"
