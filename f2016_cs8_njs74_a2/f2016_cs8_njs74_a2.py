#http://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
while True:
    try:
        file_name = str(input('Enter the file name'))
    except inproperfilename:
        print('Sorry, this file name is not acceptable')



