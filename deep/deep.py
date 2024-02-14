def main():
    goal = ['42', 'forty-two', 'forty two']   
    input_user = input('What is the answer to the Great Question of Life, the Universe and Everything?: ') 
    
    if contains_goal(goal, input_user):
        print('YES')
    else:
        print('NO')
    

def contains_goal(goal, s):
    c = ' '.join(s.lower().split())
    return any(x in c for x in goal)


if __name__ == '__main__':
    main()