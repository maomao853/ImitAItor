import random
import cohere

co = cohere.Client('zk2Nb4mb0t0DfC1IvFIjudfrEm16tFUSdUJoKR6y')

'''def getNumPlayers():
  global num_players

  flag = False
  
  while not flag:    
    try:
      num_players = int(input("How many people are playing?: "))

      if num_players > 0:
        flag = True
      else:
        print("Please enter a player count greater than zero.\n")
    
    except ValueError:
      print("Please enter a number.\n")'''


def getPrompt():
    global main_prompt
    prompts_file = open("prompts.txt")
    prompts = prompts_file.readlines()
    prompts_file.close()

    pos = random.randint(0, len(prompts) - 1)

    main_prompt = prompts[pos].strip()
    return (main_prompt)


def getSentences(main_prompt):
    '''global co, num_players, main_prompt, sentences, ai_text
  
  sentences = []
  
  for i in range(num_players):
    sentences.append(input("Player " + str(i+1) + ", please enter your sentence: ").strip(" ,.!?"))'''

    response = co.generate(
        prompt=main_prompt,
        model='xlarge',
        max_tokens=100,
        temperature=1,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=['.', '?', '!'],
        return_likelihoods='NONE',
    )

    ai_text = (response.generations[0].text).strip(" ,.!?")
    return (ai_text)


'''def displaySentences():
  global num_players, main_prompt, sentences

  random.shuffle(sentences)
  
  for j in range(num_players + 1):
    print('Sentence {}: {} {}'.format(str(j + 1), main_prompt, sentences[j]))

  print()'''
'''def guessAI():
  global num_players, ai_text, sentences
  
  flag = False
  
  while not flag:
    try:
      guess = int(input("Which sentence did the AI write?: "))
  
      if 1 <= guess <= num_players + 1:
        if sentences[guess - 1] == ai_text:
          print("Correct!")
          flag = True
        else:
          print("Incorrect!")
  
      else:
        print("Please enter a number from 1 - " + str(num_players + 1))

    except ValueError:
      print("Please enter a number from 1 - " + str(num_players + 1))  '''
'''def main():
  __cohereSetup__()
  getNumPlayers()
  getPrompt()
  getSentences()
  displaySentences()
  guessAI()'''
