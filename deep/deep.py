def main():
    goal = ['42', 'forty-two', 'forty two']    
    
    if contains_goal(goal, 'Hello, forrty   TwooooO World!'):
        print('YES')
    else:
        print('NO')
    

def contains_goal(goal, s):
    c = ' '.join(s.lower().split())
    return any(x in c for x in goal)


if __name__ == '__main__':
    main()