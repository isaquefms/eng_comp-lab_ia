clc;
close;

atv2_ia=loadfls('atv2_ia');

figure(1);
plotvar(atv2_ia,"input",[1 2]);

figure(2);
plotvar(atv2_ia,"output",1); 

figure(3);
plotsurf(atv2_ia,[1 2], 1);
