def Triangle_Maker():
    length = int(input("Please Enter The Base Length Of Triangle: "))
    length = length+1 if length%2 == 0 else length
    triangle = ["*"*i for i in range(1,length,2)]
    a = triangle.reverse() if input("Need Reversed Triangle: ").lower().startswith("y") else triangle
    def center_text(text='', length=0):
        ftl = length - len(text)
        return (" "*(int((ftl)/2)) + text if ftl % 2 == 0 else " "*(int((ftl)/2)) + text)
    return '\n'.join([center_text(i, length) for i in triangle])
print(Triangle_Maker())
