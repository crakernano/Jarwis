#!/bin/bash

PCB_PRONAME="unified-ps"
PCB_ORDER="100146057"
PCB_SIZE="5by10" #5by5, 5by10, 10by10
PCB_COLOR="green" #default
PCB_THICKNESS="1.6" #default
PCB_SURFINISH="hasl" #default
PCB_QUANTITY="10" #default

mv *-F?Cu.gbr ${PCB_PRONAME}-front.gtl
mv *-B?Cu.gbr ${PCB_PRONAME}-back.gbl
mv *-F?Mask.gbr ${PCB_PRONAME}-mask-front.gts
mv *-B?Mask.gbr ${PCB_PRONAME}-mask-back.gbs
mv *-F?SilkS.gbr ${PCB_PRONAME}-silk-front.gto
mv *-B?SilkS.gbr ${PCB_PRONAME}-silk-back.gbo
mv *-Edge?Cuts.gbr ${PCB_PRONAME}-pcb_edges.gko
mv *.drl ${PCB_PRONAME}-drill.txt
zip O${PCB_ORDER}-${PCB_SIZE}-${PCB_COLOR}-${PCB_THICKNESS}mm-${PCB_SURFINISH}-${PCB_QUANTITY}pcs.zip ${PCB_PRONAME}-front.gtl ${PCB_PRONAME}-back.gbl ${PCB_PRONAME}-mask-front.gts ${PCB_PRONAME}-mask-back.gbs ${PCB_PRONAME}-silk-front.gto ${PCB_PRONAME}-silk-back.gbo ${PCB_PRONAME}-pcb_edges.gko ${PCB_PRONAME}-drill.txt

