import json
import math

def load_journal():                #loading data from json file and the output is returned.
    file=open('journal.json','r')
    content=file.read()
    global json_data
    json_data=json.loads(content)
    return json_data

    

def compute_phi(events):                #function to find correlation of an event.
    load_journal()                 #calling the previous function.
    # event=input("enter the event:")
    event= events
    n11,n00,n10,n01=0,0,0,0
    n1plus,n0plus,nplus1,nplus0=0,0,0,0
    
    
    for daily_record in json_data:                       #incrementing each values based on condition.
        if event in daily_record['events'] and daily_record['squirrel']==True:
            n11+=1
            n1plus += 1
            nplus1 += 1
        elif event not in daily_record['events'] and daily_record['squirrel']==False:
            n00+=1
            n0plus += 1
            nplus0 += 1
        elif event in daily_record['events'] and daily_record['squirrel']==False:
            n10+=1
            n1plus += 1
            nplus0 += 1
        elif event not in daily_record['events'] and daily_record['squirrel']==True:
            n01+=1
            n0plus += 1
            nplus1 += 1
        else:
            pass

    correlation = (n11 * n00 - n10 * n01) / math.sqrt(n1plus * n0plus * nplus1 *nplus0)
    return correlation

# compute_phi()


def compute_correlation():    #function to calculate the correlation of each event,removing duplicate events and creating a dictionary with it.The keys of the dictionary will be each event and the value will be its correlation.
    load_journal()
    event_list=[]
    for daily_record in json_data:
        for each_event in daily_record['events']:
            event_list.append(each_event)
    s=set(event_list)
    unique_list=list(s)
    # print(sorted_list)

    global correlation_dictionary
    correlation_dictionary={}
    for event in unique_list:
        correlation_value=compute_phi(event)
        key=event
        value=correlation_value
        correlation_dictionary[key]=value
    
compute_correlation()


def diagnose():                        #function to find the min and max correlation values and the corresponding key from the dictionary.
    compute_correlation()
    correlation_values=correlation_dictionary.values()
    correlation_values_list=[]
    for value in correlation_values:
        correlation_values_list.append(value)
    correlation_values_list.sort()
    # print("Negatively correlated: ", correlation_values_list[0])
    # print("Positively correlated: ", correlation_values_list[-1])

    negatively_correlated=correlation_values_list[0]
    positively_correlated=correlation_values_list[-1]
    rev={value:key for key,value in correlation_dictionary.items()}

    print(rev[negatively_correlated] ,'------>', negatively_correlated,"(negatively correlated)")
    print(rev[positively_correlated] ,'------->', positively_correlated,"(positively correlated")

   

diagnose()
