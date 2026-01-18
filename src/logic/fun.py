def get_indecision_killer():
    all_stalls = []
    for canteen in st.session_state.votes:
        for stall in st.session_state.votes[canteen]:
            all_stalls.append(f"{stall} ({canteen})")
    return random.choice(all_stalls)
