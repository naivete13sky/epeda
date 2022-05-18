import os,sys
# sys.path.append(r'C:\EPSemicon\EDA_TEST')

# os.system('cd C:\EPSemicon\EDA_TEST')
# os.system('start C:\EPSemicon\EDA_TEST\EPEDA.exe')
cmd=r'''cd C:\EPSemicon\EDA_TEST & start C:\EPSemicon\EDA_TEST\EPEDA.exe'''
os.system(cmd)

path=r'C:\EPSemicon\EDA_TEST'
cmd=r'''cd {} & start C:\EPSemicon\EDA_TEST\EPEDA.exe'''.format(path)

print(cmd)
