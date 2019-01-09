#python 3.6
import time,pygame

def show_symbol(data):
    "show a symbol from morse code as a sequence of short and long white screen appearenceson pygame screen"
    screen.fill([data[1]*255,data[1]* 255,data[1]*255]) # True * 255 = 255 - white screen, False*255 = black
    pygame.display.flip()
    time.sleep(data[0]*0.2)
    
def morse_msg(message): 
    "codes common message to morse sequence"
    message = message.split()
    morse_code = []
    for word in message: # itterations on list of message words
        for letter in word: # itterations on each letter of each word
            morse_code.append(morse_alphabet[letter]+'   ')
        morse_code.append('    ') # adds a gab between words (common 7 (3+4))
    return ''.join(morse_code) # list of morse sequence to string literal
    
	
morse_alphabet = {'A':'* -','B':'- * * *', # letter : morse sequence
              'C':'- * - *','D':'- * *',
              'E':'*','F':'* * - *',
              'G':'- - *','H':'* * * *',
              'I':'* *','J':'* - - -',
              'K':'- * -','L':'* - * *',
              'M':'- -','N':'- *',
              'O':'- - -','P':'* - - *',
              'Q':'- - * -','R':'* - *',
              'S':'* * *','T':'-',
              'U':'* * -','V':'* * * -',
              'W':'* - -','X':'- * * -',
              'Y':'- * - -','Z':'- - * *',
              '1':'* - - - -','2':'* * - - -',
              '3':'* * * - -','4':'* * * * -',
              '5':'* * * * *','6':'- * * * *',
              '7':'- - * * *','8':'- - - * *',
              '9':'- - - - *','0':'- - - - -'}
			  
symbols = {'-':(3,True),' ':(1,False),'*':(1,True)} # first - time to show, second - show black or white screen
msg = input('message: ')
msg = morse_msg(msg.upper())
length = 0
running = True
len_msg = len(msg) # in order to not compute it on each itteration
print(msg)

pygame.init()
screen = pygame.display.set_mode([740,590]) # screen size
time.sleep(2)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if length < len_msg: #if length of msg becomes less length - black screen established
        show_symbol(symbols[msg[length]])
    length += 1
pygame.quit()
