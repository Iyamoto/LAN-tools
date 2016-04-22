import lan

#lan.initLog()
lan1 = lan.LAN()
lan1.load('lan.conf')

for pc in lan1.getPCs():
    #lan.writeLog(str(pc))
    print(pc)
    pc.getAutorun()
    for e in pc.getEnabledEntries():
        if not e.isVerified():
            print(str(e))
    #print(s)

    
