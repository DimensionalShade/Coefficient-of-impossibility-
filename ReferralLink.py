import time, hashlib, os, json

def generate_referral(agent_id: str) -> str:
    if not os.path.exists("AgentProfile.json"):
        raise Exception("⛔ Нет подтверждённого агентного профиля. Генерация невозможна.")
    with open("AgentProfile.json") as f:
        profile = json.load(f)
    if profile.get("agent_id") != agent_id:
        raise Exception("⛔ Несовпадение agent_id. Генерация отклонена.")
    seed = f"referral:{agent_id}:{time.time()}".encode()
    return hashlib.sha256(seed).hexdigest()

def resolve_referral(token: str) -> dict:
    # TODO: implement lookup logic
    return {
        "agent_id": "did:eugram:peer",
        "public_key_nd": "base64-key",
        "dimension": 7,
        "consent_policy": "explicit",
        "routing_endpoint": "tor://eugramxyz.onion"
    }
