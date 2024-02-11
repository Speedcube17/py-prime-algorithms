def check_file_primes_legacy(file_to_check): 
    check_file = file_to_check

    checked = open("100_mil_checked.txt", "r")
    file = open(check_file, "r")

    checked_lines = checked.readlines()
    file_lines = file.readlines()


    check = 0

    for linenum in range(len(file_lines)-2): 
        if file_lines[linenum].split()[4].replace(",","") == "True": 
            if linenum+1 == int(checked_lines[check]): 
                check += 1
            else:
                print("Error in line "+str(linenum+1)+": "+str(linenum+1)+" != "+checked_lines[check])
                quit

    print("All primes in the given source file match the saved primes!")