def invitation(mother,father,child,teacher,event):
    #here we are going to use multi-line strings: f''' text here '''
    letter = f'''
    Dear {mother} and {father},
    {teacher} and I would love to see you both as well as {child} at our {event} tomorrow evening.

    best regards,
    Principle Hacker D.
'''
    print(letter)

invitation(mother='Ayesha',father='Ibrahim',child='Hasan',teacher='Delwar',event='Annual Prize Giving Ceremony')

# here we can learn about multi-line strings and named parameter. Here we can specify the parameter we need to pass in the called function. So there will
#be a less chance of error