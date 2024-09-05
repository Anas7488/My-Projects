#welcome to dictionary
d ={
     1:'one',2:'two',3:'three',4:'four',5:'five'
}

print(d[5])
#method
print(list(d.keys()))
print(d.values())
print(d.items())
update_d = {
    6:'six',7:'seven',8:'eight',9:'nine',10:'ten'

}
d.update(update_d)
print(d[8])