# Abaqus_history_output_U
Python Script to create history output files (1 file per frame) with the displacements of an element set

For example, if you run a model called "NICOISGREAT.inp" having an element set named "ANDKIND" using
"abaqus interactive job=NICOISGREAT"
Then you can use the the following command to extract files with the displacements at each load increment (also called frame)
abaqus python disp_historyoutput.py -odb NICOISGREAT -elset ANDKIND
