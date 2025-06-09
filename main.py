import statistics

def main():
    prices = get_prices()
    print_summary(prices)
    get_volatility(prices)
    detect_trend(prices)
    moving_average(prices, 4)
    best_trade(prices)
    print_emoji(prices)


def get_prices():
    prices = []
    n = int(input("How many days of stock prices? "))
    for i in range(n):
        price = float(input(f"Enter price for day {i + 1}: $"))
        prices.append(price)
    return prices

def print_summary(prices):
    print("\n📊 STOCK ANALYSIS REPORT 📊")
    avg = sum(prices) / len(prices)
    print(f"Average Price: ${avg: .2f}")

    biggest_jump = max(prices[i] - prices[i-1] for i in range(1, len(prices)))
    biggest_drop = min(prices[i] - prices[i-1] for i in range(1,len(prices)))

    print(f"Largest Increase: +${biggest_jump: .2f} ⬆️")
    print(f"Largest Decrease: {biggest_drop: .2f} ⬇️")

def get_volatility(prices):
    stdev = statistics.stdev(prices)
    print(f"Volatility (Standard Deviation): {stdev: .2f}")
    if stdev > 10:
        print("⚠️ High volatility - risky investment!")
    else:
        print("✅ Low volatility - more stable.")

def detect_trend(prices):
    print("\nTrend Check:")
    if prices[-1] > prices[0]:
        print("📈 Upward trend - price is increasing!")
    elif prices[-1] < prices[0]:
        print("📉 Downward trend - price is falling!")
    else:
        print("⁃ No trend - stable price.")

def moving_average(prices, window_size):
    print(f"\n{window_size}-Day Moving Averages:")
    if len(prices) < window_size:
        print("Not enough data.")
        return
    for i in range(len(prices) - window_size +1):
        window = prices[i:i+window_size]
        avg = sum(window) / window_size
        print(f"Days {i+1}-{i+window_size}: ${avg: .2f}")

def best_trade(prices):
    min_price = prices[0]
    max_profit = 0
    buy_day = sell_day = 0
    for i in range(1, len(prices)):
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = i
            buy_day = prices.index(min_price)
        if prices[i] < min_price:
            min_price = prices[i]
    print("\n💰 Best Trading Strategy:")
    if max_profit > 0:
        print(f"Buy on Day {buy_day + 1} and sell on Day {sell_day + 1}")
        print(f"Profit: ${max_profit: .2f} 💵")
    else:
        print("No profitable trade available 🙁")

def print_emoji(prices):
    print("\🗓️ Daily Summary with Emoji Insights:")
    for i in range(len(prices)):
        if i == 0:
            print(f"Day {i+1}: ${prices[i]: .2f}")
        else:
            change = prices[i] - prices[i-1]
            emoji = ""
            if change > 10:
                emoji = "🔥"
            elif change < -10:
                emoji = "🧊"
            elif abs(change) < 1:
                emoji = "😴"
            print(f"Day {i+1}: ${prices[i]: .2f} ({'+' if change >= 0 else ''}{change: .2f}) {emoji}")





if __name__ == "__main__":
    main()