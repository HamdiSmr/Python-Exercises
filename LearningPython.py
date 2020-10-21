
#exercise 1
my_list = []
def paper_doll(text):
    my_list = [] # for resetting the list
    for characters in text:
        my_list.append(characters * 3)
    return "".join(my_list)


def has_33(nums):
    #has_33([1, 3, 3])
    for number in range(len(nums)):
        if(number == len(nums)-1):
            return False
        
        elif(nums[number]+nums[number+1] == 6 and nums[number] % 3 == 0 and nums[number+1] % 3 == 0):
            return True



def almost_there(n):
    if(90<=n<=110 or 190<= n <= 210):
        return True
    else:
        return False


my_list = []
last_list = []
def master_yoda(text):
    last_list = []
    my_list = text.split()
    my_list.reverse()
    for x in my_list:
        last_list.append(x)
    return " ".join(last_list)


def old_macdonald(name):
    #old_macdonald('macdonald')
    return name[0].capitalize()+ name[1:3] + name[3].capitalize() + name[4::]



def makes_twenty(n1,n2):
    if(n1+n2 == 20 or n1 == 20 or n2 == 20):
        return True
    else:
        return False


my_list = []
def animal_crackers(text):
    #text = animal architecture
    my_list = text.split()
    if(my_list[0][0] == my_list[1][0]):
        return True
    else:
        return False


def lesser_of_two_evens(a,b):
    if(a % 2 == 0 and b % 2 == 0):
        if(a < b):
            return a
        elif(a > b):
            return b
    elif(a % 2 != 0 or b % 2 != 0):
        if(a < b):
            return b
        elif(a > b):
            return a

