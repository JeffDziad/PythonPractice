import soundexdata

# Format: SSSS-FFFY-YDDD-NN

print("Wisconsin Drivers license calculator v1.0")
print("------------------------------------------\n")

first_name = input("What is your first name?: ")
middle_initial = input("What is your middle initial?: ")
last_name = input("What is your last name?: ")
gives_birth = input("Are you capable of giving birth? (YES/no): ")
if gives_birth.upper() == "YES" or gives_birth == "":
    gives_birth = True
else:
    gives_birth = False
birth_day = input("What is your birth DAY?: ")
birth_month = input("What is your birth MONTH?: ")
birth_year = input("What is your birth YEAR?: ")


def strip(s):
    rm = False
    output = ""
    for x in s:
        if not rm:
            rm = True
            continue
        if x != "H" and x != "W":
            output += x
    return output


# Last name soundex conversion
def sdx(s):
    output = s[0]
    valid = strip(s)
    for x in valid:
        skip = False
        if len(output) > 3:
            break
        # Skip conditions
        for j in ["A", "E", "I", "O", "U", "Y"]:
            if j.upper() == x.upper():
                skip = True
        # Find letter code
        candidate = 0
        for key in soundexdata.codes:
            for letter in soundexdata.codes[key]:
                if letter.upper() == x.upper():
                    candidate = key
        # Test candidate
        if len(output) > 1:
            if output[len(output) - 1] == candidate:
                skip = True
        if not skip:
            output = output + str(candidate)
    return output


def ssss():
    return sdx(last_name)


def fff():
    output = 0
    matched = False
    for name in soundexdata.first_common:
        if name.upper() == first_name.upper():
            matched = True
            output += soundexdata.first_common[name]
    if not matched:
        for alpha in soundexdata.first_alpha:
            if alpha.upper() == first_name[0].upper():
                output += soundexdata.first_alpha[alpha]
    for initial in soundexdata.middle_alpha:
        if initial.upper() == middle_initial.upper():
            output += soundexdata.middle_alpha[initial]
    return output


def yy():
    return str(birth_year[len(birth_year) - 2]) + str(birth_year[len(birth_year) - 1])


def ddd():
    output = (int(birth_month) - 1) * 40 + int(birth_day)
    if gives_birth:
        output += 500
    return output


ssss = ssss()
fff = fff()
yy = yy()
ddd = ddd()

print("\n%s-%d%s-%s%d" % (ssss, fff, yy[0], yy[1], ddd))
