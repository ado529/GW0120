import requests


def talk_api(message):
    # @param {type:"string",title:"キー入力"}
    apikey = ""
    talk_url = "https://api.a3rt.recruit-tech.co.jp/talk/v1/smalltalk"
    payload = {"apikey": apikey, "query": message}
    response = requests.post(talk_url, data=payload)
    try:
        return response.json()["results"][0]["reply"]
    except:
        print(response.json())
        return "ごめんなさい。もう一度教えて下さい。"


def main():
    while(True):
        print("自分：", end="")
        message = input()
        print("BOT：" + talk_api(message))


if __name__ == "__main__":
    main()
