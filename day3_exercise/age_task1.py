
dave = int (input('Enter daves age: '))
henry = int (input('Enter henrys age: '))
roger = int (input('Enter roger age: '))

if dave < henry and dave < roger:
    print('dave is younger')
elif henry < dave and henry < roger:
    print('henry is younger')
elif roger < dave and roger < henry:
    print('roger is younger')
else:
    print('All of same age')
