# allports

Simple script to open sockets on as many ports as you want to test egress firewall settings of systems. 

Updating the range Line 22 you can change how many and which ports are open then from a client machine you can run something like


1..1024 | % {$test= new-object system.Net.Sockets.TcpClient; $wait = $test.beginConnect("192.168.1.110",$_,$null,$null); ($wait.asyncwaithandle.waitone(250,$false)); if($test.Connected){echo "$_ open"}else{echo "$_ closed"}} | select-string " "

Changing the above ports to match the sockets you have open to test firewall rules. 