import click 
'''Click use kora hoy python code e flag akare argument pass korar jonno. And @click.command() aita kei indicate kore je amar command line interaction
korte hobe'''
@click.command()
@click.option('--number', default=1337,help='Give your lucky number') # there is a default value setup
@click.option('--name',prompt='What is your name? ', help='Your nickname') # there is a prompt. If user miss the flag input
def lucky(number,name): # the parameter must be same as the value of flag. Means parameter should be without dash
   print(f'Hello {name} your lucky number is: {number}')
#     click.echo(f'Hello {name} your lucky number is: {number}')

if __name__ == '__main__': # this python idiom is must in this case to call the special function
    lucky()


'''amra ekhane onnekvabe flag er satey interaction korte pari. but main duita process hocche bydefult value . and Arekta hocche prompt value. 
prompt value and default value same case e use hoy. means user jodi flag diye value dite bhule jay tahole Prompt, tar nijer prompt open kore input niye nibe
and Default tar moddhe store hoya default value use korbe. So ekhane both case ei user er error ke mitiate kora hy. Aro important akta notice hocche
lucky je function tah create hoise aita akta special function . jar input amader click method theke asbe. Tai ai function ke pyhton directly call korbe nh
ai function er call ke invoke kora lagve. tai ekhane python idiom use korte hobe function tah ke explicitly call korar jonno. Aro akta important notice 
hocche ekhane --help support korbe. and manual instruction show korbe. Karon amara click option e help set korsilam. So user chaile aitar manual open
korte parbe --help use kore. So evabei python er script ready kora hoy flag theke input neowar jonno. OVIOUSLY aro onnek process asey flag input neowar
but amar kasey click module use kora tah easy'''