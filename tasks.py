import sys, os, subprocess, shlex       
from termcolor import colored
from colored import fg, bg, attr
                                                                                                       
# write a simple shell  
                                
result = 0                                                                                             
                        
while 1:                                                                                               
                        
    # get the command           
    line = raw_input('%s>%s'% (fg('13'), attr('reset'))) 
                                                                                                       
                        
    if line != "":              
        lex = shlex.split(line)
        #check for internal commands "exit", "cd", use if/elif/else                                    
        if lex[0] == "exit":
                exit(0)
        elif lex[0] == "view tasks" or lex[0] == "|vt":
            #print colored("Current Tasks: ", "blue")
            print ('%s Current Tasks: %s' % (fg(228),  attr(0)))
        elif lex[0] == "|a":
            note = raw_input('%s Add note: %s' % (fg('51'), attr('reset')))
            splitNote = shlex.split(note)
            # Look at categories file
            # based on given category, add to master list with category noted

        elif lex[0] == "cd":                                                                           
                os.chdir(lex[1]) # end of internal commands                                            
        elif lex [0] == "pwd": 
                print(os.getcwd())
                #print("pwd was typed\n")
        elif lex[0] == "date":  
                bash = os.popen("date")
                print bash.read()                                                                      
        elif lex[0] == "ls":
                bash = os.popen("ls")                                                                  
                print bash.read()                                                                      
                # print (os.listdir(os.getcwd()))                                                      
        else:
                print("%s%sCommand NOT Recognized!%s" % (fg('232'), bg('196'), attr('reset')))

