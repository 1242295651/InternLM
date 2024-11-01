from openai import OpenAI
import json
from config import api_key

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

query = "strawberry”中有几个字母“r”"
prompt = f"""
# 要求
接下来你需要对下面的问题进行回答，请对问题一步一步进行思考，并且输出思维过程中的每一个步骤。
# 问题是
{query}
"""
res = internlm_gen(prompt, client)
print(res)