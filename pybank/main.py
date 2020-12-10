import os
import csv
csv_file = os.path.join("budget_data.csv")  
with open (csv_file) as csv_file:
    csvreader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csvreader)
    counter = 0
    list1 = [] 
   
    for row in csvreader:
        counter = counter + 1
        list1.append(int(row[1]))

    link = int(len(list1))
    total_money = sum(list1)

    list2 = []
    max_increase = 0
    max_decrease = 0
    
    for M in range(1, link):
        difference = (int(list1[M])- (int(list1[M-1])))
        list2.append(difference)       

        if difference > max_increase: 
            max_increase = difference
            
    for M in range(1, link):
        difference_loss = (int(list1[M])- (int(list1[M-1])))
        list2.append(difference_loss)       

        if difference_loss < max_decrease:
            max_decrease = difference_loss

    



#print(counter)
sum_of_change = sum(list2)
number_of_changes = len(list2)
average_change = round((sum_of_change/number_of_changes), 2)


print(f"total months {link}")
print (f"total ${total_money}" )
print(f"average change ${average_change}")
print(f"gratest profit ${max_increase}") 
print(f"gratest loss $ {max_decrease}")

output_path = os.path.join("results","pybank_results.csv")
with open(output_path, "w", newline= '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter =',')
   
  
    csvwriter.writerow(["total months", link])
    csvwriter.writerow(["total", total_money])
    csvwriter.writerow(["average change", average_change])
    csvwriter.writerow(["gratest profit", max_increase]) 
    csvwriter.writerow(["gratest loss", max_decrease])
  