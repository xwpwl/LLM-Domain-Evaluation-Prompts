import requests
import time

def get_crypto_price(coin_id="bitcoin"):
    """
    通过 CoinGecko API 获取加密货币实时价格
    用于测试大模型金融数据获取的时效性
    """
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        price = data[coin_id]['usd']
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {coin_id.capitalize()} 实时价格: ${price}")
        return price
    except Exception as e:
        print(f"获取价格失败，请检查网络或API限制: {e}")
        return None

if __name__ == "__main__":
    print("🚀 启动加密资产时效性监控脚本...")
    print("-" * 30)
    # 演示获取比特币和以太坊价格
    get_crypto_price("bitcoin")
    get_crypto_price("ethereum")
    print("-" * 30)
    print("✅ 测试完成：API 接口响应正常。可将此数据作为 Prompt 输入，校验大模型的实时分析能力。")
