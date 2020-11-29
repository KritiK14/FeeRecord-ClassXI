print("FEE RECORD FOR VISHWA BHARATI PUBLIC SCHOOL, NOIDA")
def main():
       fp={"kartik":("class-8D, fees payed, contact no.:9212004372"),"komal":("classs 11A, fees payed, contact no.:9512456737"),"sejal":("class-9C, fees payed, contact no.:8932126734")
       ,"hardik":("class-10d, fees payed, contact no.:8790325678"),"falguni":("classs-4F, fees payed ,contact no.:7812223456"),"yukti":("class-6D, fees payed, contact no.:9054672314"),
       "tanvi":("class-2E, fees payed, contact no.:7832451278"),"karmanya":("class-12D, fees payed, contact no.:8923676767")}
       fd={"lakshay":("class-9E, fees due, contact no.:6352489234"),"shruti":("class-5F, fees due, contact no.:9834678943"),"sanvi":("class-6C, fees due, contact no.:9853895433"),
       "hiten":("class-10D, fees due,contact no.:6734890921"),"kamakshi":("class-11E, fees due, cont no.:78325661289"),"john":("class-1A, fees due, contact no.:8754312790"),
       "laavanay":("class-12A, fees due, contact no.:6743678936"),"ujjawal":("class-6F, fees due, contact no.:9845127865")} 
       print()
       print("M A I N   M E N U")
       print("-------------------------------------------")
       print("For searching student details, Press 1. ")
       print("To add a name to the list, Press 2. ")
       print("To delete a name from a list, Press 3. ")
       print("To display the full student records, Press 4. ")
       print("To update the status of fee for a student, Press 5. ")
       print("To quit, press 6. ")
       print("-------------------------------------------")
       l=int(input("Enter your option: "))
       print()
       if (l==4):
              m=input("Enter the category: Fees due or Fees payed. ")
              if m=="fees payed":
                     print(fp)
              elif m=="fees due":
                     print(fd)
              else:
                     print("incorrect input")
       if (l==1):
              n=input("Enter the student name: ").lower()
              if n in fd:
                     print(fd[n])
              elif n in fp:
                     print(fp[n])       
              else:
                     print("We dont't have records for the particular student yet.")
       if (l==2):
              q=input("For adding a name to the fees due list, press A. For adding a name to the fees payed list, press B.").upper()
              if q=="A":
                     r=input("Enter the name of student")
                     p=input("Enter details in order of class, fees payed, contact no. ")
                     fp[r]=p
                     print("Done.")
                     print(fp)
              elif q=="B":
                     v=input("Enter the name of the student")
                     w=input("Enter details in order of class, fees due, contact no. ")
                     fd[v]=w
                     print("Done.")
                     print(fd)
              else:
                     print("Incorrect input.")
       if (l==3):
              x=input("From which list the name is to be deleted: A. Fee payed OR B. Fee due. ").upper()
              if (x=="A"):
                     o=input("Enter a name to be deleted. ").lower()
                     if o in fp:
                            del fp[o]
                     else:
                            print("Name not found.")
              if (x=="B"):
                     s=input("Enter a name to be deleted. ").lower()
                     if s in fd:
                            del fd[s]
                     else:
                            print("Name not found.")
       if (l==5):
              k=input("Enter the name of the student whose fee status is to be updated: ").lower()
              j=input("Enter student details. ")
              c=input("Press A, If status to be changed from due to payed. OR Press B, If status to be changed from payed to due.").upper()
              if (c=="A"):
                     del fd[k]
                     fp[k]=j
                     print(fp)
              elif (c=="B"):
                     del fp[k]
                     fd[k]=j
                     print(fd)
              else:
                     print("Invalid input")
       if (l==6):
              print("YOU HAVE EXITED FROM THE FEE RECORDS.")
              exit()
       if (l>6):
              print("Incorrect Input") #gives error
       restart=input("Do you want to restart the code again? ").lower()
       if (restart=="yes"):
              print()
              print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-")
              main()
       else:
              exit()
main()