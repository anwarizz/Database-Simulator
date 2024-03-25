def writeBin(value): 
    fun = ""
    for i in value:
        fun = fun + bin(ord(i)) + " "
    fun += " "
    return fun 






def readBin(value):
    final = ''
    shilter = ''
    for i in range(0, len(value)):

        if value[i] == ' ' or value[i] == 'z':
            altValue = ''
            for x in shilter:
                if 'b' in x or ' ' in x:
                    continue
                altValue += x
            altFinal = 0
            for x in range(0, len(altValue)):
                altFinal += 2**x * int(altValue[-(x + 1)])
            final += chr(altFinal)
            shilter = ''

        shilter += value[i]
    return final  


def readBin_newVersion_valid(value):
    final = ''
    shilter = ''
    final_filter = ''
    for i in range(0, len(value)):

        if value[i] == ' ' or value[i] == 'z':
            altValue = ''
            for x in shilter:
                if 'b' in x or ' ' in x:
                    continue
                altValue += x
            altFinal = 0
            for x in range(0, len(altValue)):
                altFinal += 2**x * int(altValue[-(x + 1)])
            final += chr(altFinal)
            shilter = ''

        shilter += value[i]
    
    for i in range(0, (len(final) - 1)):
        final_filter += final[i]

    return final_filter







# input [x]
def room_filter_one(from_input_user):
    final = ""
    if "]" in from_input_user[-1]:
        for i in range(0, len(from_input_user)):
            if "[" in from_input_user[i]:
                i += 1
                break
        for altI in range(i, len(from_input_user)):
            if "]" in from_input_user[altI]: break
            final += from_input_user[altI]
    else:
        print("kesalahan penulisan terjadi\n")
        return ""
    
    return final

# input = add [x,x,x]
def room_filter_coma(from_input_user):
    final = []
    shilter = ""
    if "]" in from_input_user[-1]:
        for i in range(0, len(from_input_user)):
            if from_input_user[i] == "[":
                i += 1
                break
        for o in range(i, len(from_input_user) - 1):

            if from_input_user[o] == ",":
                if shilter[0] == " ":
                    fl_shilter = ""
                    for altI in range(1, len(shilter)):
                        fl_shilter += shilter[altI]
                    final.append(fl_shilter)
                    shilter = ""
                    continue
                else:
                    final.append(shilter)
                    shilter = ""
                    continue
            shilter += from_input_user[o]

        if shilter[0] == " ":
            fl_shilter = ""
            for altI in range(1, len(shilter)):
                fl_shilter += shilter[altI]
            final.append(fl_shilter)  
        else:
            final.append(shilter)
    else:
        print("kesalahan penulisan terjadi\n")
        return ""
    # mengembalikan list array
    return final






def checking_error_if_int_has_string(f):
    for i in range(0, len(f)):
        if f[i] == "0" or f[i] == "1" or f[i] == "2" or f[i] == "3" or f[i] == "4" or f[i] == "5" or f[i] == "6" or f[i] == "7" or f[i] == "8" or f[i] == "9":
            '...'
        else:
            return "no"
            
    return "yes"