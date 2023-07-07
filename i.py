from midjourney_api import TNL   
NL_API_KEY = 'your_api_key_here'

tnl = TNL("e5ca66d9-d7b0-4371-9b7c-b84f6c0aa951")



prompt = 'love is independent of money '

response = tnl.imagine(prompt)



print(response)