import datetime

while True:
    birthday = input("Enter your birthday date in fromat YYYY-MM-DD: ")

    try:
        birth = datetime.datetime.strptime(birthday, '%Y-%m-%d')
    except Exception:
        print("Wrong date format!")
        continue


    difference = (datetime.datetime.now() - birth)
    total = difference.total_seconds()
    print("You are %d seconds old." % total)
    break
