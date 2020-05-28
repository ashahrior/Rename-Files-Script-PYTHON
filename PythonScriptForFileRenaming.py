import os
import string

def serial_renamer(dirr):
    os.chdir(dirr)

    x = 1
    s = ''

    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        print('Renaming original file name %s with extension %s'%(f_name, f_ext))
        if x==1:
            s = input('Enter new name with {} serialization placeholders')
        n_name = s.format(x)
        new_name = '{}{}'.format(n_name,f_ext)
        os.rename(f,new_name)
        x += 1

def mono_renamer(dirr):
    for f in os.listdir(dirr):
        f_name, f_ext = os.path.splitext(f)
        '''
        # listed all jpg album art files and deleted them because
        # you can just use if else condition to ignore the jpgs and only work with .mp3 files
        if f.endswith('.jpg'):
        os.remove(f)
        '''
        print('Renaming original file name %s with extension %s'%(f_name, f_ext))
        '''
        modifying the file names in accordance with my preference. I am removing all non alpha chars
        and only separating the words with '-'
        '''
        n_name = ''
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

if __name__ == "__main__":
    dirr = input('Input source directory path>> ')
    if input('1 - Serial renaming\n2 - Format-wise renaming\n>> ') == '1':
        serial_renamer(dirr)
    else: 
        mono_renamer(dirr)