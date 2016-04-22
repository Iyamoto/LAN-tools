import subprocess
import codecs
import os.path

#how to store autoruns data? sql db? autorun object class
#autoruns class: user, date, path, program...
#use console git
#add some test functions
#what if pc is offline?
#add configs
#add clear cache method

class PC(object):
    #Individual PC class
    
    def __init__(self, IP=''):
        """Creates PC"""
        self.IP = checkIP(IP)

    def getIP(self):
        return self.IP

    def setIP(self, IP):
        self.IP = checkIP(IP)
        return
    
    def __str__(self):
        #What is string representation of PC?
        return self.getIP()

    def getAutorun(self):
        cmd = 'run.cmd '+self.getIP()
        #print(cmd)
        path = 'cache\\'+self.getIP()+'.csv'
        #print(path)
        if os.path.isfile(path) == False:
            try:
                subprocess.call(cmd, shell=True)                
            except:
                print('Cant execute: '+cmd)
                return ''
        lines = file2list(path, 'utf-16-le')
        i=0
        self.Entries = []
        for line in lines:
            if i>0:
                a = Autoruns(line.strip())
                self.Entries.append(a)
            i+=1
        return

    def getEntries(self):
        return self.Entries

    def getEnabledEntries(self):
        for e in self.getEntries():
            if e.isEnabled():
                yield e
        
class Autoruns(object):
    ID=0

    def __init__(self, line):
        """Creates Autorun instance"""
    #Time,Entry Location,Entry,Enabled,Category,Profile,Description,Signer,Company,Image Path,Version,Launch String
        self.id = Autoruns.ID
        Autoruns.ID += 1
        s = line.split(',')
        self.time = s[0]
        self.location = s[1]
        self.name = s[2]
        self.status = s[3]
        self.category = s[4]
        self.profile = s[5]
        self.desc = s[6]
        self.signer = s[7]
        self.company = s[8]
        self.path = s[9]
        self.ver = s[10]
        self.launch = s[11]

    def isEnabled(self):
        if self.status == 'enabled':
            return True
        return False

    def getSigner(self):
        return self.signer

    def isVerified(self):
        if self.signer.find('(Verified)')==1:
            return True
        return False
          
    def __str__(self):
        return str(self.id)+' '+str(self.name)
        

class LAN(object):
    #PC group class
    PCs = []
    
    def __init__(self, IPList=[]):
        for IP in IPList:
            self.PCs.append(PC(IP))
                
    def addPC(self, PC):
        self.PCs.append(PC)

    def getPCs(self):
        return self.PCs

    def save(self, path):
        f = codecs.open(path, 'w', encoding='utf-8')
        f.write(self.__str__())
        f.close()
        return

    def load(self, path):
        #Validate!
        IPs = file2list(path)
        for IP in IPs:
            self.PCs.append(PC(IP))
        return 
        
    def __str__(self):
        output = ''
        for PC in self.PCs:
            output += PC.getIP()+'\n'
        return output

def file2text(path, codetable='utf-8'):
    """Reads file from path"""
    #get back utf-8?
    try:
        f = codecs.open(path, 'r', encoding=codetable)
    except:
        print('Cant read file: '+path)
        return ''
    text = f.read()
    f.close()
    return text

def file2list(path, codetable='utf-8'):
    """Reads utf-8 file from path
    Returns a list of lines"""
    lines = []
    try:
        f = codecs.open(path, 'r', encoding=codetable)
    except:
        print('Cant read file: '+path)
        return lines
    for line in f:
        if len(line)>0:
            lines.append(line.strip())
    f.close()
    return lines

def initLog(log_file='log.txt', out = ''):
    """ Log file init """
    try:
        f = codecs.open(log_file, 'w', encoding='utf-8')
    except:
        print('Cant open log file: '+log_file)
        return False
    # TODO add date and time
    f.write(out)
    f.close()
    return True

def writeLog(msg, log_file='log.txt', isLogFile=True):
    """ Log file init """
    if isLogFile==True:
        assert type(msg)==str
        try:
            f = codecs.open(log_file, 'a', encoding='utf-8')
        except:
            print('Cant open log file: '+log_file)
            return False
        f.write(msg)
        f.close()
        return True
    else:
        return False

def checkIP(ip=''):
    """validates IP"""
    assert type(ip)==str
    ip = ip.strip()
    #add IP validation
    return ip    
