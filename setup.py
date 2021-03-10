<<<<<<< Updated upstream
import configparser as cp
=======
import configparser as cp

configParser = cp.RawConfigParser()
configFileName = "config.cfg"
configParser.read(configFileName)

height = int(configParser.get('setup', 'height'))
width = int(configParser.get('setup', 'width'))
>>>>>>> Stashed changes
