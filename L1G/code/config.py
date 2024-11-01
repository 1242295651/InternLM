from openai import OpenAI

api_key = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI1MDE3NDc4NCIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTcyOTg1OTU5MywiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTg4MDczNjg2ODciLCJ1dWlkIjoiZjQwOGVlZDItMDBlNi00YTdlLTk5NjYtNGU5ZmUyNWY1MjFlIiwiZW1haWwiOiIiLCJleHAiOjE3NDU0MTE1OTN9.IUq1CflIg7q1Ui36EzoBm4R2N0ivIsqqMWCHlIW1jku6muK8vtq5OoOiO-Gkqp6L3CcJ9FUnjWIITrjLHUgHjQ"

def internlm_gen(prompt, client):
    '''
    LLM生成函数
    Param prompt: prompt string
    Param client: OpenAI client 
    '''
    response = client.chat.completions.create(
        model="internlm2.5-latest",
        messages=[
            {"role": "user", "content": prompt},
        ],
        stream=False
    )
    return response.choices[0].message.content

client = OpenAI(
    base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
    api_key=api_key)

