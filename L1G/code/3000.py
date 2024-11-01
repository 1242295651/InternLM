from openai import OpenAI
import json
from config import api_key,internlm_gen,client

query = "strawberry”中有几个字母“r”"
prompt = f"""
# 要求
接下来你需要对下面的问题进行回答，请对问题一步一步进行思考，并且输出思维过程中的每一个步骤。
最后的输出结果请用<answer></answer>标签包裹。
# 技巧
你可以对于问题中的每个单词都分别去鉴定，写出每个单词的情况，并在结果处累加
# 问题是
{query}
"""
res = internlm_gen(prompt, client)
print(res)