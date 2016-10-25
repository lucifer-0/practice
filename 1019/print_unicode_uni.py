import sys
import unicodedata


def print_unicode_table(word):
    filename = "unicode-table.txt"
    with open(filename, "a", encoding="utf-8") as file:
        file.write("decimal   hex   chr  {0:^40}\n".format("name"))
        file.write("-------  -----  ---  {0:-<40}\n".format(""))

    code = ord(" ")
    end = min(0xD800, sys.maxunicode)

    while code < end:
          c = chr(code)
          name = unicodedata.name(c, "*** unkown ***")
          ok = True
          for word in words:
              if word not in name.lower():
                  ok = False
                  break
          if ok:
              with open(filename, "a", encoding="utf-8") as file:
                  file.write("{0:7}   {0:5X}   {0:^3c}  {1}\n".format(code, name.title()))
          code += 1
    print("wrote results to", filename)


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print ("usage:{0}[string1 [string2 [...stringN]]]".format(sys.argv[0]))
        words = None
    else:
        for word in sys.argv[1:]:
            words.append(word.lower())

if word is not None:
    print_unicode_table(words)
    
