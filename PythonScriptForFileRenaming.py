import os
import string

os.chdir('H:\\SONGS')

for f in os.listdir():
    #print(os.path.splitext(f))

    '''
    # listed all jpg album art files and deleted them because
    # you can just use if else condition to ignore the jpgs and only work with .mp3 files
    if f.endswith('.jpg'):
       os.remove(f)
    '''

    # separated the file names and their extensions
    f_name, f_ext = os.path.splitext(f)
    #print(f_name,f_ext)

    '''
    modifying the file names in accordance with my preference. I am removing all non alpha chars
    and only separating the words with '-'
    '''
    n_name = ''
    #print(f_name)

    '''
    I don't want to have any digits. I'd rather want the list of songs to be in alphabetic order.
    So I didn't put any condition to handle alphanumerics. And my songs folder was too much of
    a convoluted mess. So handling all those conditions would've been a real pain.
    '''
    for i in f_name:
        if i in string.ascii_letters:
            n_name += i
        else: n_name += ' '
        
    n_name = n_name.strip(' ')  # stripping away all leading and trailing spaces
    n_name = n_name.replace(' ','-') # replacing spaces with '-'

    #print(n_name)

    '''
    there were some files containing multiple consecutive unnecessary duplicate '-'
    so i removed those duplicates here
    '''

    title = n_name[0]
    for i in range(1,len(n_name)):
        if n_name[i]!='-':
            title += n_name[i]
        else:
            if n_name[i] == n_name[i+1]:
                pass
            else: title += n_name[i]
    #print(title)
    new_name = '{}{}'.format(title,f_ext)
    print(new_name)
    os.rename(f,new_name)

