#author:Vitor Fernandes Gonçalves da cruz
import random
NUMBER_OF_ATTEMPTS = 3
class HangmanGame:
 
    
    def get_words(self):
       
        with open("Words.txt","r",encoding="utf-8") as w:
            total_lines = sum(1 for line in w)
            w.seek(0)
            random_line = random.randint(0,total_lines-1)
            word = w.readlines()
            word = word[random_line].lower()
            word  =word.replace('\n','')
        w.close()
      
            
        return word 
    
    def showResult(self,index,len_word,input_user,output_word ):
        
        if(len(output_word)==0):

            for l in range(len_word):
                output_word.append(' _ ')
            output_word[index] = input_user
        else:
            output_word[index] = input_user

        return output_word
    
    def if_win(self,word):
        for i in  word:
            if(i != ''):return False 

        return True

    def output_word(self,word,input_user,output_word):

        index = word.index(input_user)
        len_word = len(word)
        word[index] = ''
        output_word = self.showResult(index,len_word,input_user,output_word)

        return output_word

    def message (self,win,word):
        if(win==True):
            print()
            print('You Won !!!')   
        else:
            print()
            print('You losed ):') 
            print(f'Word:{word}')  
            print()
    
    def show_output_word(self,output_word):
        for letter in output_word :
            print(letter,end='')

    def show_used_letters(self,words_useds):
          for letter_used in words_useds :
            print(letter_used + ',',end='')

    def play(self):
        play = True
        win = False
        output_word = []
        words_useds = []
        number_of_attempts = 0;
        word= self.get_words()
        word_list = list(word)
       
     
        while(number_of_attempts<NUMBER_OF_ATTEMPTS and not(win)):

            if(not(self.if_win(word_list))):
                print()
                input_user =  input('Enter with a letter:').lower()
                if(input_user in word_list):

                    for i in range(word_list.count(input_user)):
                        self.output_word(word_list,input_user,output_word)
                        
                    words_useds.append(input_user)      
                    self.show_output_word(output_word)

                else:
                    if(input_user not in words_useds):

                        print()
                        print(f'There is not  {input_user}'  )
                        number_of_attempts+=1
                        words_useds.append(input_user)  
                        print()
                        print('---------------')
                        print('Used letters :')
                        self.show_used_letters(words_useds)
                        print()
                        print('---------------')
                    else:
                        print()
                        print('Letter Used!!')
                        print('---------------')
                        print('Letters Used:')
                        self.show_used_letters(words_useds)
                        print()
                        print('---------------')
            else:
                win = True

        self.message(win,word)
        print()
        print('Would you like play again?')
        print('Y / N')
        input_user_choice =  input().lower()
        if(input_user_choice=='y'):

            self.play()

        else:win = True

      
forca = HangmanGame()
forca.play()

