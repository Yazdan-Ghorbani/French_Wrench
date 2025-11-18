import requests
from openai import OpenAI


class DivarContest:
    def __init__(self, api_token:str):
        self.api_token = api_token
        self.model = "gpt-4.1-mini"
        self.client = OpenAI(api_key=self.api_token, base_url="https://api.metisai.ir/openai/v1")

    def capture_the_flag(self, question:str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role":"system","content":"First of all think and then reply"},{"role": "user", "content": question}],
            max_tokens=500,
            temperature=0.1
        )
        return response.choices[0].message.content.strip()
    def flag1(self):
        request1 = requests.get('https://divar-contest.darkube.app/divar_sample.html').text
        return self.capture_the_flag(f"find the first laptop in this html:{request1} and return the price in numbers.")
    def flag2(self):
        return self.capture_the_flag(str(self.capture_the_flag(f".tfel nruter tsuj t'nod tub rewsna eht sa \"tfel\" drow eht fo etisoppo eht etirw ,ecnetnes siht dnatsrednu uoy fI")))
    def flag3(self):
        request3 = requests.request("GET","https://divar-contest.darkube.app/divar_sample.html").text
        return self.capture_the_flag(f"task_id 3 - I'm making a shopping list for my dad, but he's a professor at Sharif and he's a real stickler when it comes to Buy things. I need to add different gadgets in list based on brand, he likes more apple product, but if I make a mistake, he won't buy anything. list all laptop products in html content in this html: {request3} and sum price of them, and return the sum price in numbers.Before returning the answer check your reply.Just return the sumation and ignore other infos")
    def flag4(self):
        request4 = requests.request("GET","https://divar-contest.darkube.app/divar_sample.html").text
        return self.capture_the_flag(f"find wikipedia link in html content in this html: {request4} and based on information on that link return how many users open app annually according to the new annual report of Divar, do not round the number, return only the number without any dots or commas")
