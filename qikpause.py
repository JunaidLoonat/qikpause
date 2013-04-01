#!/usr/bin/env python
"""
QikPause
Junaid Loonat <junaid@packet-broker.co.za>
"""
import subprocess
from multiprocessing import Pool

def runCommand(cmdargs):
	cmdret = 0
	try:
		cmdout = subprocess.check_output(cmdargs, shell = True, universal_newlines = True)
	except subprocess.CalledProcessError as e:
		cmdret = e.returncode
		cmdout = e.output
	return (cmdret, cmdout)

# -----===== >>>>> VMware >>>>> =====-----

def vmware_pause(vm):
	(cret, cout) = runCommand(''.join(['vmrun ', 'suspend ', vm]))
	if cret is 0:
		print ''.join(['[*] Successfully suspended: ', vm])
	else:
		print ''.join(['[!] Failed to suspend: ', vm])

def vmware_list():
	(cret, cout) = runCommand('vmrun list')
	if cret is 0:
		return cout.strip().split("\n")[1:]
	return None
	
# -----===== <<<<< VMware <<<<< =====-----



if __name__ == '__main__':
	print 'QikPause by Junaid Loonat <junaid@packet-broker.co.za>'
	p = Pool(2)
	vms = vmware_list()
	if vms is not None:
		p.map(vmware_pause, vms)
		p.close()
		p.join()

