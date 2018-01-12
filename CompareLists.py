list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']


def comparelist(list_one, list_two):
    if(cmp(list_one, list_two) == 0):
        print "The lists are the same"
    else:
        print "The lists are not the same"
    



comparelist(list_one, list_two)