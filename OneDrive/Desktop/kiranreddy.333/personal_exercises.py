#finding avg. of variable numbers##

# def avg_of(*args):
#     sum=0
#     for x in args:
#         sum+=x
#     print(sum) 
#     average=sum/2
#     print(f"avg. of those numbers is {average}")

# # avg_of(100,200,300)

##################################################################################
       
## finding maximum of defined numbers##

# def max_no(*numbers):
#     max_no=0
#     for x in numbers:
#         if x>max_no:
#             max_no=x
#     print(f"maxium number in the abpve list is {max_no}")    
# max_no(180,888,90,10,466)

######################################################################################

## finding palendrome series ##

# word=input("ener the word to know whether it is a palendrome ornot : \n ")
# word_len=len(word)
# word_len_for_for_loop=word_len-1

# palendrome=True
# for x in range(word_len):                             ## NOTE: here it would be better if we use word_len/2 , 
#     if word[x]!=word[word_len_for_for_loop-x]:        ##the programme would be more appropriate, 
#         palendrome=False                              ## but the answer would be same in both the cases
# if palendrome==True:
#     print("entered word has a palendrome series")
# else:
#     print("entered word has no palendrome series")    
            
          ########## ### using functions #####    
             
def palendrome_check_for(*words):
    words_list=words      #(ab,bcd,efgh,mju)
    list_len=len(words_list)     #4

    for x in range(list_len):
        word=words_list[x]
        palendrome=True
        for y in range(0,len(word)//2):
            if word[y]!=word[len(word)-1-y]:
                palendrome=False
                
        if palendrome==True:
            print(f"{word} is a palendrome sequence")
        else:
            print(f"{word} is not a palendrome sequence")

palendrome_check_for("kirik","karak","kuri","raman")            
                 