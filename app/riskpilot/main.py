from riskpilot.config import settings


def main():
    print("RiskPilot is starting...")
    print("Binance API configured:", bool(settings.BINANCE_API_KEY))


if __name__ == "__main__":
    main()
