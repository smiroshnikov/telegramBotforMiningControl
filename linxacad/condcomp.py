# tupo case/switch

def name_t(name):
    if len(name) >= 5:
        print("not too short ")
    elif len(name) == 4:
        print("average")
    elif len(name) == 3:
        print("OK")
    elif 1 < len(name) <= 2:
        print("tiny")
    else:
        print("this is not a name ")


name_t("morbnusborbus")
name_t("1")
name_t("1234")
name_t("123")
name_t("11")
name_t("")

print(not 1)
print(1 is 1)
print({} is {})
print([] is {})

print(() is ())  # immutable

print(True and False)
print(False and True)
print(False or False)
print(True or False)

print(1 and 1 and 3 and '1' and 0)
