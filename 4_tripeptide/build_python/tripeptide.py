from CHARMM import CHARMM
import sys

charmm_exec = '/Users/sunhwan/local/charmm/c43b1'
charmm_data = './toppar'

charmm = CHARMM(output=sys.stdout, exec=charmm_exec, data=charmm_data)
charmm.loadParameters('top_all36_prot.rtf', 'par_all36m_prot.prm')

resnames = ['ALA', 'ARG', 'ASN', 'ASP', 'CYS', 'GLN',
            'GLU', 'GLY', 'HSD', 'ILE', 'LEU', 'LYS',
            'MET', 'PHE', 'PRO', 'SER', 'THR', 'TRP',
            'TYR', 'VAL']

for resname in resnames:
    resname = "%s_%s_%s" % (resn1, resn2, resn3)
    charmm.sendCommand("""
! Read PROA
read sequ card
* AXA
*
3
ALA %s ALA

generate PROA setup warn first NTER last CT2

ic param
ic seed PROA 1 N PROA 1 CA PROA 1 C
ic build
hbuild
""" % resname)

    charmm.sendCommand("""
write coor pdb  name %s.pdb
* tripeptide
*
""" % resname)

    charmm.sendCommand("delete atom sele all end")

charmm.sendCommand("stop")

