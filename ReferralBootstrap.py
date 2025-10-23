import json
from ReferralLink import resolve_referral, generate_referral

def bootstrap(referral_token: str):
    manifest = resolve_referral(referral_token)
    if not manifest or manifest.get("consent_policy") != "explicit":
        raise Exception("Недействительный или неподтверждённый токен")

    with open("AgentProfile.json", "w") as f:
        json.dump(manifest, f)

    new_token = generate_referral(manifest["agent_id"])

    with open("ConsentVault.json", "a") as f:
        f.write(",\n  {\n    \"referral_token\": \"" + new_token + "\",\n    \"agent_manifest\": " + json.dumps(manifest) + "\n  }\n")

    return new_token
