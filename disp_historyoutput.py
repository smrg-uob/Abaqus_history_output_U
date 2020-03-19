from odbAccess import *
from sys import argv,exit
#from odbAccess import *
from types import IntType
import os
def rightTrim(input,suffix):
    if (input.find(suffix) == -1):
        input = input + suffix
    return input

def resultadoFEM(odbName,nsetName):
     """ Print max mises location and value given odbName
         and elset(optional)
     """
     nset = nodeset = None
     region = "over the entire model"
     """ Open the output database """
     odb = openOdb(odbName)
     assembly = odb.rootAssembly
#     histPoint = HistoryPoint(node=nsetName)
#     tipHistories = odb.steps['Step-1'].getHistoryRegion(
#      point=histPoint)



     Node_Keys = odb.steps['Load'].historyRegions.keys() #Lista con los Keys de los nodos. Si se le agrega [0] te da el key del primer nodo
#     print Node_Keys
     lastFrame = odb.steps['Load'].historyRegions.values()
#     print lastFrame
     lengNodesKey=range(len(Node_Keys))
#     print lengNodesKey  # Lista del 0 al N-1 numero de nodos (ojo no es el numero de nodo)
     lastFrame2 = odb.steps['Load'].historyRegions.values()[337].historyOutputs['U1'].data
#     print '%-10.5g %10.5g' % lastFrame2[0],lastFrame2[1]
#     lastFrame1 = odb.steps['Load'].historyRegions[Node_Keys].historyOutputs['U1'].data
#     print lastFrame1
   
#     print lastFrame.description
#     print lastFrame.point.node
#     print '-----------------------------------------------'
#     print '-----------------------------------------------'
#     print lastFrame.point.node.label,lastFrame.point.node.coordinates
#     print displacement1.name
     print '-----------------------------------------------'
#     print displacement1
#print tipHistories.historyOutputs['U1']

#     outFile = open('KH_TEST.data', 'w')
#     outFile = open(odbName+'_'+nsetName+'_DISP.dat', 'w')
   
     format = '%d %E %E %E %E %E\n'

     nodes=odb.steps['Load'].historyRegions # esto da los nodos
#     timeSteps=lastFrame.historyOutputs['U1'].data[1][0]
     timeSteps1=odb.steps['Load'].historyRegions.values()[0].historyOutputs['U1'].data
#     timeSteps2=odb.steps['Load'].historyRegions.values()[307].historyOutputs['U1'].data
     nodesRange=range(len(nodes))
     timestepRange=range(len(timeSteps1))
     exit
#
     for v in nodesRange:
        Node_Key = odb.steps['Load'].historyRegions.keys()[v] 
        outFile = open(odbName+'_'+nsetName+'_'+Node_Key+'.dat', 'w')
        Frame = odb.steps['Load'].historyRegions.values()[v].point.node
#       print 'Node = %d,  X-coordinate = %E and Y-coordinate = %E' % (Frame.label, Frame.coordinates[0], Frame.coordinates[1])
#       print Frame.label, Frame.coordinates[0], Frame.coordinates[1]
#        outFile.write('Node = %d,  X-coordinate = %E and Y-coordinate = %E\n' % (Frame.label, Frame.coordinates[0], Frame.coordinates[1]))
#
        for t in timestepRange:
         Xdisp = odb.steps['Load'].historyRegions[Node_Key].historyOutputs['U1'].data[t][1] 
         Ydisp = odb.steps['Load'].historyRegions[Node_Key].historyOutputs['U2'].data[t][1]
         sumXY=Ydisp+Xdisp
         print sumXY    
#         print '%E %E %E'%(timeSteps1[t][0],Xdisp,Ydisp)
#         outFile.write('At time = %f,  X-displacement = %G and Y-displacement = %G' % (timeSteps1[t][0],Xdisp,Ydisp)
         if sumXY>0.0:
          outFile.write(format % (Frame.label, Frame.coordinates[0], Frame.coordinates[1],timeSteps1[t][0],Xdisp,Ydisp))
#          break
#        print to-give_error #this is just to make the code to stop
        outFile.close()
#       print tipHistories.historyOutputs['U1'] 


     odb.close()
#==================================================================
# S T A R T
#    
if __name__ == '__main__':
    
    odbName = None
    nsetName = None
    argList = argv
    argc = len(argList)
    i=0
    while (i < argc):
        if (argList[i][:2] == "-o"):
            i += 1
            name = argList[i]
            odbName = rightTrim(name,".odb")
        elif (argList[i][:2] == "-e"):
            i += 1
            nsetName = argList[i]
        elif (argList[i][:2] == "-h"):            
            print __doc__
            exit(0)
        i += 1
    if not (odbName):
        print ' **ERROR** output database name is not provided'
        print __doc__
        exit(1)
    resultadoFEM(odbName,nsetName)