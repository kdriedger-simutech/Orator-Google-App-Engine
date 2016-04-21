import json 
import sys 

print "starting... pydevd_startup.py"
 
if ':' not in config.version_id:  
  # The default server version_id does not contain ':'  
  sys.path.append("lib")  
  import ptvsd  #ptvsd.settrace() equivalent  
  ptvsd.enable_attach(secret = 'sim')
  print "Hey World,eh. Attach to:"
  print "tcp://sim@localhost:5678"
  ptvsd.wait_for_attach()

  if ptvsd.is_attached:
      print "Attached debugger, eh"
      #ptvsd.break_into_debugger()