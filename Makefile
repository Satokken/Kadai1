obj-m:=myled.o
	
myled.ko:myled.c
	make -C /usr/src/linux-headers-4.4.0-1046-raspi2 M=`pwd` V=1 modules
clean:
	make -C /usr/src/linux-headers-4.4.0-1046-raspi2 M=`pwd` V=1 clean
