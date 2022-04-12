import requests
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

threads = 5 #number of accounts you want
base_username = 'YOUR USERNAME HEREEEE'

class session:
    def __init__(self, username, gameid):
        self.username = username
        self.pin = gameid
        self.driver = webdriver.Chrome()
    def get_answers(self):
        client = requests.Session()
        headers = { #no touch
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,ja;q=0.8',
            'authorization': 'Bearer eyJraWQiOiJTZmRDOUNBOHlyT2dhOEVMUWxEODFyWWV2d1NicEE5cWxTb0siLCJ0eXAiOiJhY2Nlc3Mrand0IiwiYWxnIjoiUlMyNTYifQ.eyJhdWQiOiJodHRwczpcL1wva2Fob290Lml0XC9yZXN0Iiwic3ViIjoiYmQ5MGQxYzItN2E2YS00OWE2LWEzMDItM2UwYTBiMTE0MGRlIiwiaXNzIjoiaHR0cHM6XC9cL2thaG9vdC5pdFwvcmVzdCIsImV4cCI6MTY1MDI1NTk4NCwiaWF0IjoxNjQ5Njk0NDY2LCJqdGkiOiJlZDA0ZTM3OC1iYzlmLTNmNzktODY1NC0xOTI0YzNjNjM3MDciLCJzaWQiOiIxYThhZDI2Yi01ODMzLTQ1NGUtYTM5ZC1jMWJlOWU0NGQ2YTUifQ.3rj-9V3p8JTRT33FN8OHjBxKxPfJ4_2dDYLiaZ9PueSithn8FyHLLt_Ceqcwy5dyeaj-adPEXpjYKMsQ7ZqIsbl2G36gSRFB0lTQufWEj7491tGoDZ-CGTjm_QmMoNNU29y4xXNYtcHJC8jWHQ_nvzXj4R_kNmEtGMmmEqAFKXIu6x_Z087-DDBnOUETqZBtZiNvwq7UUCbkCQm8mOBAIBmBaUKJs6gyG4v57E4Cr82BSZzcnyMCZ3r03L22s9nWoUxRZXKph5hUg7PdDs1pHwiRas-Gqn5Sm3IlJWqJ6TcIsDubOXxJBbkZGg8xdKAmnjcvmeYzOhDg6NBtnsqwIw',
            'content-type': 'application/json',
            'cookie': '_hjid=322a515b-70f6-4107-9d0b-68e044e28e4a; _hjSessionUser_554762=eyJpZCI6ImRlMzM1NGIwLTA4N2ItNTNmYi1iZGJiLTgxNzY2OTExNzdlNCIsImNyZWF0ZWQiOjE2NDk2OTQzODUyMDksImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_554762=eyJpZCI6IjI0ZWM5ODRlLTFlZDgtNDcxNC1iYWZkLWQ0ODhlMmIyY2JkZSIsImNyZWF0ZWQiOjE2NDk2OTQzODUyOTgsImluU2FtcGxlIjpmYWxzZX0=; _hjIncludedInSessionSample=0; _hjAbsoluteSessionInProgress=0; generated_uuid=195d0dcd-0ea5-4121-b975-e1cd922ee356; amplitude_id_bbe76494b586b96ca8380f0a81505aa2kahoot.it=eyJkZXZpY2VJZCI6IjM5YTQ1MGI3LTA0N2QtNDAxNC1iZTc4LWEwZmFiOWQ5ODI3OVIiLCJ1c2VySWQiOiJiZDkwZDFjMi03YTZhLTQ5YTYtYTMwMi0zZTBhMGIxMTQwZGUiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE2NDk2OTQ0NDU5OTksImxhc3RFdmVudFRpbWUiOjE2NDk2OTQ1MjY2ODEsImV2ZW50SWQiOjUyLCJpZGVudGlmeUlkIjo5Mywic2VxdWVuY2VOdW1iZXIiOjE0NX0=',
            'referer': 'https://create.kahoot.it/details/fe1ddcdd-4b82-49ba-9665-b96fdc349fdc',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': 'Windows',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
            'x-kahoot-tracking': 'platform/Web'
        }

        response = client.get(url='https://create.kahoot.it/rest/kahoots/YOUR GAME UUAID', headers=headers) #put game UUAID HERE
        questions = response.json()['questions']
        answers = []

        #for item in questions: print(item)  #printresponsedata debug
        for key in questions:
            choices = key['choices']
            for index, answer in enumerate(choices):
                if answer['correct']:
                    answers.append([key['question'], answer['answer'], index])

        #for item in answers: print(item) debug
        self.answers = answers
        return self.answers

def bot(i):
    global base_username
    client = session(f'{base_username}{i}', 'KAHOOT GAME PIN HERE')
    answers = client.get_answers()
    client.driver.get(f'https://kahoot.it?pin={client.pin}&refer_method=link')
    client.driver.implicitly_wait(1)
    client.driver.find_element(By.XPATH, '//*[@id="nickname"]').send_keys(client.username)
    client.driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[3]/div[2]/main/div/form/button').click()

    for questionID in range(len(answers)):
        waiting = True
        while waiting:
            try:
                client.driver.find_element(By.XPATH, f'//*[@id="root"]/div[1]/main/div[2]/div/div/button[{answers[questionID][2]+1}]').click()
                waiting = False
            except NoSuchElementException: pass

if __name__ == '__main__': #main :)
    for i in range(threads):
        Thread(target=lambda: bot(str(i))).start()
