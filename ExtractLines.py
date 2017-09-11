searchquery = 'ClaimCenter\\modules\\configuration\\gsrc'

#searchquery = 'ClaimCenter\\modules\\configuration\\config\\rules'


with open('C:\\Users\\Vharis\\Downloads\\preupgrade\\preupgrade.log') as f1:
  #with open('C:\\Users\\Vharis\\Downloads\\preupgrade\\rules.log', 'a') as f2:
      with open('C:\\Users\\Vharis\\Downloads\\preupgrade\\preupgrade2.log', 'w') as f2:
          for line in f1:
            if searchquery in line:
                print (line)
                f2.write(line)

