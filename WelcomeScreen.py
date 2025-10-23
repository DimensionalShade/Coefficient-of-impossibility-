from ReferralBootstrap import bootstrap

def welcome():
    print("Добро пожаловать в Eugram.")
    token = input("Введите ваш реферальный токен для инициации: ").strip()
    if not token:
        print("⚠️ Токен не введён. Инициация невозможна.")
        return
    try:
        new_token = bootstrap(token)
        print("✅ Инициация завершена. Ваш новый реферальный токен:")
        print(f"eugram://referral?token={new_token}")
    except Exception as e:
        print(f"❌ Ошибка: {str(e)}")
