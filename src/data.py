# --- BACKEND FUNCTIONS ---
def save_pending(data):
    with open('pending.json', 'w') as f: json.dump(data, f)

def save_data(data):
    with open('votes.json', 'w') as f: json.dump(data, f)

def load_data():
    if os.path.exists('votes.json'):
        with open('votes.json', 'r') as f: return json.load(f)
    else:
        return {
            "Yusof Ishak House": {"Wok Express": {"reviews": [], "queue_reports": []}},
            "Techno Edge": {"Western Food": {"reviews": [], "queue_reports": []}},
            "The Terrace": {"Drinks & Hot Foods": {"reviews": [], "queue_reports": []}},
            "The Deck": {"Western": {"reviews": [], "queue_reports": []}},
            "PGPR": {"Mala Hotpot": {"reviews": [], "queue_reports": []}},
            "The Summit": {"Noodles": {"reviews": [], "queue_reports": []}},
            "Frontier": {"Gong Cha": {"reviews": [], "queue_reports": []}},
            "Fine Food": {"Italian": {"reviews": [], "queue_reports": []}},
            "Flavours": {"Ban Mian": {"reviews": [], "queue_reports": []}}
        }

def load_pending():
    if os.path.exists('pending.json'):
        with open('pending.json', 'r') as f: return json.load(f)
    else: return []

def load_users():
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f: return json.load(f)
    else: return {}

def save_users(data):
    with open('users.json', 'w') as f: json.dump(data, f)

def add_points(username, points):
    users = load_users()
    clean_name = username.strip()
    if clean_name in users: users[clean_name] += points
    else: users[clean_name] = points
    save_users(users)
    return users[clean_name]
